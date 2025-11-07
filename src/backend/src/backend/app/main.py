from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Unmanned Store API")

class QR(BaseModel):
    code: str
    device: str

@app.post("/auth/verify-qr")
def verify(qr: QR):
    if qr.code.startswith("DEMO-"):
        return {"ok": True}
    raise HTTPException(status_code=401, detail="invalid")
