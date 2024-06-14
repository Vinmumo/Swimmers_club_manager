from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index = True)
    username = Column(String)
    email = Column(String)
    profile = relationship("Profile", back_populate = "users", uselist = False)

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key = True, index = True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populate = "profile")