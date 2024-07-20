# Admin Dashboard Project

## Description

This is a simple admin dashboard that fetches data from a MySQL database and visualizes it in the form of charts. For chart visualization, we have used the Google Charts API.

## Steps to Run This Flask App

### 1. Clone This Repository

```sh
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Required Dependencies

```sh
pip install -r requirements.txt
```

### 3. Update MySQL Database Credentials

Open `app.py` and update the MySQL database credentials with your own:

```python
def get_mysql_connection():
    return mysql.connector.connect(
        user='your-username',
        password='your-password',
        host='your-host',
        port=your-port,
        database='your-database-name'
    )
```

### 4. Create Database and Table

Login to your MySQL server and create the required database and table using the following SQL query:

```sql
CREATE TABLE energy_outlook (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(500),
  sector VARCHAR(100),
  topic VARCHAR(100),
  insight VARCHAR(255),
  url VARCHAR(500),
  region VARCHAR(100),
  start_year VARCHAR(10),
  end_year VARCHAR(10),
  impact VARCHAR(100),
  added DATETIME,
  published DATETIME,
  country VARCHAR(100),
  relevance INT,
  pestle VARCHAR(100),
  source VARCHAR(255),
  likelihood INT,
  intensity INT,
  PRIMARY KEY (id)
);
```

### 5. Load Data Into the Database

Execute `load.py` to load JSON data into the database. Ensure `load.py` contains the necessary logic to insert data into the `energy_outlook` table.

```sh
python load.py
```

### 6. Run the Flask Application

Finally, run `app.py` to start the Flask application.

```sh
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/dashboard` to view the admin dashboard with data visualizations.

## Conclusion

With these steps, you should be able to set up and run the admin dashboard application on your local machine, visualizing data from your MySQL database using Google Charts. If you encounter any issues, feel free to seek further assistance.