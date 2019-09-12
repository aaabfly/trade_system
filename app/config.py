from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from testmodels.database import purchase_engine, product_engine

app = Flask(__name__)

SQLALCHEMY_DATABASE_BIND = {'purchaseorderdb': purchase_engine,
                            'productdetaildb' : product_engine }
