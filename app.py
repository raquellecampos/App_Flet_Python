from flet import *
import sqlite3

# no terminal digitar: flet - r e o nome do arquivo para rodar a aplicação nesse caso app.py
def main(page:Page):
    page.add(
        Text('Olá mundo')
    )

app(target=main)