from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy import create_engine

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
PASSWORD = 'root'
HOST = 'localhost'
PORT = '5432'
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
#create DB
metadata.create_all(engine)
############

####

# insert_stmt = authors_table.insert(bind=engine)
# print(type(insert_stmt))
# print (insert_stmt)
# compiled_stmt = insert_stmt.compile()
# print(compiled_stmt.params)
# insert_stmt.execute(name='Alexandre Dumas') # insert a single entry
# insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}]) # a list of entries
######
metadata.bind = engine # no need to explicitly bind the engine from now on
select_stmt = authors_table.select(authors_table.c.id>3)
print(select_stmt)
result = select_stmt.execute()
print(result)
print(result.fetchall())

with engine.connect() as con:

    rs = con.execute("""SELECT authors.id, authors.name 
                        FROM authors 
                        WHERE authors.id > {id};""".format(id=3))

    for row in rs:
        print(row)
#
# del_stmt = authors_table.delete()
#
# del_stmt.execute(whereclause=text("name='Mr Y'"))
#
# # del_stmt.execute() # delete all
# #



print("\n\nAll data:\n")
with engine.connect() as con:
    rs = con.execute("SELECT * FROM public.books;")

    for row in rs:
        print(row)

with engine.connect() as con:
    rs = con.execute("SELECT * FROM public.authors;")

    for row in rs:
        print(row)



