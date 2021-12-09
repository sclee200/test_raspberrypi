from flask import Flask
import cv2
import threading
from flask import Response

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "<h1>Hello World! I'm sangchul Lee</h1>"

video_frame = ''
def encodingframe():
    global video_frame
    while True:
        ret, encoded_image = cv2.imencode('.jpg', video_frame)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')
    return   
@app.route('/streaming')
def streamframe():
    return Response(encodingframe(), mimetype='multipart/x-mixed-replace; boundary=frame')

def captureframe():
    cap=cv2.VideoCapture(0)
    global video_frame
    while cap.isOpened():
        ret, frame = cap.read()
        # cv2.imshow('webcam', frame)
        video_frame = frame.copy()
        key = cv2.waitKeyEx(30)

# /dev/video0
if __name__ == "__main__":
    cap_thread=threading.Thread(target=captureframe)
    cap_thread.daemon = True
    cap_thread.start()
    # cap_thread.join()

    app.run(host="0.0.0.0", port="8000")

    