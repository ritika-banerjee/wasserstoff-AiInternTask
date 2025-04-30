from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Load DB config from .env
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/game")

# Set up DB connection
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the table for global guess counts
class Guess(Base):
    __tablename__ = "guesses"
    word = Column(String, primary_key=True, index=True)
    count = Column(Integer, default=0)

# Create table if not exists
def init_db():
    Base.metadata.create_all(bind=engine)

# Increment global guess count (or create new row if not exists)
def increment_global_guess_count(word: str) -> int:
    session = SessionLocal()
    word = word.lower()

    try:
        guess = session.query(Guess).filter_by(word=word).first()
        if guess:
            guess.count += 1
        else:
            guess = Guess(word=word, count=1)
            session.add(guess)
        session.commit()
        return guess.count
    except Exception as e:
        print(f"[DB Error] {e}")
        session.rollback()
        return 1
    finally:
        session.close()

# Get global guess count (used for history/stats)
def get_global_guess_count(word: str) -> int:
    session = SessionLocal()
    word = word.lower()
    try:
        guess = session.query(Guess).filter_by(word=word).first()
        return guess.count if guess else 0
    except Exception as e:
        print(f"[DB Error] {e}")
        return 0
    finally:
        session.close()
