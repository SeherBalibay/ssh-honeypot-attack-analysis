# SSH Honeypot Attack Analysis

## Overview

SSH Honeypot Attack Analysis is a medium-interaction SSH honeypot designed for cybersecurity research, attack monitoring, and threat intelligence collection. The system simulates an SSH service, records attacker activities, and provides a web-based dashboard for attack visualization and analysis.

The project focuses on collecting authentication attempts, analyzing attacker behavior, identifying attack origins, and presenting collected information through an interactive dashboard.

---

## Research Objectives

The main objectives of this project are:

* To monitor SSH-based attack attempts.
* To collect attacker usernames and passwords.
* To analyze post-authentication attacker behavior.
* To identify attack origins using GeoIP technologies.
* To visualize collected threat intelligence through a web dashboard.
* To demonstrate the practical use of medium-interaction honeypots in cybersecurity.

---

## Features

* SSH Honeypot Service
* Username and Password Logging
* SQLite Database Storage
* GeoIP-Based Country Detection
* Interactive Flask Dashboard
* Command Execution Logging
* Medium-Interaction Fake Shell
* Top Commands Analytics
* Top Countries Analytics
* World Map Visualization
* Docker Deployment Support

---

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

---

## Technologies Used

* Python
* Flask
* SQLite
* Plotly
* Pandas
* Requests
* GeoIP2
* Docker

---

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

Open the dashboard:

```text
http://127.0.0.1:5000
```

---

## Dashboard Capabilities

The dashboard provides:

* Recent attack logs
* Top usernames
* Top passwords
* Top countries
* Most frequently executed commands
* GeoIP-based attack visualization
* World attack map

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### World Attack Map

![World Map](screenshots/world-map.png)

### Fake Shell

![Fake Shell](screenshots/fake-shell.png)

### Command Logging

![Command Logging](screenshots/command-logging.png)

---

## Educational Purpose

This project was developed for academic and cybersecurity research purposes. The collected data is intended for attack analysis, security awareness, and threat intelligence studies in controlled environments.

---

## Future Improvements

* Real SSH Protocol Emulation
* Dockerized Deployment
* High-Interaction Honeypot Environment
* Threat Intelligence Integration
* Automated Reporting System
* Real-Time Alert Mechanisms

---

## Literature Review

The theoretical background of this project is documented in:

```text
research/literature-review.md
```

The literature review covers honeypot technologies, SSH attack analysis, threat intelligence concepts, and related academic studies.

---

## Author

Seher Balibay

---

## License

MIT License
