from sqlalchemy.orm import Session
from database import SessionLocal
import models

def create_swimmer(db: Session, name: str, age: int, style: str, best_lap: str):
    new_swimmer = models.Swimmer(name=name, age=age, style=style, best_lap=best_lap)
    db.add(new_swimmer)
    db.commit()
    db.refresh(new_swimmer)
    return new_swimmer

def create_coach(db: Session, name: str, age: int, swimmer_id: int):
    new_coach = models.Coach(name=name, age=age, swimmer_id=swimmer_id)
    db.add(new_coach)
    db.commit()
    db.refresh(new_coach)
    return new_coach

def main():
    db = SessionLocal()
    try:
        while True:
            print("Choose an option:")
            print("1. Add a new swimmer")
            print("2. Add a new coach")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                name = input("Name: ")
                age = int(input("Age: "))
                style = input("Style: ")
                best_lap = input("Best Lap: ")

                swimmer = create_swimmer(db, name, age, style, best_lap)
                print(f"Swimmer {swimmer.name} added with ID {swimmer.id}")

            elif choice == '2':
                name = input("Name: ")
                age = int(input("Age: "))
                swimmer_id = int(input("Swimmer ID to be allocated: "))

                # Check if the swimmer ID exists
                swimmer = db.query(models.Swimmer).filter(models.Swimmer.id == swimmer_id).first()
                if swimmer:
                    coach = create_coach(db, name, age, swimmer_id)
                    print(f"Coach {coach.name} added with ID {coach.id} and allocated to swimmer ID {swimmer_id}")
                else:
                    print(f"Swimmer ID {swimmer_id} does not exist")

            elif choice == '3':
                break

            else:
                print("Invalid choice, please try again.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
