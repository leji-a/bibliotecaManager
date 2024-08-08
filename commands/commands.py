import click
import commands.json_manager as json_manager
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
        "copies": copies,
    }

    books = json_manager.read_json()
    books.append(new_book)
    json_manager.write_json(books)




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


@click.command()
@click.argument("title")
def modify(title):
    '--- Modifica un libro por "titulo" ---'
    books = json_manager.read_json()
    for book in books:
        if book["title"] == title:
            new_title = input("Nuevo título del libro > ")
            new_author = input("Nuevo autor del libro > ")
            new_editorial = input("Nueva editorial del libro > ")
            new_genre = input("Nuevo género del libro > ")
            new_location = input("Nueva ubicación en la biblioteca > ")
            while True:
                try:
                    new_copies = int(input("Nuevas copias disponibles > "))
                    break
                except ValueError:
                    print("El número de copias debe ser un número entero. Intenta de nuevo.")
            updated_book = {
                "title": new_title,
                "author": new_author,
                "editorial": new_editorial,
                "genre": new_genre,
                "location": new_location,
                "copies": new_copies,
            }
            updated_books = [updated_book if b["title"] == title else b for b in books]
            json_manager.write_json(updated_books)