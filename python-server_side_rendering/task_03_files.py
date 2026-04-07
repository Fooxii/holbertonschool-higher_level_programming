from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception:
        items_list = []

    return render_template('items.html', items=items_list)


# ✅ NEW ROUTE (this is the task)
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 🔹 Read JSON
    if source == "json":
        with open('products.json') as f:
            data = json.load(f)

    # 🔹 Read CSV
    elif source == "csv":
        data = []
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)

    # 🔹 Wrong source
    else:
        return render_template('product_display.html', error="Wrong source")

    # 🔹 Filter by ID
    if product_id:
        product_id = int(product_id)
        data = [p for p in data if p['id'] == product_id]

        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)