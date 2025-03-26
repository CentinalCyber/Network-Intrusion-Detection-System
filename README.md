# Network-Intrusion-Detection-System
Python based network intrusion detection system using Suricata and Raspberry Pi with real-time physical alerts


# Raspberry Pi Network Intrusion Detection System (NIDS)

This project uses a **Raspberry Pi 4**, **Suricata**, and a **Freenove Super Starter Kit** to create a Network Intrusion Detection System (NIDS). When a Suricata alert is triggered, the system activates a **buzzer** and **LED** to indicate potential malicious traffic.

## 🔧 Hardware Used
- Raspberry Pi 4 Model B
- LED
- Buzzer
- Jumper wires

## 🛠️ Software & Tools
- **Suricata**: Open-source intrusion detection engine
- **Python**
- **RPi.GPIO** and **time** libraries

## 📷 Project Setup

![NIDS Setup](NIDS.Photo.png)

## 🧠 How It Works
- Suricata monitors network traffic and generates alerts
- A Python script constantly checks the alert file
- If an alert is detected, it triggers a **buzzer** and **LED**

## 🗂️ Files
- `nids_alert_system.py`: Main Python script monitoring Suricata and triggering hardware alerts
- `NIDS.Photo.png`: Image of the Raspberry Pi setup (optional)

## 🚀 How to Run
Install required libraries:
```bash
pip install RPi.GPIO


