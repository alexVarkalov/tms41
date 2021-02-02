from oop.book.validators import (
    validate_pages,
    validate_year,
    validate_author,
    validate_price,
)


class Book:
    def __init__(self, pages, year, author, price):
        validate_pages(pages)
        self.pages = pages

        validate_year(year)
        self.year = year

        validate_author(author)
        self.author = author

        validate_price(price)
        self.price = price
