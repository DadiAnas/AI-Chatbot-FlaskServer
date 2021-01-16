import datetime
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship, backref
from project.config import Base


class Context(Base):
    __tablename__ = 'context'

    id_context = Column(Integer, primary_key=True, autoincrement=True)
    context = Column(VARCHAR(250), nullable=True)

    tag_id = Column(Integer, ForeignKey('tag.id_tag'),
                    nullable=False)
    tag = relationship('Tag',
                       backref=backref('contexts', lazy=True))

    def __repr__(self):
        return str({'id_pattern': self.id_context, 'pattern': self.context,'tag_id': self.tag_id})
