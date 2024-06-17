from sqlalchemy.orm import Session
from database import SessionLocal
from classes import SwimmerService, CoachService

def main():
    db = SessionLocal()
    swimmer_service = SwimmerService(db)
    coach_service = CoachService(db)

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

                swimmer = swimmer_service.create_swimmer(name, age, style, best_lap)
                print(f"Swimmer {swimmer.name} added with ID {swimmer.id}")

            elif choice == '2':
                name = input("Name: ")
                age = int(input("Age: "))
                swimmer_id = int(input("Swimmer ID to be allocated: "))

                coach = coach_service.create_coach(name, age, swimmer_id)
                if coach:
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
