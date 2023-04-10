from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.usermodel import User
from app.schemas.reviewschema import Review
from app.config.token import get_currentUser
from .reviewservice import ReviewService

router = APIRouter(prefix="/review", tags=["Review"])


@router.get("/")
def getAllReview(db: Session = Depends(get_db)):
    return ReviewService.get_all(db=db)


@router.post("/create/{productid}")
def createReview(
    productid: int,
    request: Review,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_currentUser),
):
    return ReviewService.create_review(
        request=request, productId=productid, db=db, current_user=current_user
    )


@router.post("/feno")
def fenoReview(request: Review):
    return request

