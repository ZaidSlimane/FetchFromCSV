from flask import Flask, render_template, request, send_file
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def process_store_data(store_data, target_year):
    fetched_data = {}
    for month_year, earnings in store_data.items():
        if month_year.startswith(target_year):
            month = datetime.strptime(month_year, '%Y-%m').strftime('%B')
            fetched_data[month] = earnings
    return fetched_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    target_year = request.form['target_year']
    store = request.form['store']

    csv_path = 'Walmart_sales.csv'  # Replace with your actual CSV path

    stores_data = {}  # Dictionary to store earnings by month and store

    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            store_name = row['Store']
            date = datetime.strptime(row['Date'], '%d-%m-%Y')  # Assuming Date format
            month_year = date.strftime('%Y-%m')
            weekly_sales = float(row['Weekly_Sales'])

            # Check if store exists, initialize with empty dictionary if not
            if store_name not in stores_data:
                stores_data[store_name] = {}

            # Check if monthly earnings dictionary exists for the month, initialize if not
            if month_year not in stores_data[store_name]:
                stores_data[store_name][month_year] = 0

            # Add weekly sales to the corresponding store's monthly earnings
            stores_data[store_name][month_year] += weekly_sales

    fetched_data = process_store_data(stores_data.get(store, {}), target_year)

    # Plotting the graph
    plt.bar(fetched_data.keys(), fetched_data.values())
    plt.xlabel('Month')
    plt.ylabel('Earnings')
    plt.title('Earnings by Month for Target Year')
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close()

    # Returning the image file
    return send_file(image_stream, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
