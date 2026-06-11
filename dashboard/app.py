from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_PATH = "../database/attacks.db"


@app.route("/")
def dashboard():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM attacks")
    total_attacks = cursor.fetchone()[0]

    cursor.execute("""
        SELECT timestamp, ip_address, username, password
        FROM attacks
        ORDER BY id DESC
        LIMIT 10
    """)
    attacks = cursor.fetchall()

    cursor.execute("""
        SELECT username, COUNT(*)
        FROM attacks
        GROUP BY username
        ORDER BY COUNT(*) DESC
        LIMIT 5
    """)
    top_usernames = cursor.fetchall()

    cursor.execute("""
        SELECT password, COUNT(*)
        FROM attacks
        GROUP BY password
        ORDER BY COUNT(*) DESC
        LIMIT 5
    """)
    top_passwords = cursor.fetchall()

    connection.close()

    return render_template(
        "index.html",
        total_attacks=total_attacks,
        attacks=attacks,
        top_usernames=top_usernames,
        top_passwords=top_passwords
    )


if __name__ == "__main__":
    app.run(debug=True)