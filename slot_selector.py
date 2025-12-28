import cv2
import json

VIDEO_PATH = "data/parking.mp4"
SLOTS_PATH = "slots/slots.json"

cap = cv2.VideoCapture(VIDEO_PATH)
ret, frame = cap.read()
cap.release()

if not ret:
    raise RuntimeError("Cannot read video")

slots = []
points = []

def mouse_click(event, x, y, flags, param):
    global points, slots

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Clicked: {x}, {y}")

        if len(points) == 2:
            (x1, y1), (x2, y2) = points
            slot = [min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)]
            slots.append(slot)

            cv2.rectangle(
                frame,
                (slot[0], slot[1]),
                (slot[2], slot[3]),
                (0, 255, 0),
                4
            )
            points.clear()

cv2.namedWindow("Select Parking Slots")
cv2.setMouseCallback("Select Parking Slots", mouse_click)

while True:
    display = cv2.resize(frame, (1280, 720))
    cv2.imshow("Select Parking Slots", display)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

with open(SLOTS_PATH, "w") as f:
    json.dump(slots, f)

print("Slots saved.")