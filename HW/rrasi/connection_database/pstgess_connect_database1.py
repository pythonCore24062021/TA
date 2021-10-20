import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy import create_engine

#engine = create_engine('postgresql://postgres:HeckfyfHfczr#1511@localhost:5432/TAQC')
#print(engine)

metadata = MetaData()
authors_table = Table('authors',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))
books_table = Table('books', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))

DB_NAME = 'TAQC'
USER = 'postgres'
PASSWORD = 'HeckfyfHfczr#1511'
HOST = 'localhost'
PORT = '5432'
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

metadata.create_all(engine)
#######

#insert_stmt = authors_table.insert(bind=engine)
#print(type(insert_stmt))
#print(insert_stmt)
#compiled_stmt = insert_stmt.compile()
#print(compiled_stmt.params)
#insert_stmt.execute(name='Alexandre Dumas') # insert a single entry
#insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}]) # a list of entries
##############

metadata.bind = engine # no need to explicitly bind the engine from now on
select_stmt = authors_table.select(authors_table.c.id>3)
print(select_stmt)
result = select_stmt.execute()
print(result)
print(result.fetchall())

with engine.connect() as con:
    rs = con.execute("SELECT * FROM public.authors;")
    print(rs)
    for row in rs:
        print(row)

print(engine)



