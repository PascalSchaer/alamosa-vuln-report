## Finding: Exposed PaperCut NG Interface – Adams State University

**Date Discovered:** August 4, 2025  
**IP Address:** 192.156.134.153  
**Domain:** adams.edu  
**Organization:** Adams State University  
**Location:** Alamosa, Colorado  
**Ports Open:** 80 (redirect), 443 (HTTPS)  
**Service:** PaperCut NG 24.0 – Print Management Web Interface (srvprn1.ad.adams.edu)

---

### Description
A publicly accessible instance of PaperCut NG version 24.0 was identified via Shodan at Adams State University. The service is exposed over HTTPS with no access controls, such as VPN, IP filtering, or Web Application Firewall (WAF). The login page reveals session cookies and application metadata, and uses a certificate issued by Let's Encrypt, valid through July 20, 2025.

The PaperCut NG software has historically been vulnerable to remote code execution (RCE) and authentication bypass vulnerabilities (e.g., CVE-2023-27350, CVE-2023-27351)—making unprotected public access a significant risk if the system is not fully patched.

---

### Risk Summary
- Exposure of internal administrative software to the public internet  
- Potential for exploitation of known PaperCut vulnerabilities if unpatched  
- Disclosure of system metadata (cookies, software version, headers)  
- Increased attacker reconnaissance capability  
- Risk of credential harvesting, brute-force attacks, or lateral movement  

---

### Evidence
- **Login Interface:** PaperCut NG 24.0 with institutional branding  
- **SSL Certificate:** Issued by Let's Encrypt, expires July 20, 2025  
- **Cookie Header:** SESSIONID token present  
- **Shodan Metadata:** Identifies service, hostnames, and geolocation  

---

### Assets
- `data/adams-state/raw/papercut-data.txt` – Raw Shodan response  
- `data/adams-state/screenshots/papercut-login.png` – Screenshot of exposed login page  

---

### Recommendations
- Restrict external access immediately via IP allowlisting, firewall rules, or VPN  
- Verify PaperCut NG is fully patched and up to date  
- Implement login hardening: CAPTCHA, rate-limiting, lockout after failed attempts  
- Apply server hardening and enable WAF if public exposure is absolutely required  
- Review access logs for any signs of unauthorized access  

---

### Notes
This report is based on publicly available Shodan data. No active probing or exploitation was performed. Responsible disclosure steps will be followed if applicable.
