import cv2, requests, time, yaml
from pyzbar.pyzbar import decode

cfg = yaml.safe_load(open("config.yaml"))
cap = cv2.VideoCapture(cfg["CAMERA_ID"])

def verify(qr_text:str)->bool:
    try:
        r = requests.post(f'{cfg["BACKEND_URL"]}/auth/verify-qr', json={"code": qr_text, "device": cfg["DEVICE_ID"]}, timeout=3)
        return r.status_code == 200 and r.json().get("ok") is True
    except Exception:
        return False

while True:
    ok, frame = cap.read()
    if not ok:
        time.sleep(0.2)
        continue
    for code in decode(frame):
        text = code.data.decode("utf-8")
        if verify(text):
            print("ACCESS OK", text)
        else:
            print("DENIED", text)
    if cv2.waitKey(1) == 27:
        break
cap.release()
