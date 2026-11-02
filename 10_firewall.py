rules = [
    {"ip": "203.0.113.66", "action": "DENY"},
    {"port": 80, "action": "ALLOW"},
    {"port": 443, "action": "ALLOW"},
    {"ip": "192.168.1.10", "port": 22, "action": "ALLOW"},
]

def check_packet(ip, port):
    for rule in rules:
        if rule.get("ip", ip) == ip and rule.get("port", port) == port:
            return rule["action"]
    return "DENY"

packets = [
    ("198.51.100.5", 80),
    ("198.51.100.5", 22),
    ("192.168.1.10", 22),
    ("203.0.113.66", 443),
]

for ip, port in packets:
    print(f"{ip}:{port} -> {check_packet(ip, port)}")
