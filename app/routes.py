from flask import Blueprint, render_template
from datetime import datetime
from .data_fetcher import load_stock_data, load_global_development_data, fetch_nasa_api_data, fetch_alpha_vantage_data


bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    #return render_template('dashboard.html')
    # Toggle between data sources by changing this variable
    data_source = "nasa_api"  # Options: "stock_file", "global_dev_file", "nasa_api", "alpha_api"

    data_source = "global_dev_file"  # Options: "stock_file", "global_dev_file", "nasa_api", "alpha_api"

    if data_source == "stock_file":
        data = load_stock_data()
    elif data_source == "global_dev_file":
        data = load_global_development_data()
    elif data_source == "nasa_api":
        data = fetch_nasa_api_data()
    elif data_source == "alpha_api":
        data = fetch_alpha_vantage_data()
    else:
        data = None

    if data is not None:
        data_preview = data.head(20).to_html()
    else:
        data_preview = "<p>Error loading data.</p>"

    return render_template('dashboard.html', year=datetime.now().year, data_preview=data_preview)