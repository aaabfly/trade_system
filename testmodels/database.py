from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
from app.app import app
=======
>>>>>>> db_create
import os

databese_file = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'purchaseorder.db')
<<<<<<< HEAD
purchase_engine = create_engine('sqlite:///' + databese_purchaseorder_file, convert_unicode=True)

db_session_pu = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=purchase_engine))
Base.query = db_session_pu.query_property()


database_productdetail_file = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'productdetails.db')

product_engine = create_engine('sqlite:///' + "databese_productdetail_file", convert_unicode=True)
=======
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
>>>>>>> db_create


def init_db():
    import testmodels.models
    Base.metadata.create_all(bind=engine)
