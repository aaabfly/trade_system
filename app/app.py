from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from testmodels.database import db_session_pu, db_session_pr, purchase_engine, product_engine

import os

from testmodels.models import OrderContent, InsertOrder, ProductDetail, InsertProduct

app = Flask(__name__)
app.secret_key = os.urandom(24)

SQLALCHEMY_DATABASE_BIND = {'purchaseorderdb': purchase_engine,
                            'productdetaildb': product_engine}




@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    form_i = InsertOrder()
    if request.method == 'POST':
        contentorder = OrderContent(orderdate=form_i.orderdate.data, expirationdate=form_i.expirationdate.data,
                                deliverydate=form_i.deliverydate.data, customerid=form_i.customerid.data,
                                customername=form_i.customername.data, orderfrom=form_i.orderfrom.data,
                                orderto=form_i.orderto.data, insurance=form_i.insurance.data,
                                remarks1=form_i.remarks1.data, remarks2=form_i.remarks2.data,
                                incoterms=form_i.incoterms.data, signedorder=form_i.signedorder.data,
                                remarks=form_i.remarks.data, expenseitem=form_i.expenseitem.data,
                                expensecost=form_i.expensecost.data)
        db_session_pu.add(contentorder)
        db_session_pu.commit()
        all_purchaseorder = OrderContent.query.all()
        return render_template('index.html', form_i=form_i, all_purchaseorder=all_purchaseorder)
        #return redirect(url_for('checkpurchaseorder'))
    else :
        return render_template('index.html', form_i=form_i)

@app.route('/checkpurchaseorder', methods=['GET'])
def checkpurchaseorder():
    all_purchaseorder = OrderContent.query.all()
    return render_template('checkpurchaseorder.html', all_purchaseorder=all_purchaseorder)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/new', methods=['GET'])
def new():
    return render_template('new.html')

if __name__ == "__main__":
    app.run(debug=True)
