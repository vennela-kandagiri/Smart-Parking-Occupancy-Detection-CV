import cv2
import json
import numpy as np

VIDEO_PATH = "data/parking.mp4"
SLOTS_PATH = "slots/slots.json"
OUTPUT_PATH = "output/result.mp4"

with open(SLOTS_PATH) as f:
    slots = json.load(f)

cap = cv2.VideoCapture(VIDEO_PATH)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter(
    OUTPUT_PATH,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (w, h)
)

GREEN = (0, 255, 0)
RED = (0, 0, 255)

def is_occupied(slot, frame):
    x1, y1, x2, y2 = slot
    roi = frame[y1:y2, x1:x2]

    if roi.size == 0:
        return False

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, mask = cv2.threshold(
        blur, 120, 255, cv2.THRESH_BINARY_INV
    )

    dark_ratio = np.count_nonzero(mask) / mask.size
    return dark_ratio > 0.25

while True:
    ret, frame = cap.read()
    if not ret:
        break

    free_count = 0

    for slot in slots:
        occupied = is_occupied(slot, frame)
        color = RED if occupied else GREEN
        if not occupied:
            free_count += 1

        cv2.rectangle(
            frame,
            (slot[0], slot[1]),
            (slot[2], slot[3]),
            color,
            8
        )

    cv2.putText(
        frame,
        f"Free Slots: {free_count}/{len(slots)}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 255),
        3
    )

    out.write(frame)

    # 🔹 Efficient display (scaled only)
    display = cv2.resize(frame, (1280, 720))
    cv2.imshow("Smart Parking System", display)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()