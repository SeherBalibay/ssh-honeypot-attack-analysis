from flask import Flask, render_template
import sqlite3
import plotly.express as px
import pandas as pd

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
        WHERE country IS NOT NULL
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

    cursor.execute("""
        SELECT country, COUNT(*)
        FROM attacks
        WHERE country IS NOT NULL
          AND country != 'Localhost'
          AND country != 'None'
          AND country != ''
        GROUP BY country
    """)
    country_data = cursor.fetchall()

    connection.close()

    map_html = """
    <div style="color:#94a3b8; text-align:center; padding:80px;">
        No public country data available yet.
    </div>
    """

    if country_data:
        df = pd.DataFrame(country_data, columns=["country", "count"])

        country_iso = {
            "Turkey": "TUR",
            "Russia": "RUS",
            "China": "CHN",
            "United States": "USA",
            "Germany": "DEU",
            "France": "FRA",
            "Brazil": "BRA",
            "United Kingdom": "GBR",
            "Netherlands": "NLD",
            "India": "IND",
            "Japan": "JPN",
            "Canada": "CAN",
            "Italy": "ITA",
            "Spain": "ESP"
        }

        df["iso"] = df["country"].map(country_iso)
        df = df.dropna(subset=["iso"])

        if not df.empty:
            fig = px.choropleth(
                df,
                locations="iso",
                color="count",
                hover_name="country",
                hover_data={"count": True, "iso": False},
                color_continuous_scale="Reds",
                title="Global SSH Attack Distribution"
            )

            fig.update_geos(
                projection_type="natural earth",
                showframe=False,
                showcoastlines=True,
                coastlinecolor="#94a3b8",
                showland=True,
                landcolor="#1e293b",
                showocean=True,
                oceancolor="#020617",
                showlakes=True,
                lakecolor="#020617",
                showcountries=True,
                countrycolor="#94a3b8",
                bgcolor="#020617"
            )

            fig.update_layout(
                paper_bgcolor="#020617",
                plot_bgcolor="#020617",
                font=dict(color="#e5e7eb"),
                title=dict(
                    text="Global SSH Attack Distribution",
                    x=0.5,
                    font=dict(size=22, color="#ffffff")
                ),
                margin=dict(l=0, r=0, t=55, b=0),
                height=520,
                coloraxis_colorbar=dict(
                    title="Attacks",
                    tickcolor="#e5e7eb",
                    tickfont=dict(color="#e5e7eb"),
                    titlefont=dict(color="#e5e7eb")
                )
            )

            map_html = fig.to_html(
                full_html=False,
                include_plotlyjs="cdn",
                config={
                    "displayModeBar": False,
                    "responsive": True
                }
            )

    return render_template(
        "index.html",
        total_attacks=total_attacks,
        attacks=attacks,
        top_usernames=top_usernames,
        top_passwords=top_passwords,
        top_countries=top_countries,
        top_commands=top_commands,
        map_html=map_html
    )


if __name__ == "__main__":
    app.run(debug=True)