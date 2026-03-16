# Vehicle Cybersecurity Intrusion Detection System

## Overview

This project implements a prototype Intrusion Detection System (IDS) for connected vehicles.  
The system simulates vehicle telemetry data and detects anomalies using a machine learning model.

To enhance cybersecurity, the system integrates encrypted telemetry and blockchain-based intrusion logging.

## Features

• Vehicle telemetry simulation  
• Machine learning anomaly detection  
• Real-time monitoring dashboard  
• Encrypted vehicle data transmission  
• Blockchain-secured intrusion log storage  

## Technologies

Python  
Flask  
Machine Learning (Isolation Forest)  
Cryptographic encryption  
Blockchain hashing  

## System Architecture

Vehicle Sensors  
↓  
Encrypted Telemetry  
↓  
Intrusion Detection Model  
↓  
Alert Generation  
↓  
Blockchain-secured Intrusion Logs  
↓  
Dashboard Monitoring

## Installation

Clone repository:

git clone https://github.com/USERNAME/vehicle-cybersecurity-ids

Install dependencies:

pip install -r requirements.txt

Run system:

python app.py

Open browser:

http://localhost:5050

## Project Structure

app.py → Flask server  
simulator.py → vehicle telemetry generator  
ids_model.py → intrusion detection model  
encryption.py → encrypted telemetry module  
blockchain.py → blockchain event log  
templates → dashboard interface  

## Future Improvements

• Edge computing IDS deployment  
• CAN bus data integration  
• Real vehicle telemetry datasets
