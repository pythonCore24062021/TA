from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_DB_NAME = 'TAQC'
_USER = 'postgres'
_PASSWORD = 'HeckfyfHfczr#1511'
_HOST = 'localhost'
_PORT = '5432'
_engine = create_engine(f'postgresql://{_USER}:{_PASSWORD}@{_HOST}:{_PORT}/{_DB_NAME}')
_Session = sessionmaker(bind=_engine)  # bound session
SESSION = _Session()