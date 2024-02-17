# Walmart Sales Visualization

This project enables users to visualize Walmart sales data by selecting a target year and store ID.

## Prerequisites

- Python 3 installed on your system
- Walmart sales data CSV file (provided or replace with your own dataset)

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd walmart-sales-visualization
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have your Walmart sales data CSV file named `Walmart_sales.csv` in the project directory. If your CSV file has a different name or location, update the `csv_path` variable in `app.py` accordingly.

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://localhost:5000` to access the visualization form.

4. Select the target year from the dropdown menu and choose the store ID from the scrollable dropdown menu.

5. Click on the "Generate Visualization" button to view the sales visualization for the selected year and store.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.


