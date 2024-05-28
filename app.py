import os
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
app_version = "1.0.0"

# Database connection parameters from environment variables
DB_NAME = os.getenv('DB_NAME', 'exampledb')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def create_table():
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
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM visitors")
    unique_visitors = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"<h1>Unique Visitors: {unique_visitors}</h1>"

@app.route('/version')
def version():
    return jsonify(version=app_version)

@app.before_request
def track_visitor():
    ip_address = request.args.get('ip', request.remote_addr)
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            sql.SQL("INSERT INTO visitors (ip_address) VALUES (%s) ON CONFLICT (ip_address) DO NOTHING"),
            [ip_address]
        )
        conn.commit()
    except Exception as e:
        print(f"Error tracking visitor: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000)
