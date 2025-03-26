# Network-Intrusion-Detection-System
Python based network intrusion detection system using Raspberry Pi with real-time physical alerts


📡 Raspberry Pi Network Intrusion Detection Simulation (Ping-Based Alert System)
This project simulates a basic network intrusion detection system (NIDS) using a Raspberry Pi, Python, and GPIO components (LED + buzzer). When the Raspberry Pi receives a network ping (ICMP request), it treats it as a simulated attack. The system then triggers an audible and visual alert using a buzzer and an LED.

🛠️ Key Features
Detects incoming ping requests as simulated "network attacks"

Sounds a buzzer briefly and activates an LED alert

LED stays on for 3 seconds, then blinks for 10 seconds

Fully resets and waits for the next detection


🧠 What This Project Demonstrates
This system is designed to bridge cybersecurity concepts and physical hardware. While not using deep packet inspection or real intrusion detection software like Suricata, it introduces core ideas such as:

Simulating threat detection

Using GPIO to trigger physical responses

Creating event-driven logic for network activity

🖥️ How to Use It
Run the Python script on your Raspberry Pi.
In another terminal, simulate an "attack" by pinging the Pi’s IP:

'ping [Raspberry Pi IP]'

When the Pi detects the ping, the buzzer will sound briefly and the LED will light up and blink, alerting you of the "intrusion."


