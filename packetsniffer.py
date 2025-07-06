from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"[+] New Packet: {ip_layer.src} --> {ip_layer.dst} | Protocol: {ip_layer.proto}")

sniff(prn=packet_callback, count=10)  # Capture 10 packets for testing
