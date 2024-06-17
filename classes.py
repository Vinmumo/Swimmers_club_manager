from sqlalchemy.orm import Session
import models

class SwimmerService:
    def __init__(self, db: Session):
        self.db = db

    def create_swimmer(self, name: str, age: int, style: str, best_lap: str):
        new_swimmer = models.Swimmer(name=name, age=age, style=style, best_lap=best_lap)
        self.db.add(new_swimmer)
        self.db.commit()
        self.db.refresh(new_swimmer)
        return new_swimmer

class CoachService:
    def __init__(self, db: Session):
        self.db = db

    def create_coach(self, name: str, age: int, swimmer_id: int):
        # Check if the swimmer ID exists
        swimmer = self.db.query(models.Swimmer).filter(models.Swimmer.id == swimmer_id).first()
        if swimmer:
            new_coach = models.Coach(name=name, age=age, swimmer_id=swimmer_id)
            self.db.add(new_coach)
            self.db.commit()
            self.db.refresh(new_coach)
            return new_coach
        else:
            return None
