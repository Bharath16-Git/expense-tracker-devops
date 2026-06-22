from flask import Flask, request
import psycopg2

app = Flask(__name__)

expense_list = []

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="expenses_db",
        user="admin",
        password="admin123",
        port="5432"
    )
    return conn

@app.route('/')
def home():
    return {
        "message": "Welcome to Expense Tracker API"
    }

@app.route('/health')
def health():
    return {
        "status": "healthy"
    }

@app.route('/expenses')
def get_expenses():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT title, amount, category FROM expenses")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    expenses = []

    for row in rows:
        expenses.append({
            "title": row[0],
            "amount": float(row[1]),
            "category": row[2]
        })

    return {
        "expenses": expenses
    }

@app.route('/expense', methods=['POST'])
def add_expense():
    expense = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses (title, amount, category) VALUES (%s, %s, %s)",
        (expense["title"], expense["amount"], expense["category"])
    )

    conn.commit()

    cur.close()
    conn.close()

    return {
        "message": "Expense added successfully",
        "expense": expense
    }, 201

@app.route('/summary')
def summary():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT COALESCE(SUM(amount),0), COUNT(*) FROM expenses")
    result = cur.fetchone()

    cur.close()
    conn.close()

    return {
        "total_expenses": float(result[0]),
        "total_items": result[1]
    }

@app.route('/insight')
def insight():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
        LIMIT 1
    """)

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result is None:
        return {
            "insight": "No expenses added yet"
        }

    return {
        "insight": f"You spent the most on {result[0]}"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)