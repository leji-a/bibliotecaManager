import click


def print_format(book):
    if "title" not in book:
        click.echo("Error: Book does not have a 'title'. Here's the problematic book: ")
        click.echo(book)
        return
    print("{")
    print(f'    Titulo: {book["title"]},')
    print(f'    Autor: {book["author"]},')
    print(f'    Editorial: {book["editorial"]},')
    print(f'    Género: {book["genre"]},')
    print(f'    Ubicación en biblioteca: {book["location"]},')
    print(f'    Copias disponibles: {book["copies"]}')
    print("}")
