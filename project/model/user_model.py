# coding=utf-8

from sqlalchemy import Column, VARCHAR, Integer

from project.config import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(80), unique=True, nullable=False)
    user_email = Column(VARCHAR(120), unique=True, nullable=False)
    user_first_name = Column(VARCHAR(80))
    user_last_name = Column(VARCHAR(80))
    user_password = Column(VARCHAR(120))

    def __repr__(self):
        return str({'user_id': self.user_id,
                    'username': self.username,
                    'user_email': self.user_email,
                    'user_first_name': self.user_first_name,
                    'user_last_name': self.user_last_name})
