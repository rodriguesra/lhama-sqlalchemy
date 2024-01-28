import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

password = os.getenv("PASSWORD")


class DBConnectionHandler:
    def __init__(self):
        self.engine = create_engine(
            f"mysql+mysqldb://root:{password}@localhost:3306/cinema"
        )
        self.sessionmaker = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.conn = self.engine.connect()
        self.session = self.sessionmaker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.conn.close()

    def get_session(self):
        return self.sessionmaker()

    def get_engine(self):
        return self.engine

    def get_connection(self):
        return self.engine.connect()

    def close(self):
        self.engine.dispose()
