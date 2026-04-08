from flask import Flask, render_template, request
import json
import csv
import sqlite3

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


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == "json":
        with open('products.json') as f:
            data = json.load(f)

    elif source == "csv":
        data = []
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)

    elif source == "sql":
        data = []
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()

            try:
                cursor.execute("SELECT id, name, category, price FROM Products")
            except:
                cursor.execute("SELECT id, name, category, price FROM products")

            rows = cursor.fetchall()

            for row in rows:
                data.append({
                    "id":row[0],
                    "name":row[1],
                    "category":row[2],
                    "price":row[3]
                })

            conn.close()
        except Exception:
            return render_template('product_display.html',error="Database error")

        else:
          return render_template('product_display.html',error="Wrong source")

    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        product_id = int(product_id)
        data = [p for p in data if p['id'] == product_id]

        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)