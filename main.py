import click
from commands.commands import *


@click.group()
def main():
    "--- Administrador simple de una biblioteca ---"
    pass

commands = [add, display, modify, delete]
for command in commands:
    main.add_command(command)


if __name__ == "__main__":
    main()
