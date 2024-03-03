from flet import *
import sqlite3

def main(page:Page):
    page.add(
        Text('Olá mundo')
    )

app(target=main)