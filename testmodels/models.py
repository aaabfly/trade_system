from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Column, Integer, String, Text, Date, ForeignKey, Boolean)
from sqlalchemy.orm import relationship

from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, BooleanField, TextAreaField,SelectField, IntegerField, SubmitField)
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

from testmodels.database import Base
import app.config

from datetime import datetime


class OrderContent(Base):
    __tablename__ = 'ordercontent'
    __bind_key__ = 'purchaseorderdb'
    id = Column(Integer, primary_key=True, unique=True)
    orderdate = Column(Date)
    expirationdate = Column(Date)
    deliverydate = Column(Date)
    customerid = Column(String)
    customername = Column(String)
    orderfrom = Column(String)
    orderto = Column(String)
    ordervia = Column(String)
    insurance = Column(Text)
    ramarks1 = Column(Text)
    ramarks2 = Column(Text)
    incoterms = Column(Text)
    currency = Column(String) #
    paymentterms = Column(String)
    signedorder = Column(String)
    remarks = Column(Text)
    expenseitem = Column(String)
    expensecost = Column(Integer)

    productdetails = relationship('ProductDetail')


    def __init__(self, orderdate=None, expirationdate=None, deliverydate=None,
                 customerid=None, customername=None, orderfrom=None, orderto=None,
                 ordervia=None, insurance=None, remarks1=None, remarks2=None,
                 incoterms=None, signedorder=None, remarks=None, expenseitem=None,
                 expensecost=None, currency=None, paymentterms=None ):
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
        self.currency = currency
        self.paymentterms = paymentterms
        self.signedorder = signedorder
        self.remarks = remarks
        self.expenseitem = expenseitem
        self.expensecost = expensecost

    # total amount #
    def __repr__(self):
        return '<PurchaseOrder %r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r>' % (self.id, self.orderdate, self.expirationdate, self.deliverydate, self.customerid, self.customername, self.orderfrom, self.orderto, self.ordervia, self.insurance, self.remarks1, self.remarks2, self.incoterms, self.signedorder, self.remarks, self.expenseitem, self.expensecost)


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
    insurance = TextAreaField('insurance', validators=[DataRequired()])
    remarks1 = TextAreaField('remarks1')
    remarks2 = TextAreaField('remarks2')
    currency = SelectField('currency',
                            validation=[DataRequired()],
                            choices=[(('ドル', 'ドル'), ('円', '円'),
                            ('ユーロ', 'ユーロ'))],
                            default='')
    paymentterms = SelectField(
                    'paymentterms',
                    validators=[DataRequired()],
                    choices=[(('', ''), ('EXW', 'EXW'), ('FCA', 'FCA'),
                            ('CPT', 'CPT'), ('CIP', 'CIP'), ('DAT', 'DAT'),
                            ('DAP', 'DAP'), ('DDP', 'DDP'), ('FAS', 'FAS'),
                            ('FOB', 'FOB'), ('CFR', 'CFR'), ('CIF', 'CIR'))],
                            default='' )

    signedorder = StringField('signedorder', validators=[DataRequired()])
    remarks = TextAreaField('remarks')
    expenseitem = StringField('expenseitem', validators=[DataRequired()])
    expensecost = IntegerField('expensecost', validators=[DataRequired()])

    submit = SubmitField('追加')

class ProductDetail(Base):
    __tablename__ = 'productdetail'
    __bind_key__ = 'productdetaildb'

    id = Column(Integer, primary_key=True)
    ordercontent_id = Column(Integer, ForeignKey('ordercontent.id'))

    item_no = Column(String)
    productname = Column(String)
    unitprice = Column(Integer)
    quantity = Column(Integer)
    amount = Column(Integer)
    valueflag = Column(Boolean)

    def __init__(self, item_no=None, productname=None,unitprice=None, quantity=None,
                 amount=None, valueflag=False):
        self.item_no = item_no
        self.productname = productname
        self.unitprice = unitprice
        self.quantity = quantity
        self.amount = amount
        self.valueflag = valueflag

    def __repr__(self):
        return '<ProductDetail %r,%r,%r,%r,%r,%r,>' % (self.item_no, self.productname,
                    self.unitprice, self.quantity, self.amount, self.valueflag)

class InsertProduct(FlaskForm):
    item_no = StringField('item_no', validators=[DataRequired()])
    productname = StringField('productname', validators=[DataRequired()])
    unitprice = IntegerField('unitprice', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])
    amount = IntegerField('amount', validators=[DataRequired()])
    valueflag = BooleanField('valueflag')

    def __init__(self, amount=None ,valueflag=False,):
        self.amount = amount
        self.valueflag = valueflag


def init_db():
    from testmodels.database import engine, Base
    Base.metadata.create_all(bind=engine, checkfirst=False)

