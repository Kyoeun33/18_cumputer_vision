from ultralytics import YOLO

# COCO로 사전 학습된 YOLOv3u 모델을 불러옵니다
model = YOLO("yolov3u.pt")
# 모델 정보 표시(선택 사항)
model.info()
# COCO8 예제 데이터셋으로 100 에포크 동안 모델 학습
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

