import datetime
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship, backref
from project.config import Base


class Response(Base):
    __tablename__ = 'response'

    id_response = Column(Integer, primary_key=True, autoincrement=True)
    response = Column(VARCHAR(250), nullable=True)

    tag_id = Column(Integer, ForeignKey('tag.id_tag'),
                    nullable=False)
    tag = relationship('Tag',
                       backref=backref('responses', lazy=True))

    def __repr__(self):
        return str({'id_response': self.id_response, 'response': self.response,'tag_id': self.tag_id})
