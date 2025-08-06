\# Adams State University – Vulnerability Observation Report



\*\*Date:\*\* August 6, 2025  

\*\*Researcher:\*\* Pascal Schaer  

\*\*Location Focus:\*\* Alamosa, Colorado  

\*\*Tool Used:\*\* Shodan.io



---



\## Summary



During open-source intelligence (OSINT) reconnaissance of publicly exposed systems in Alamosa, an exposed \*\*PaperCut NG\*\* web interface was identified on Adams State University's public IP (192.156.134.153). This instance was accessible over HTTPS without IP restrictions, WAF protection, or login obfuscation, and returned session tokens in the response.



---



\## Risk Overview



\- \*\*Software:\*\* PaperCut NG (commonly used in campus printing systems)

\- \*\*IP:\*\* 192.156.134.153

\- \*\*Exposure:\*\* Publicly accessible login portal

\- \*\*SSL Certificate:\*\* Valid but not configured with additional security headers

\- \*\*Potential CVEs:\*\* This service has a history of RCE and auth bypass vulnerabilities if unpatched



---



\## Suggested Remediation



\- Restrict access to known networks or VPN

\- Ensure PaperCut NG is up-to-date and patched

\- Implement rate-limiting and/or CAPTCHA on login

\- Monitor for brute-force or credential stuffing attempts



---



\## Intent and Ethics



This report was generated strictly using publicly available internet metadata. No intrusive methods, credential attempts, or exploitation were performed. This is part of a responsible disclosure and cybersecurity education project.



---



\*\*GitHub Repository:\*\* \[github.com/PascalSchaer/alamosa-vuln-report](https://github.com/PascalSchaer/alamosa-vuln-report)



