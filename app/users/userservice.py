from fastapi import Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.usermodel import User
from app.schemas.userschema import RegisterUser
from app.config.hashing import Hashing


class UserService:
    def get_allUser(db: Session):
        return db.query(User).all()

    def get_user(email: str, db: Session = Depends(get_db)):
        return db.query(User).filter(User.email == email).first()

    def create_user(user: RegisterUser, db: Session = Depends(get_db)):
        db_user = User(
            name=user.name,
            email=user.email,
            password=Hashing.bcrypt(user.password),
            is_admin=user.is_admin,
            is_active=user.is_active,
        )

        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        db_user.password = None

        return db_user

    def update_user(userid: int, user: RegisterUser, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()

        db_userid.name = user.name
        db_userid.email = user.email
        db_userid.password = Hashing.bcrypt(user.password)
        db_userid.is_admin = user.is_admin
        db_userid.is_active = user.is_active

        db.commit()

        return db_userid

    def deleteUser(userid: int, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()

        db.delete(db_userid)

        db.commit()

        return db_userid

