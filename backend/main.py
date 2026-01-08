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

Base.metadata.create_all(bind=engine)
seed()
train()

# Serve frontend static files from frontend
# app.mount("/static", StaticFiles(directory="static"), name="static")

# For render
from fastapi.staticfiles import StaticFiles

app.mount(
    "/", 
    StaticFiles(directory="static", html=True), 
    name="frontend"
)

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

# ---------- API ROUTES ----------

@app.post("/login")
def login(card_number: str, pin: str):
    db = SessionLocal()
    user = db.query(User).filter_by(card_number=card_number, pin=pin).first()
    if not user:
        return {"success": False}
    return {"success": True, "balance": user.balance}

@app.post("/withdraw")
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

@app.post("/deposit")
def deposit(card_number: str, amount: float):
    db = SessionLocal()
    user = db.query(User).filter_by(card_number=card_number).first()
    user.balance += amount
    db.commit()
    return {"status": "success", "balance": user.balance}

@app.get("/assistant")
def assistant(msg: str):
    return {"reply": respond(msg)}
