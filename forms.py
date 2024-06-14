from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class IngredientForm(FlaskForm):
    name = StringField('Nama Bahan Baku', validators=[DataRequired()])
    quantity = IntegerField('Kuantitas', validators=[DataRequired()])
    unit = StringField('Satuan', validators=[DataRequired()])
    supplier_id = IntegerField('ID Pemasok', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SupplierForm(FlaskForm):
    name = StringField('Nama Pemasok', validators=[DataRequired()])
    contact_info = StringField('Informasi Kontak')
    submit = SubmitField('Submit')
