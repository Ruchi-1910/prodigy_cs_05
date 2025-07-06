# 🛡️ PRODIGY_CYBERSECURITY_05

## 📡 Task-05: Network Packet Analyzer – Cybersecurity Internship

---

### 📘 Task Overview
Developed a **basic network packet analyzer (packet sniffer)** to:

- Capture and analyze **live network traffic**
- Extract useful data such as **source and destination IP addresses** and **protocol types**

This task strengthens understanding of **network communication**, **protocol structures**, and the importance of **ethical boundaries** when working with packet sniffing tools.

---

### ⚙️ Features
✅ Captures **live network packets** using the scapy library  
✅ Extracts and displays:
- **Source IP address**
- **Destination IP address**
- **Protocol used**

✅ Designed for testing with a **configurable packet capture limit**  
✅ Lightweight and efficient for **learning and demonstration purposes**

---

### 📂 Files Included
- `packet_sniffer.py` – Python script implementing the packet analyzer

---

### 🧠 How It Works
1. Uses **Scapy**, a powerful Python packet manipulation library, to sniff packets
2. Defines a **callback function (`packet_callback`)** to process each packet
3. Filters for packets containing an **IP layer**
4. Extracts and displays:
   - **Source IP**
   - **Destination IP**
   - **Protocol number**
5. Captures **10 packets (default)** for testing purposes

---

## 🔗 LinkedIn Post:
[Paste your LinkedIn post link here]

