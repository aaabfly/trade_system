from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, create_engine, Boolean

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

from testmodels.database import Base

from datetime import datetime


class OrderContent(Base):
    __tablename__ = 'ordercontent'
    id = Column(Integer, primary_key=True)
    orderdate = Column(Date)
    expirationdate = Column(Date)
    deliverydate = Column(Date)
    customerid = Column(String)
    customername = Column(String)
    orderfrom = Column(String)
    orderto = Column(String)
    ordervia = Column(String)
    insurance = Column(String)
    ramarks1 = Column(String)
    ramarks2 = Column(String)
    incoterms = Column(String)
    # currency = db.Column() #
    # payment terms #
    signedorder = Column(String)
    remarks = Column(String)
    expenseitem = Column(String)
    expensecost = Column(Integer)

    #productdetail
    itemnumber1 = Column(String)
    productname1 = Column(String)
    unitprice1 = Column(Integer)
    quantity1 = Column(Integer)
    amount1 = Column(Integer)
    novalue1 = Column(Boolean)
    itemnumber2 = Column(String)
    productname2 = Column(String)
    unitprice2 = Column(Integer)
    quantity2 = Column(Integer)
    amount2 = Column(Integer)
    novalue2 = Column(Boolean)
    itemnumber3 = Column(String)
    productname3 = Column(String)
    unitprice3 = Column(Integer)
    quantity3 = Column(Integer)
    amount3 = Column(Integer)
    novalue3 = Column(Boolean)
    itemnumber4 = Column(String)
    productname4 = Column(String)
    unitprice4 = Column(Integer)
    quantity4 = Column(Integer)
    amount4 = Column(Integer)
    novalue4 = Column(Boolean)
    itemnumber5 = Column(String)
    productname5 = Column(String)
    unitprice5 = Column(Integer)
    quantity5 = Column(Integer)
    amount5 = Column(Integer)
    novalue5 = Column(Boolean)

    def __init__(self, orderdate=None, expirationdate=None, deliverydate=None,
                 customerid=None, customername=None, orderfrom=None, orderto=None,
                 ordervia=None, insurance=None, remarks1=None, remarks2=None,
                 incoterms=None, signedorder=None, remarks=None, expenseitem=None,
                 expensecost=None, itemnumber1=None, productname1=None, unitprice1=None,
                 quantity1=None, amount1=None, novalue1=None, itemnumber2=None,
                 productname2=None, unitprice2=None, quantity2=None, amount2=None,
                 novalue2=None, itemnumber3=None, productname3=None, unitprice3=None,
                 quantity3=None, amount3=None, novalue3=None, itemnumber4=None,
                 productname4=None, unitprice4=None, quantity4=None, amount4=None,
                 itemnumber5=None, productname5=None, unitprice5=None, quantity5=None,
                 amount5=None, novalue4=None, novalue5=None):
        self.orderdate = orderdate
        self.expirationdate = expirationdate
        self.deliverydate = deliverydate
        self.customerid = customerid
        self.customername = customername
        self.orderfrom = orderfrom
        self.orderto = orderto
        self.ordervia = ordervia
        self.insurance = insurance
        self.remarks1 = remarks1
        self.remarks2 = remarks2
        self.incoterms = incoterms
        self.signedorder = signedorder
        self.remarks = remarks
        self.expenseitem = expenseitem
        self.expensecost = expensecost
        self.itemnumber1 = itemnumber1
        self.productname1 = productname1
        self.unitprice1 = unitprice1
        self.quantity1 = quantity1
        self.amount1 = amount1
        self.novalue1 = novalue1
        self.itemnumber2 = itemnumber2
        self.productname2 = productname2
        self.unitprice2 = unitprice2
        self.quantity2 = quantity2
        self.amount2 = amount2
        self.itemnumber3 = itemnumber3
        self.productname3 = productname3
        self.unitprice3 = unitprice3
        self.quantity3 = quantity3
        self.amount3 = amount3
        self.itemnumber4 = itemnumber4
        self.productname4 = productname4
        self.unitprice4 = unitprice4
        self.quantity4 = quantity4
        self.amount4 = amount4
        self.novalue4 = novalue4
        self.itemnumber5 = itemnumber5
        self.productname5 = productname5
        self.unitprice5 = unitprice5
        self.quantity5 = quantity5
        self.amount5 = amount5
        self.novalue5 = novalue5

    # total amount #
    def __repr__(self):
        return '<PurchaseOrder %r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r, >' % (self.id,
                self.orderdate, self.expirationdate, self.deliverydate, self.customerid,
                self.customername, self.orderfrom, self.orderto, self.ordervia, self.insurance,
                self.remarks1, self.remarks2, self.incoterms, self.signedorder, self.remarks,
                self.expenseitem, self.expensecost, self.itemnumber1, self.productname1,
                self.unitprice1, self.quantity1, self.amount1, self.novalue1, self.itemnumber2,
                self.productname2, self.unitprice2, self.quantity2, self.amount2, self.novalue2,
                self.itemnumber3, self.productname3, self.unitprice3, self.quantity3, self.amount3,
                self.novalue3, self.itemnumber4, self.productname4, self.unitprice4, self.quantity4,
                self.amount4, self.novalue4, self.itemnumber5, self.productname5, self.unitprice5,
                self.quantity5, self.amount5, self.novalue5)


