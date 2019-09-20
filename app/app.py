from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from testmodels.database import db_session, engine
import os

from testmodels.models import OrderContent, InsertOrder
app = Flask(__name__)
app.secret_key = os.urandom(24)




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
                                expensecost=form_i.expensecost.data, itemnumber1=form_i.itemnumber1.data,
                                productname1=form_i.productname1.data, unitprice1=form_i.unitprice1.data,
                                quantity1=form_i.quantity1.data, novalue1=form_i.novalue1.data,
                                itemnumber2=form_i.itemnumber2.data, productname2=form_i.productname2.data,
                                unitprice2=form_i.unitprice2.data, quantity2=form_i.quantity2.data,
                                novalue2=form_i.novalue2.data, itemnumber3=form_i.itemnumber3.data,
                                productname3=form_i.productname3.data, unitprice3=form_i.unitprice3.data,
                                quantity3=form_i.quantity3.data, novalue3=form_i.novalue3.data,
                                itemnumber4=form_i.itemnumber4.data, productname4=form_i.productname4.data,
                                unitprice4=form_i.unitprice4.data, quantity4=form_i.quantity4.data,
                                novalue4=form_i.novalue4.data, itemnumber5=form_i.itemnumber5.data,
                                productname5=form_i.productname5.data, unitprice5=form_i.unitprice5.data,
                                quantity5=form_i.quantity5.data, novalue5=form_i.novalue5.data,
                                amount1=form_i.amount1.data, amount2=form_i.amount2.data,
                                amount3=form_i.anount3.data, amount4=form_i.amount3.data,
                                amount5=form_i.amount5.data, purchase_submit=form_i.purchase_submit.data)
        db_session.add(contentorder)
        db_session.commit()
    return render_template('index.html', form_i=form_i)
    #return redirect(url_for('checkpurchaseorder'))

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
