# QR-based Unmanned Store System  
*(Raspberry Pi + FastAPI + Next.js)*  
by **FIRE STAR Design Studio**

---

## 🛰 Overview
A modular unmanned-store platform using **QR authentication** and **event-based sensing** instead of weight sensors.  
Designed for small-scale self-checkout shops, pop-ups, or community kiosks.  

**日本語要約:**  
カメラのROI解析とQRコード照合による無人販売システムです。  
重量センサーを使わず、赤外線やカメライベントで在庫変動を検知します。

---

## 🧩 System Architecture
```text
[ Customer QR ]
        │
        ▼
 ┌─────────────┐
 │ Raspberry Pi │  → Local detection (QR, IR beam)
 └─────────────┘
        │
        ▼
 ┌─────────────┐
 │  FastAPI Backend │  → QR verification / Logs / Inventory
 └─────────────┘
        │
        ▼
 ┌─────────────┐
 │ Web Admin (Next.js) │  → Dashboard & evidence viewer
 └─────────────┘
