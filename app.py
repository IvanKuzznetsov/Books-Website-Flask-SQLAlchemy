from flask import Flask, render_template

from database import db
from model import Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    novel = Genre(name="Роман")
    db.session.add(novel)

    adventure = Genre(name="Приключение")
    db.session.add(adventure)

    comedy = Genre(name="Комедия")
    db.session.add(comedy)

    satire = Genre(name="Сатира")
    db.session.add(satire)

    story = Genre(name="Повесть")
    db.session.add(story)

    db.session.add(Book(title="Война и мир", author="Толстой Л.Н.", genre=novel))
    db.session.add(Book(title="Капитанская дочка", author="Пушкин А.С.", genre=novel))
    db.session.add(Book(title="Пятнадцатилетний капитан", author="Жюль Верн", genre=adventure))
    db.session.add(Book(title="Преступление и наказание", author="Достоевский Ф.М.", genre=novel))
    db.session.add(Book(title="Евгений Онегин", author="Пушкин А.С.", genre=novel))
    db.session.add(Book(title="Обломов", author="Гончаров И.А.", genre=novel))
    db.session.add(Book(title="Мертвые души", author="Гоголь Н.В.", genre=novel))
    db.session.add(Book(title="Ревизор", author="Гоголь Н.В.", genre=comedy))
    db.session.add(Book(title="Герой нашего времени", author="Лермонтов М.Ю.", genre=novel))
    db.session.add(Book(title="Братья Карамазовы", author="Достоевский Ф.М.", genre=novel))
    db.session.add(Book(title="Идиот", author="Достоевский Ф.М.", genre=novel))
    db.session.add(Book(title="Отцы и дети", author="Тургенев И.С.", genre=novel))
    db.session.add(Book(title="Анна Каренина", author="Толстой Л.Н.", genre=novel))
    db.session.add(Book(title="Горе от ума", author="Грибоедов А.С.", genre=satire))
    db.session.add(Book(title="Му-му", author="Тургенев И.С.", genre=story))
    db.session.add(Book(title="Собачье сердце", author="Булгаков М.А.", genre=satire))
    db.session.add(Book(title="Недоросль", author="Фонвизин Д.И.", genre=comedy))
    db.session.add(Book(title="Вечера на хуторе близ Диканьки", author="Гоголь Н.В.", genre=story))
    db.session.add(Book(title="Тарас Бульба", author="Гоголь Н.В.", genre=story))
    db.session.add(Book(title="Мастер и Маргарита", author="Булгаков М.А.", genre=novel))

    db.session.commit()


@app.route("/books/")
def all_books():
    query = db.select(Book).order_by(Book.id.desc()).limit(15)
    books = db.session.execute(query).scalars()
    return render_template("all_books.html", books=books)


@app.route("/books/genre/<int:genre_id>/")
def books_by_genre(genre_id):
    query = db.select(Book).filter(Book.genre_id == genre_id).order_by(Book.id.desc())
    books = db.session.execute(query).scalars()
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "books_by_genre.html",
        genre_name=genre.name,
        books=books,
    )


if __name__ == "__main__":
    app.run()
