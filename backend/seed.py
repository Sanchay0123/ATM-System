from database import SessionLocal, engine
from models import User, Base

Base.metadata.create_all(bind=engine)
db = SessionLocal()

def seed():
    if db.query(User).count() == 0:
        user = User(
            card_number="1234567890",
            pin="1234",
            balance=10000.0
        )
        db.add(user)
        db.commit()
        print("✅ Seed user created")
    else:
        print("ℹ️ Users already exist")

seed()
