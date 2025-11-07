# 🛠 Operations Guide — QR-based Unmanned Store

This doc explains how to run the **Edge (Raspberry Pi)**, **Backend (FastAPI)**, and optional **Web Admin** locally and in production-lite.

---

## 1) Prerequisites

### Backend
- Python 3.10+  
- `pip`, `venv`
- (Dev DB) SQLite / (Prod) PostgreSQL

### Edge (Raspberry Pi)
- Raspberry Pi OS (Bookworm/Bullseye)
- Camera enabled (`raspi-config`)
- Internet to reach backend

### Web (optional)
- Node.js 18+ / npm

---

## 2) Quick Start (Local Dev)

### Backend (FastAPI)
```bash
cd src/backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# env
cat > .env <<'EOF'
DB_URL=sqlite:///./store.db
JWT_SECRET=change-me
EOF

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
# Open: http://127.0.0.1:8000/docs
