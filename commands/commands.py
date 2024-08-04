import click
import json_manager
from commands.utils import print_format


@click.command()
def add():
    "--- Añade un libro ---"

    title = input("Título del libro > ")
    author = input("Autor del libro > ")
    editorial = input("Editorial del libro > ")
    genre = input("Género del libro > ")
    location = input("Ubicación en la biblioteca > ")

    while True:
        try:
            copies = int(input("Copias disponibles > "))
            break
        except ValueError:
            print("El número de copias debe ser un número entero. Intenta de nuevo.")

    new_book = {
        "title": title,
        "author": author,
        "editorial": editorial,
        "genre": genre,
        "location": location,
        "copies": copies
    }

    books = json_manager.read_json()
    books.append(new_book)
    json_manager.write_json(books)


@click.command()
@click.argument("keyword")
def find(keyword):
    '--- Busqueda de libro por "titulo" o "autor" ---'
    books = json_manager.read_json()
    for book in books:
        if keyword in book["title"] or keyword in book["author"]:
            print_format(book)


@click.command()
def display():
    "--- Muestra todos los libros ---"
    books = json_manager.read_json()
    for book in books:
        print_format(book)


@click.command()
@click.argument("title")
def delete(title):
    '--- Borra un libro por "titulo" ---'
    books = json_manager.read_json()
    new_books = [book for book in books if book["title"] != title]
    if len(books) == len(new_books):
        click.echo("No title found")
    else:
        click.echo(f'Book titled "{title}" deleted.')
        json_manager.write_json(new_books)
