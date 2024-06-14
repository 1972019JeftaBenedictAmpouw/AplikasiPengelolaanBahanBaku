from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bahanbaku_kafe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '0'

db = SQLAlchemy(app)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200))
    ingredients = db.relationship('Ingredient', backref='supplier', lazy=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingredients')
def ingredient_list():
    ingredients = Ingredient.query.all()
    return render_template('ingredient.html', ingredients=ingredients)

@app.route('/ingredients/new', methods=['GET', 'POST'])
def new_ingredient():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        supplier_id = request.form['supplier_id']
        new_ingredient = Ingredient(name=name, quantity=quantity, unit=unit, supplier_id=supplier_id)
        db.session.add(new_ingredient)
        db.session.commit()
        flash('Bahan baku berhasil ditambahkan')
        return redirect(url_for('ingredient_list'))
    return render_template('new_ingredient.html')

@app.route('/suppliers')
def supplier_list():
    suppliers = Supplier.query.all()
    return render_template('supplier.html', suppliers=suppliers)

@app.route('/suppliers/new', methods=['GET', 'POST'])
def new_supplier():
    if request.method == 'POST':
        name = request.form['name']
        contact_info = request.form['contact_info']
        new_supplier = Supplier(name=name, contact_info=contact_info)
        db.session.add(new_supplier)
        db.session.commit()
        flash('Pemasok berhasil ditambahkan')
        return redirect(url_for('supplier_list'))
    return render_template('new_supplier.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Membuat semua tabel di database sesuai model
    app.run(debug=True)
