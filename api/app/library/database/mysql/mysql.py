import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class MYSQLConnection:
    def __init__(self):
        pass

    def get_session(self):
        try:
            server = '3.130.126.210'
            port = '3309'
            database = 'habi_db'
            user = 'admin'
            password = 'HANrhz5u7e3jKqVQ'
            sql_alchemy_url = 'mysql+pymysql://' + user + ':' + password + '@' + server + ':' + port + '/' + database
            engine = create_engine(
                sql_alchemy_url
            )
            session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            session = session_maker()
            return session
        except NameError:
            logging.debug('There were an error creating the sql server connection')
            return None




