# Literature Review

## 1. Introduction

Honeypots are security mechanisms designed to attract attackers and monitor malicious activities. Unlike traditional security systems, honeypots focus on collecting information about attacker behavior rather than blocking attacks. In recent years, SSH honeypots have become widely used because SSH services are frequently targeted by automated brute-force attacks.

---

## 2. Honeypot Technologies

According to Spitzner (2003), honeypots can be categorized into low-interaction, medium-interaction, and high-interaction systems.

* Low-interaction honeypots provide limited services and are easier to deploy.
* Medium-interaction honeypots simulate realistic services while maintaining security.
* High-interaction honeypots provide full operating system environments but require stronger isolation mechanisms.

The system developed in this project belongs to the medium-interaction category because it includes a fake shell environment and command logging functionality.

---

## 3. SSH Honeypots and Attack Analysis

Research conducted by The Honeynet Project demonstrates that SSH services are among the most frequently targeted network services. Attackers often use automated bots to perform brute-force login attempts using common usernames and passwords.

Studies show that collecting attacker credentials alone is insufficient. Post-authentication behavior, such as executed commands, provides valuable information about attacker objectives and tactics.

For this reason, modern SSH honeypots often include command monitoring and behavioral analysis modules.

---

## 4. Threat Intelligence and Data Visualization

Recent studies emphasize the importance of combining honeypots with visualization and analytics platforms.

By storing attack information in databases and presenting it through dashboards, security analysts can identify:

* Frequently targeted accounts
* Common passwords
* Geographic attack sources
* Attacker behavioral patterns

GeoIP technologies further improve analysis by mapping attack origins to specific countries and regions.

---

## 5. Relation to This Project

This project incorporates several concepts discussed in previous research:

* SSH attack monitoring
* Credential collection
* Command execution logging
* GeoIP-based country identification
* Dashboard-based attack visualization

Unlike a basic low-interaction honeypot, this project records attacker commands through a simulated Linux shell environment and provides a centralized dashboard for analysis.

---

## References

Spitzner, L. (2003). Honeypots: Tracking Hackers. Addison-Wesley.

Provos, N., & Holz, T. (2007). Virtual Honeypots: From Botnet Tracking to Intrusion Detection. Addison-Wesley.

The Honeynet Project. (2004). Know Your Enemy: Learning About Security Threats. Addison-Wesley.

Alata, E., Nicomette, V., Kaâniche, M., Dacier, M., & Herrb, M. (2006). Lessons learned from the deployment of a high-interaction honeypot. International Conference on Dependable Systems and Networks.

Pouget, F., Dacier, M., & Pham, V. H. (2005). Analysis of Honeypot Data and Attack Trends. International Information Security Conference.