class InsertOrder(FlaskForm):
    orderdate = DateField('orderdate', validators=[DataRequired()],
                          format='%Y-%m-%d')
    expirationdate = DateField('expirationdate', validators=[DataRequired()],
                               format='%Y-%m-%d')
    deliverydate = DateField('deliverydate', validators=[DataRequired()],
                             format='%Y-%m-%d')
    customerid = StringField('customerid', validators=[DataRequired()])
    customername = StringField('customername', validators=[DataRequired()])
    orderfrom = StringField('orderfrom', validators=[DataRequired()])
    orderto = StringField('orderto', validators=[DataRequired()])
    ordervia = StringField('ordervia', validators=[DataRequired()])
    insurance = StringField('insurance', validators=[DataRequired()])
    remarks1 = StringField('remarks1')
    remarks2 = StringField('remarks2')
    incoterms = StringField('incoterms')
    signedorder = StringField('signedorder', validators=[DataRequired()])
    remarks = StringField('remarks')
    expenseitem = StringField('expenseitem')
    expensecost = IntegerField('expensecost')

    purchase_submit = SubmitField('追加')

    itemnumber1 = StringField('itemnumber1')
    productname1 = StringField('productname1')
    unitprice1 = IntegerField('unitprice1')
    quantity1 = IntegerField('quantity1')
    amount1 = IntegerField('amount1')
    novalue1 = BooleanField('novalue1')
    itemnumber2 = StringField('itemnumber2')
    productname2 = StringField('productname2')
    unitprice2 = IntegerField('unitprice2')
    quantity2 = IntegerField('quantity2')
    amount2 = IntegerField('amount2')
    novalue2 = BooleanField('novalue2')
    itemnumber3 = StringField('itemnumber3')
    productname3 = StringField('productname3')
    unitprice3 = IntegerField('unitprice3')
    quantity3 = IntegerField('quantity3')
    amount3 = IntegerField('amount3')
    novalue3 = BooleanField('novalue3')
    itemnumber4 = StringField('itemnumber4')
    productname4 = StringField('productname4')
    unitprice4 = IntegerField('unitprice4')
    quantity4 = IntegerField('quantity4')
    amount4 = IntegerField('amount4')
    novalue4 = BooleanField('novalue4')
    itemnumber5 = StringField('itemnumber5')
    productname5 = StringField('productname5')
    unitprice5 = IntegerField('unitprice5')
    quantity5 = IntegerField('quantity5')
    amount5 = IntegerField('amount5')
    novalue5 = BooleanField('novalue5')


