from typing import Any

from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound


class FilmesRepository:
    def __init__(self):
        self.connection = DBConnectionHandler()

    def select(self) -> Any:
        session = self.connection.get_session()
        response = session.query(Filmes).all()
        session.close()
        return response

    def select_drama_filmes(self) -> Any:
        session = self.connection.get_session()
        response = session.query(Filmes).filter(Filmes.genero == "Drama").all()
        session.close()
        return response

    def insert(self, filme: Filmes) -> Any:
        session = self.connection.get_session()
        session.add(filme)
        session.commit()
        session.close()

    def update(self, filme: Filmes) -> Any:
        session = self.connection.get_session()
        session.merge(filme)
        session.commit()
        session.close()

    def delete(self, titulo: str) -> Any:
        session = self.connection.get_session()
        try:
            filme = session.query(Filmes).filter(Filmes.titulo == titulo).one()
            session.delete(filme)
            session.commit()
        except NoResultFound:
            session.rollback()
        finally:
            session.close()
