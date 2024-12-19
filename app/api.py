from flask import Flask, request, jsonify
from main import calculate_net, calculate_brutto  # Import function from main application.

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render a simple HTML form for calculating net or gross.
    """
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Gross-Net Calculator</title>
    </head>
    <body>
        <h1>Gross-Net Calculator</h1>
        <form action="/calculate_net" method="post">
        <label for="brutto">Gross Amount:</label>
        <input type="text" id="brutto" name="brutto" required><br>
        <label for="tax_rate_net">VAT Rate (%):</label>
        <input type="text" id="tax_rate_net" name="tax_rate" required><br>
        <button id="calculate_net" type="submit">Calculate</button>
    </form>
    <br>
    <form action="/calculate_gross" method="post">
        <label for="netto">Net Amount:</label>
        <input type="text" id="netto" name="netto" required><br>
        <label for="tax_rate_gross">VAT Rate (%):</label>
        <input type="text" id="tax_rate_gross" name="tax_rate" required><br>
        <button id="calculate_gross" type="submit">Calculate</button>
    </form>

    </body>
    </html>
    '''


@app.route('/calculate_net', methods=['POST'])
def calculate_net_api():
    """Endpoint API to count net from gross."""
    return process_calculation(request, calculate_net, "net", "Net amount")

@app.route('/calculate_gross', methods=['POST'])
def calculate_gross_api():
    """Endpoint API to count gross from net."""
    return process_calculation(request, calculate_brutto, "gross", "Gross amount")

def process_calculation(req, calculation_func, result_key, result_label):
    """Support for common functions for calculations."""
    if req.content_type == 'application/json':
        data = req.get_json()
        amount = data.get("netto" if result_key == "gross" else "brutto")
        tax_rate = data.get("tax_rate")
    elif req.content_type == 'application/x-www-form-urlencoded':
        amount = req.form.get("netto" if result_key == "gross" else "brutto")
        tax_rate = req.form.get("tax_rate")
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415

    if amount is None or tax_rate is None:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        amount = float(amount)
        tax_rate = float(tax_rate)
        if amount < 0 or tax_rate < 0:
            return jsonify({"error": "Negative values not allowed"}), 400

        result = calculation_func(amount, tax_rate)
        if req.content_type == 'application/x-www-form-urlencoded':
            return f"<h1>{result_label}: {result:.2f} zł</h1>", 200
        return jsonify({result_key: result}), 200
    except ValueError:
        return jsonify({"error": "Invalid input type"}), 400

if __name__ == "__main__":
    app.run(debug=True)
