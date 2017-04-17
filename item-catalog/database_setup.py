from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    """This class will create a 'user' table in database."""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
          "id": self.id,
          "name": self.name,
          "email": self.email,
          "picture": self.picture,
        }


class Category(Base):
    """This class will create a 'category' table in database."""
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
          "id": self.id,
          "name": self.name,
          "user_id": self.user_id,

        }


class Item(Base):
    """This class will create a 'item' table in database."""
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    category = relationship(Category)
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
          "id": self.id,
          "name": self.name,
          "category_id": self.category_id,
          "user_id": self.user_id,
        }


engine = create_engine("sqlite:///itemCatalog.db")


Base.metadata.create_all(engine)
