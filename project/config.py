from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#engine = create_engine('mysql://root:@localhost:3306/chatbot__db?charset=utf8', pool_size=20, max_overflow=0)
engine = create_engine('sqlite:///database/chatbot__db?charset=utf8')

# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)#, expire_on_commit=False)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()


def add_object(instance):
    session = session_factory()
    try:
        session.add(instance)
        session.commit()
        session.close()
        return True
    except:
        session.rollback()
        return False


def update_object(instance):
    session = session_factory()
    try:
        session.merge(instance)
        session.commit()
        session.close()
        return True
    except:
        session.rollback()
        return False


def get_object(class_name, object_id):
    session = session_factory()
    try:
        the_objects = session.query(class_name).get(object_id)
        session.close()
        return the_objects
    except:
        return False


def get_objects(class_name):
    session = session_factory()
    try:
        objects_query = session.query(class_name)
        session.close()
        return objects_query.all()
    except:
        raise


def delete_object(class_name, object_id):
    session = session_factory()
    try:
        the_object = session.query(class_name).get(object_id)
        session.delete(the_object)
        session.commit()
        session.close()
        return True
    except:
        session.rollback()
        return False

class BrokerConfig:
    enable_utc = True
    timezone = 'Europe/London'