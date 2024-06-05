import os
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
app_version = "1.0.0"

# Database connection parameters from environment variables

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Log the environment variables for debugging

print(f"DB_NAME: {DB_NAME}")
print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {DB_PASSWORD}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_PORT: {DB_PORT}")

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database using environment variables.
    Returns:
        conn: A psycopg2 connection object.
    Raises:
        Exception: If there is an error connecting to the database.
    """
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise

def create_table():
    """
    Create the 'visitors' table if it does not exist.
    The table stores the IP addresses of visitors.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS visitors (
        ip_address VARCHAR(50) PRIMARY KEY
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def main_page():
    """
    Main page route that displays the count of unique visitors.
    Returns:
        str: HTML string displaying the unique visitors count.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM visitors")
        unique_visitors = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f"<h1>Unique Visitors: {unique_visitors}</h1>"
    except Exception as e:
        return f"Error: {e}"

@app.route('/version')
def version():
    """
    Version route that returns the current version of the application.
    Returns:
        json: JSON object containing the application version.
    """
    return jsonify(version=app_version)

@app.before_request
def track_visitor():
    """
    Track each visitor's IP address before handling the request.
    The IP address is either obtained from query parameters or from the request remote address.
    """
    ip_address = request.args.get('ip', request.remote_addr)
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            sql.SQL("INSERT INTO visitors (ip_address) VALUES (%s) ON CONFLICT (ip_address) DO NOTHING"),
            [ip_address]
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error tracking visitor: {e}")

if __name__ == '__main__':
    try:
        create_table()  # Ensure the visitors table is created before starting the app
        app.run(host='0.0.0.0', port=5000)  # Run the app on all available IP addresses, port 5000
    except Exception as e:
        print(f"Failed to start application: {e}")
