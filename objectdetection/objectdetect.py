import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def ShowVideo(filename):
    cap = cv2.VideoCapture("uploads/"+filename)
    if (cap.isOpened()== False):
        print("Error opening video file")
    while True:
        frame = cap.read()[1]
        if frame is None:
            break
        result = model(frame)
        print(result)
        #frame = cv2.resize(frame, (640,360))
        df = result.pandas().xyxy[0]
        for ind in df.index:
            x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
            x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
            label = df['name'][ind]
            conf = df['confidence'][ind]
            text = label + " " + str(conf)
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255, 255, 0), 2)
            cv2.putText(frame, text, (x1, y1-5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)
        output_frame = np.array(frame)
        ret, buffer = cv2.imencode('.jpg', output_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
