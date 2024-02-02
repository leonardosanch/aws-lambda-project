
from lib_users.config import Settings
from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import update


class DataBase:
    def __init__(self):
        self.engine = create_engine(Settings().DATABASE_URL)
        self.metadata = sqlalchemy.MetaData()
        self.connection = self.engine.connect()
        self.user =  sqlalchemy.Table(
           'usuarios', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('nombre', String(255)),
            Column('apellido', String(255)),
            Column('ciudad', String(255))
        )
        
                                   
        
    #def get_users(self):
     #   query = sqlalchemy.select(
      #      self.user.c.id,
       #     self.user.c.nombre,
        #    self.user.c.apellido,
        #    self.user.c.ciudad
       # )     # Correcto
       # result = self.connection.execute(query)
       # return [row._asdict() for row in result.fetchall()] 
       
    def get_users(self):
        query = sqlalchemy.select(
            self.user.c.id,  # Selecciona las columnas explicitly
            self.user.c.nombre,
            self.user.c.apellido,
            self.user.c.ciudad
        ).select_from(self.user)  # Especifica la tabla de la que se obtienen los datos
        result = self.connection.execute(query)
        return [row._asdict() for row in result.fetchall()]

    def create_user(self, user=dict):
        session = Session(self.engine, future=True)
        query = (
            self.user.insert()
            .values(user)
            .returning(
                self.user.c.id,
                self.user.c.nombre,
                self.user.c.apellido,
                self.user.c.ciudad,
           
            )
        )
        result = session.execute(query)
        session.commit()
        session.close()
        return dict(result.fetchone())

    def get_user_by_id(self, id):
        query = sqlalchemy.select([self.user]).where(self.user.c.id == id)
        result = self.connection.execute(query)
        return result.fetchone()

    #def update_user(self, id, user):
       # session = Session(self.engine, future=True)
       # query = (
        #    self.user.update()
         #   .where(self.user.c.id == id)
         #   .values(user)
         #   .returning(
          #      self.user.c.id,
          #      self.user.c.nombre,
           #     self.user.c.apellido,
           #     self.user.c.ciudad,
           # )
       # )
      #  result = session.execute(query)
      #  session.commit()
       # session.close()
       # return dict(result.fetchone())
       
    def update_user(self, id, data):
        session = Session(self.engine, future=True)
        query = (
            update(self.user)
            .where(self.user.c.id == id)
            .values(**data)
        )
        session.execute(query)
        session.commit()
        session.close()