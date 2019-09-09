from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, Date, create_engine

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, IntegerField
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
    insurance = Column(Text)
    ramarks1 = Column(Text)
    ramarks2 = Column(Text)
    incoterms = Column(Text)
    # currency = db.Column() #
    # payment terms #
    signedorder = Column(String)
    remarks = Column(Text)
    expenseitem = Column(String)
    expensecost = Column(Integer)

    def __init__(self, orderdate=None, expirationdate=None, deliverydate=None,
                 customerid=None, customername=None, orderfrom=None, orderto=None,
                 ordervia=None, insurance=None, remarks1=None, remarks2=None,
                 incoterms=None, signedorder=None, remarks=None, expenseitem=None,
                 expensecost=None ):
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

    # total amount #
    def __repr__(self):
        return '<PurchaseOrder %r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r>' % (self.id, self.orderdate, self.expirationdate, self.deliverydate, self.customerid, self.customername, self.orderfrom, self.orderto, self.ordervia, self.insurance, self.remarks1, self.remarks2, self.incoterms, self.signedorder, self.remarks, self.expenseitem, self.expensecost)


class Insert(FlaskForm):
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
    incoterms = TextAreaField('incoterms')
    signedorder = StringField('signedorder', validators=[DataRequired()])
    remarks = TextAreaField('remarks')
    expenseitem = StringField('expenseitem', validators=[DataRequired()])
    expensecost = IntegerField('expensecost', validators=[DataRequired()])

    submit = SubmitField('追加')

def init_db():
    from testmodels.database import engine, Base
    Base.metadata.create_all(bind=engine)

