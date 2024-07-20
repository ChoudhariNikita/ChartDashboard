from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_mysql_connection():
    return mysql.connector.connect(
        user='root',
        password='adminroot@123',
        host='localhost',
        port=3306,
        database='dashboard_db'
    )

def fetch_data(query, params=None):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute(query, params or ())
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

@app.route('/')
@app.route('/dashboard')
def dashboard():
    end_years = fetch_data("SELECT DISTINCT end_year FROM energy_outlook")
    topics = fetch_data("SELECT DISTINCT topic FROM energy_outlook")
    sectors = fetch_data("SELECT DISTINCT sector FROM energy_outlook")
    regions = fetch_data("SELECT DISTINCT region FROM energy_outlook")
    countries = fetch_data("SELECT DISTINCT country FROM energy_outlook")

    return render_template('dashboard.html', 
                           end_years=[row[0] for row in end_years],
                           topics=[row[0] for row in topics],
                           sectors=[row[0] for row in sectors],
                           regions=[row[0] for row in regions],
                           countries=[row[0] for row in countries])

@app.route('/fetch_data')
def fetch_data_route():
    try:
        selected_end_year = request.args.get('end_year')
        selected_topic = request.args.get('topic')
        selected_sector = request.args.get('sector')
        selected_region = request.args.get('region')
        selected_country = request.args.get('country')

        query = """
        SELECT 
            intensity, 
            likelihood, 
            relevance, 
            (end_year - start_year) AS year,
            country, 
            region 
        FROM energy_outlook 
        WHERE 1=1
        """
        params = []

        if selected_end_year:
            query += " AND end_year = %s"
            params.append(selected_end_year)
        if selected_topic:
            query += " AND topic = %s"
            params.append(selected_topic)
        if selected_sector:
            query += " AND sector = %s"
            params.append(selected_sector)
        if selected_region:
            query += " AND region = %s"
            params.append(selected_region)
        if selected_country:
            query += " AND country = %s"
            params.append(selected_country)

        result = fetch_data(query, params)

        intensity_data = [{"category": "Intensity", "value": row[0]} for row in result if row[0] is not None]
        likelihood_data = [{"category": "Likelihood", "value": row[1]} for row in result if row[1] is not None]
        relevance_data = [{"category": "Relevance", "value": row[2]} for row in result if row[2] is not None]
        year_data = [{"category": "Year", "value": row[3]} for row in result if row[3] is not None]
        country_data = [{"category": "Country", "value": row[4]} for row in result if row[4] is not None]
        region_data = [{"category": "Region", "value": row[5]} for row in result if row[5] is not None]

        return jsonify({
            "intensity_data": intensity_data,
            "likelihood_data": likelihood_data,
            "relevance_data": relevance_data,
            "year_data": year_data,
            "country_data": country_data,
            "region_data": region_data
        })

    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        return jsonify({"error": "Failed to fetch data"}), 500


if __name__ == '__main__':
    load.py
    app.run(debug=True)
