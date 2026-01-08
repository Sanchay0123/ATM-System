from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import Base, engine, SessionLocal
from models import User
from fraud_model import train, is_fraud
from chatbot import respond
from seed import seed

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB + seed + ML
Base.metadata.create_all(bind=engine)
seed()
train()

# ---------------- API ROUTES ----------------

@app.post("/api/login")
def login(card_number: str, pin: str):
    db = SessionLocal()
    user = db.query(User).filter_by(card_number=card_number, pin=pin).first()
    if not user:
        return {"success": False}
    return {"success": True, "balance": user.balance}

@app.post("/api/withdraw")
def withdraw(card_number: str, amount: float):
    db = SessionLocal()
    user = db.query(User).filter_by(card_number=card_number).first()

    if is_fraud(amount):
        return {"status": "fraud_detected"}

    if amount > user.balance:
        return {"status": "insufficient_balance"}

    user.balance -= amount
    db.commit()
    return {"status": "success", "balance": user.balance}

@app.post("/api/deposit")
def deposit(card_number: str, amount: float):
    db = SessionLocal()
    user = db.query(User).filter_by(card_number=card_number).first()
    user.balance += amount
    db.commit()
    return {"status": "success", "balance": user.balance}

@app.get("/api/assistant")
def assistant(msg: str):
    return {"reply": respond(msg)}

# ---------------- FRONTEND ----------------

app.mount(
    "/", 
    StaticFiles(directory="static", html=True), 
    name="frontend"
)
