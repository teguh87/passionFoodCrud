from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import InputRequired

class ProductForm(FlaskForm):
    item    = StringField('item', [InputRequired()])
    qty     = IntegerField('quantity')
    price   = IntegerField('price')