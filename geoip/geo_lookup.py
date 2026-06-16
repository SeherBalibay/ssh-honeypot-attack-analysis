import requests


def get_country(ip_address):

    if ip_address == "127.0.0.1":
        return "Localhost"

    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip_address}",
            timeout=5
        )

        data = response.json()

        return data.get("country", "Unknown")

    except:
        return "Unknown"