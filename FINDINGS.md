## Finding: Exposed PaperCut NG Interface at Adams State University

**Date Discovered:** August 4, 2025  
**IP Address:** 192.156.134.153  
**Domain:** adams.edu  
**Organization:** Adams State University  
**Location:** Alamosa, Colorado  
**Port:** 443 (HTTPS)  
**Service:** PaperCut NG – Print Management Web Interface

### Description:
An instance of **PaperCut NG** was found publicly accessible over HTTPS with no login page obfuscation or rate-limiting mechanisms. The login interface exposes application metadata and session cookies, and it appears to be hosted without advanced protection such as WAF (Web Application Firewall).

### Risks:
- Public exposure of an internal administrative service.
- Possible exploitation of **known CVEs** related to PaperCut NG (e.g., RCE and auth bypass vulnerabilities if unpatched).
- Could aid attackers in credential harvesting or lateral movement if breached.

### Evidence:
- **Title:** PaperCut NG Login for Adams State University
- **Cookie:** SESSIONID token observed
- **SSL Cert:** Issued by Let's Encrypt, valid until July 20, 2025
- **Ports Open:** 80 (redirect), 443 (HTTPS)

### Recommendations:
- Immediately restrict access to the PaperCut NG interface using access control (IP whitelisting or VPN).
- Ensure the PaperCut NG software is fully patched.
- Implement login rate-limiting and obfuscation if public access is required.
- Monitor and alert on any unauthorized access attempts.

### Notes:
This finding is based on public Shodan data and does not include any active probing or exploitation. Responsible disclosure steps will be followed if applicable.
