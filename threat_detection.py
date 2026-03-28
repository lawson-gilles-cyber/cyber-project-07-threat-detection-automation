logs = [
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN SUCCESS - admin - 45.33.32.1",
    "FILE ACCESS - confidential.docx",
    "LOGIN FAILED - user - 192.168.1.5"
]

THRESHOLD = 3

failed_attempts = {}
alerts = []

for log in logs:
    parts = log.split(" - ")
    event = parts[0]

    if event == "LOGIN FAILED":
        user = parts[1]
        ip = parts[2]

        if ip not in failed_attempts:
            failed_attempts[ip] = 0

        failed_attempts[ip] += 1

        if failed_attempts[ip] == THRESHOLD:
            alerts.append(f"[ALERT] Brute force detected from {ip}")

    elif event == "LOGIN SUCCESS":
        user = parts[1]
        ip = parts[2]

        if ip in failed_attempts and failed_attempts[ip] >= THRESHOLD:
            alerts.append(f"[ALERT] Suspicious login from {ip}")

    elif event == "FILE ACCESS":
        file = parts[1]
        alerts.append(f"[ALERT] Sensitive file accessed: {file}")

print("=== Threat Detection Report ===\n")

for alert in alerts:
    print(alert)
