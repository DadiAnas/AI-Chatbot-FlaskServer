from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship, backref
from project.config import Base


class Pattern(Base):
    __tablename__ = 'pattern'

    id_pattern = Column(Integer, primary_key=True, autoincrement=True)
    pattern = Column(VARCHAR(250), nullable=True)

    tag_id = Column(Integer, ForeignKey('tag.id_tag'),
                    nullable=False)
    tag = relationship('Tag',
                       backref=backref('patterns', lazy=True))

    def __repr__(self):
        return str({'id_pattern': self.id_pattern, 'pattern': self.pattern,'tag_id': self.tag_id})
