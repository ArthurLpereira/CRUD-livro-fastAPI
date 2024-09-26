from peewee import SqliteDatabase
database = SqliteDatabase('database.db')
def start_database():
    database.connect()
    from models.livros import livrosDB
    database.create_tables(
        [livrosDB]
    )
def end_database():
    database.close()