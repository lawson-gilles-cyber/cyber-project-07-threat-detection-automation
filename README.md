# 🤖 cyber-project-07-threat-detection-automation
Python-based threat detection automation from logs (SOC simulation)


## Context

Modern SOC environments rely on automation to detect threats efficiently.

This project simulates automated threat detection using Python.

---

## Objective

* Automate log analysis
* Detect multiple threat types
* Generate alerts

---

## 🔍 Logs

```id="4t9w0g"
LOGIN FAILED - admin - 45.33.32.1
LOGIN FAILED - admin - 45.33.32.1
LOGIN FAILED - admin - 45.33.32.1
LOGIN SUCCESS - admin - 45.33.32.1
FILE ACCESS - confidential.docx
LOGIN FAILED - user - 192.168.1.5
```

---

## Detection Logic

* Brute force → multiple failed logins
* Suspicious login → success after failures
* Sensitive file access → critical file access

---

## Conclusion

Multiple threats detected:

* Brute force attack
* Account compromise
* Sensitive data access

---

## Recommendations

* Block suspicious IPs
* Reset compromised accounts
* Monitor sensitive file access

---

## Key Takeaways

* Automation in cybersecurity
* Threat detection logic
* SOC workflow simulation

---

## 👨‍💻 Author

Part of my cybersecurity learning journey.
