from sqlalchemy import func
from sqlalchemy.orm import relationship

from database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publication_date = db.Column(db.Date, nullable=False, default=func.current_date())
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    annotation = db.Column(db.Text, nullable=True, default="нет")

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete="SET NULL"))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"Book(name={self.title!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    books = relationship("Book", back_populates="genre")

    def __repr__(self):
        return f"Genre(name={self.name!r})"
