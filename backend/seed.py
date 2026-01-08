from database import SessionLocal
from models import User

def seed():
    db = SessionLocal()

    user = db.query(User).filter_by(card_number="1234567890").first()

    if not user:
        demo_user = User(
            card_number="1234567890",
            pin="1234",
            balance=10000.0
        )
        db.add(demo_user)
        db.commit()
        print("✅ Demo user created")
    else:
        print("ℹ️ Demo user already exists")
