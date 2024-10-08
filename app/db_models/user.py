from sqlalchemy.orm import Mapped, mapped_column, relationship  # type: ignore
from flask_login import UserMixin  # type: ignore

from app import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    profile_image_id: Mapped[str] = mapped_column(nullable=True)
    profile_image_url: Mapped[str] = mapped_column(nullable=True)

    reset_token: Mapped["PasswordResetToken"] = relationship("PasswordResetToken", back_populates="user")  # type: ignore

    letterboxd_username: Mapped[str] = mapped_column(unique=True)
    ratings: Mapped[list["MovieRating"]] = relationship("MovieRating", back_populates="user")  # type: ignore

    def get_id(self):
        return self.id
