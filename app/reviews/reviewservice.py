from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.productmodel import ProductModel
from app.config.token import get_currentUser
from app.models.reviewmodel import ReviewModel
from app.models.usermodel import User
from app.config.database import get_db
from app.schemas.reviewschema import Review


class ReviewService:
    def get_all(db: Session):
        return db.query(ReviewModel).all()

    def create_review(
        request: Review,
        productId: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_currentUser),
    ):
        product_by_id = (
            db.query(ProductModel).filter(ProductModel.id == productId).first()
        )

        try:

            review_new = ReviewModel(
                name=current_user.name,
                user_id=current_user.id,
                rating=request.rating,
                comment=request.comment,
            )
            review_new.product_id = product_by_id.id

            db.add(review_new)
            db.commit()
        except Exception as e:
            return e

        return "Done"

