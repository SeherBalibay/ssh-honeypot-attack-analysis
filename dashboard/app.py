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
        SELECT timestamp, ip_address, username, password, country
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

    cursor.execute("""
        SELECT country, COUNT(*)
        FROM attacks
        GROUP BY country
        ORDER BY COUNT(*) DESC
        LIMIT 5
    """)
    top_countries = cursor.fetchall()

    cursor.execute("""
        SELECT command, COUNT(*)
        FROM commands
        GROUP BY command
        ORDER BY COUNT(*) DESC
        LIMIT 10
    """)
    top_commands = cursor.fetchall()

    connection.close()

    return render_template(
        "index.html",
        total_attacks=total_attacks,
        attacks=attacks,
        top_usernames=top_usernames,
        top_passwords=top_passwords,
        top_countries=top_countries,
        top_commands=top_commands
    )


if __name__ == "__main__":
    app.run(debug=True)