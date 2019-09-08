from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from testmodels.database import db_session
import os

from testmodels.models import OrderContent, Insert

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    form_i = Insert()
    if form_i.validate_on_submit():
        contentorder = OrderContent(orderdate=form_i.orderdate.data, expirationdate=form_i.expirationdate.data,
                                deliverydate=form_i.deliverydate.data, customerid=form_i.customerid.data,
                                customername=form_i.customername.data, orderfrom=form_i.orderfrom.data,
                                orderto=form_i.orderto.data, insurance=form_i.insurance.data,
                                remarks1=form_i.remarks1.data, remarks2=form_i.remarks2.data,
                                incoterms=form_i.incoterms.data, signedorder=form_i.signedorder.data,
                                remarks=form_i.remarks.data, expenseitem=form_i.expenseitem.data,
                                expensecost=form_i.expensecost.data)
        db_session.add(contentorder)
        db_session.commit()
        all_purchaseorder = OrderContent.query.all()
        return redirect(url_for('checkpurchaseorder'))


    return render_template('index.html', form_i=form_i)

@app.route('/checkpurchaseorder', methods=['GET'])
def checkpurchaseorder():
    all_purchaseorder = OrderContent.query.all()
    return render_template('checkpurchaseorder.html', all_purchaseorder=all_purchaseorder)

if __name__ == "__main__":
    app.run(debug=True)
