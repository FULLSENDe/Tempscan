from ultralytics import YOLO
import cv2

model = YOLO("/opt/homebrew/runs/detect/train5/weights/best.pt")

image_path = "IR_41811.jpg"

results = model.predict(image_path, save=True)

image = cv2.imread(image_path)

boxes = results[0].boxes.xyxy.cpu().numpy()

if len(boxes) > 0:
    x_min, y_min, x_max, y_max = boxes[0]

    x_center = int((x_min + x_max) / 2)
    y_center = int((y_min + y_max) / 2)

    crop_size = 50
    half = crop_size // 2

    x1 = max(x_center - half, 0)
    y1 = max(y_center - half, 0)
    x2 = min(x_center + half, image.shape[1])
    y2 = min(y_center + half, image.shape[0])

    cropped = image[y1:y2, x1:x2]

    cv2.imwrite("cropped_result.jpg", cropped)
    print("Вырезанный участок сохранен: cropped_result.jpg")
else:
    print(" Крестик не найден.")