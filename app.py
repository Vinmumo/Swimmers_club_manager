from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

def create_swimmer(db: Session, name: str, age: int, style: str, best_lap: str):
    new_swimmer = models.Swimmer(name=name, age=age, style=style, best_lap=best_lap)
    db.add(new_swimmer)
    db.commit()
    db.refresh(new_swimmer)
    return new_swimmer

def main():
    db = SessionLocal()
    try:
        print("Add a new swimmer")
        name = input("Name: ")
        age = int(input("Age: "))
        style = input("Style: ")
        best_lap = input("Best Lap: ")

        swimmer = create_swimmer(db, name, age, style, best_lap)
        print(f"Swimmer {swimmer.name} added with ID {swimmer.id}")
    finally:
        db.close()

if __name__ == "__main__":
    main()