from collections import Counter

log = [
    ("192.168.1.50", 22), ("192.168.1.50", 23), ("192.168.1.50", 80),
    ("192.168.1.50", 443), ("192.168.1.50", 3389), ("192.168.1.50", 8080),
    ("203.0.113.7", 22), ("203.0.113.7", 22), ("203.0.113.7", 22),
]

ports_by_ip = {}
for ip, port in log:
    ports_by_ip.setdefault(ip, set()).add(port)

port_count = Counter(log)

print("--- Port Scan Detection ---")
for ip, ports in ports_by_ip.items():
    if len(ports) >= 5:
        print(f"ALERT: Port scan detected from {ip} ({len(ports)} ports)")

print("\n--- Brute Force Detection ---")
for (ip, port), count in port_count.items():
    if count >= 3:
        print(f"ALERT: Brute force from {ip} on port {port} ({count} attempts)")
