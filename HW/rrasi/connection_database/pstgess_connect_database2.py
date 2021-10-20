from sqlalchemy import create_engine



DB_NAME = 'library2'
USER = 'postgres'
PASSWORD = 'HeckfyfHfczr#1511'
HOST = 'localhost'
PORT = '5432'
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

with engine.connect() as con:
    rs = con.execute("SELECT * FROM public.books;")
    print(rs)
    for row in rs:
        print(row)

print(engine)
