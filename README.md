# Implementation and Analysis on Cowrie Honeypot

## Project Overview
This project focuses on deploying the Cowrie honeypot to study and mitigate SSH and Telnet brute-force attacks. Cowrie, a medium-interaction honeypot, simulates SSH services to attract attackers, logs their interactions, and provides insights into their behaviors and tactics. The project also includes testing the honeypot using various tools and analyzing the collected data.

## Objectives
- Review existing research and honeypot solutions.
- Set up and configure Cowrie honeypot on Ubuntu Server.
- Simulate brute-force attacks using tools like Medusa and Metasploit.
- Analyze attacker behaviors, techniques, and tactics.
- Provide recommendations for proactive defense measures.

## Project Highlights
### Features of Cowrie Honeypot
- Simulates SSH and Telnet services to attract attackers.
- Logs attacker interactions, including login attempts, executed commands, and file transfers.
- Provides JSON-formatted logs for detailed analysis.
- Supports integration with tools like ELK Stack for enhanced visualization.

### Tools and Technologies Used
#### Hardware
- **Lenovo T460s Laptop**: Used for hosting virtual environments.
- **VirtualBox**: Virtualization platform for running isolated Ubuntu Server and Kali Linux environments.

#### Software
- **Ubuntu Server 22.04 LTS**: Hosting platform for Cowrie honeypot.
- **Kali Linux 2024**: Used for penetration testing and launching attacks.
- **Putty**: Terminal emulator for testing SSH access.
- **Nmap**: Network scanning tool to detect open ports and services.
- **Medusa and Metasploit**: Brute-forcing tools for simulating attacks.

### Methodology
1. **Setup and Configuration**
   - Installed Cowrie honeypot on Ubuntu Server.
   - Redirected SSH connections to Cowrie using `iptables`.
   - Configured logging and file paths for capturing activity.

2. **System Testing**
   - Nmap: Nmap is one of the tools that can be used in port scanning. nmap was use to run a port scan on the system, I used following command to scan the system on kali-linux “nmap ip-addr"
![Nmap Scan](./nmap.png "Nmap scan for open ports")

 Medusa, Metasploit, and Putty.
   - Captured logs for each scenario to analyze attacker behaviors.

3. **Data Collection and Analysis**
   - Developed a Python-based parsing tool to process Cowrie logs.
   - Analyzed log data to identify successful and failed login attempts and attacker tactics.
   - Tools like Medusa and Metasploit demonstrated the ability to compromise weak SSH credentials.
   - Comprehensive logging provided valuable insights into attacker behaviors.

### Challenges
- Difficulty setting up Ubuntu Server and GUI.
- Challenges in developing log analysis tools.

## Recommendations
- Enhance Cowrie with cryptographic measures for added security.
- Strengthen authentication using multi-factor authentication (MFA).
- Regularly update system software and enforce strong password policies.
- Integrate advanced log visualization tools like ELK Stack for deeper insights.

## Future Work
- Deploy the honeypot in external network environments to gather more diverse data.
- Expand the scope to include additional attack vectors and protocols.
- Develop automated alert systems based on honeypot logs.

## Directory Structure
```
├── src
│   ├── cowrie_config.cfg   # Configuration file for Cowrie
│   ├── parse_logs.py       # Python script for log parsing
├── logs
│   ├── cowrie.log          # Raw logs from Cowrie
│   ├── parsed_logs.json    # Parsed logs in JSON format
├── docs
│   ├── report.pdf          # Detailed project report
│   ├── analysis_charts.png # Visualization of attacker behaviors
```

## Author
**Abdulkarim Rahmatu**
Cybersecurity Enthusiast
Email:famirapt@gmail.com

---
For more information or to contribute, feel free to reach out or create a pull request in this repository!
