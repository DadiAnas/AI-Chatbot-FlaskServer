from sqlalchemy import Column, Integer, VARCHAR

from project.config import Base


class Tag(Base):
    __tablename__ = 'tag'

    id_tag = Column(Integer, primary_key=True,autoincrement=True)
    tag = Column(VARCHAR(50), nullable=False)

    def __repr__(self):
        return str({'id_tag': self.id_tag, 'tag': self.tag})
