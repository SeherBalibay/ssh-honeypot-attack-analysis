# Design and Implementation of an SSH Honeypot for Attack Analysis

## Overview

This project presents the design and implementation of a medium-interaction SSH honeypot developed for cybersecurity research, attack monitoring, and behavioral analysis. The system simulates an SSH service, records attacker activities, and provides a web-based dashboard for attack visualization and analysis.

The proposed platform captures authentication attempts, monitors post-authentication attacker behavior, identifies attack origins using GeoIP technologies, and stores collected information in a SQLite database. The recorded data are presented through an interactive Flask-based dashboard to support threat intelligence and cybersecurity education.

---

## Research Objectives

The main objectives of this project are:

* To design and implement a medium-interaction SSH honeypot.
* To monitor SSH-based attack attempts.
* To collect attacker usernames and passwords.
* To analyze post-authentication attacker behavior.
* To identify attack origins using GeoIP technologies.
* To visualize collected threat intelligence through a web dashboard.
* To support cybersecurity education and attack analysis activities.

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
design-and-implementation-of-an-ssh-honeypot-for-attack-analysis
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
