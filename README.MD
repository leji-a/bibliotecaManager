# Administrador de Biblioteca

Este es un programa simple para administrar una biblioteca. Permite añadir, buscar, mostrar y eliminar libros.

## Tabla de Contenidos
- [Instalación](#instalación)
- [Uso](#uso)
- [Comandos](#comandos)
- [Dependencias](#dependencias)

## Instalación

Sigue estos pasos para instalar el proyecto:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/leji-a/bibliotecaManager.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd bibliotecaManager
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar el programa, usa el siguiente comando:
```bash
python main.py
```

## Comandos

Aquí hay una lista de comandos útiles para trabajar con el proyecto:

- `python main.py add`: Añade un libro.
- `python main.py find <keyword>`: Busca un libro por título o autor.
- `python main.py display`: Muestra todos los libros.
- `python main.py delete <title>`: Borra un libro por título.

## Dependencias

Principales dependencias del proyecto:

- `click`: ^8.0.0
