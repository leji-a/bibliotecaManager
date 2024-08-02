import click
from commands.commands import add, find, display, delete

@click.group()
def main():
    "--- Administrador simple de una biblioteca ---"
    pass


main.add_command(add)
main.add_command(find)
main.add_command(display)
main.add_command(delete)

if __name__ == "__main__":
    main()
