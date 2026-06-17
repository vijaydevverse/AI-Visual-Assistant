from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame)

    detections = []

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            name = model.names[cls_id]
            conf = float(box.conf[0])

            if conf > 0.6:
                x1, y1, x2, y2 = box.xyxy[0]

                detections.append({
                    "name": name,
                    "conf": conf,
                    "box": (int(x1), int(y1), int(x2), int(y2))
                })

    return detections