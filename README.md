# SSH Honeypot Attack Analysis

## Overview

SSH Honeypot Attack Analysis is a medium-interaction SSH honeypot developed to monitor, collect, and analyze malicious login attempts. The system records attacker credentials, command execution behavior, and attack origins while providing a web-based dashboard for visualization and analysis.

## Features

* SSH Honeypot Service
* Username and Password Logging
* SQLite Database Storage
* GeoIP-Based Country Detection
* Interactive Attack Dashboard
* Command Execution Logging
* Medium-Interaction Fake Shell
* Top Commands Analytics
* Top Countries Analytics
* World Map Visualization
* Docker Deployment Support

## Project Structure

```text
ssh-honeypot-attack-analysis
│
├── dashboard
├── database
├── demo
├── docker
├── docs
├── geoip
├── research
├── screenshots
├── src
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

## Technologies Used

* Python
* Flask
* SQLite
* Plotly
* Pandas
* Requests
* GeoIP2
* Docker

## Installation

Clone the repository:

```bash
git clone https://github.com/SeherBalibay/ssh-honeypot-attack-analysis.git
cd ssh-honeypot-attack-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the honeypot:

```bash
cd src
python honeypot.py
```

Run the dashboard:

```bash
cd dashboard
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Dashboard Capabilities

The dashboard provides:

* Recent attack logs
* Top usernames
* Top passwords
* Top countries
* Top executed commands
* GeoIP attack visualization
* World attack map

## Educational Purpose

This project was developed for academic and cybersecurity research purposes. It is intended for attack monitoring, security awareness, and threat intelligence studies.

## Future Improvements

* Real SSH Protocol Emulation
* Dockerized Deployment
* High-Interaction Honeypot Environment
* Threat Intelligence Integration
* Automated Reporting System

## Author

Seher Balibay

## License

MIT License
