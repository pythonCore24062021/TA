
from sqlalchemy import create_engine



DB_NAME = 'library2'
USER = 'postgres'
PASSWORD = 'root'
HOST = 'localhost'
PORT = '5432'
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

with engine.connect() as con:
    rs = con.execute("SELECT * FROM public.book_book;")
    print(rs)
    for row in rs:
        print(row)

print(engine)



