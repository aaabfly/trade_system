from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import app.app
import os


Base = declarative_base()

databese_purchaseorder_file = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'purchaseorder.db')
purchase_engine = create_engine('sqlite:///' + databese_purchaseorder_file, convert_unicode=True)

db_session_pu = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=purchase_engine))
Base.query = db_session_pu.query_property()


database_productdetail_file = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'productdetails.db')

product_engine = create_engine('sqlite:///' + databese_purchaseorder_file, convert_unicode=True)

db_session_pr = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=product_engine))

Base.query = db_session_pr.query_property()