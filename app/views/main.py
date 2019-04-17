from flask import render_template, redirect, url_for, request
import json
from app import app

from app.forms import product
from app.models import Product



@app.route('/')
@app.route('/index')
def index():
    data = Product.query.all()
    app.logger.info("total record: %s"%(len(data)))
    return render_template('index.html', title='Home', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    form = product.ProductForm()
    if form.validate_on_submit():
        # set form data to model
        newProd  = Product()
        newProd.item = form.item.data
        newProd.price = form.price.data 
        newProd.qty = form.qty.data 

        # db transaction
        newProd.save()
        return redirect(url_for('index'))
        
    return render_template('form.html', form=form, title="Add Product")

@app.route('/show/<int:product_id>', methods=['GET'])
def show_product(product_id):
    showProd = Product.get_or_404(product_id)
    form = product.ProductForm()
    title = 'Show product %s'%(showProd.item)
    return render_template('show.html', title=title, form=form, item=showProd)


@app.route('/update/<int:prod_id>', methods=['GET', 'POST'])
def update_product(prod_id):
    form = product.ProductForm()
    if form.validate_on_submit():
        # db update 
        getProd = Product.get(prod_id)
        if getProd :
            getProd.item = form.item.data.capitalize()
            getProd.price = form.price.data
            getProd.qty = form.qty.data
            getProd.update()
    return redirect(url_for('index'))
