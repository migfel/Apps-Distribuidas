from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process_sale', methods=['POST'])
def process_sale():
    quantity = int(request.form['quantity'])
    product_name = request.form['product_name']
    price = float(request.form['price'])

    total_amount = quantity * price

    # Puedes hacer más cosas aquí, como generar la factura, etc.

    return render_template('invoice.html', quantity=quantity, product_name=product_name, price=price, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
