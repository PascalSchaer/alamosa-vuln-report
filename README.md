\# Alamosa Vulnerability Report



This project is a reconnaissance report of publicly exposed services in Alamosa, Colorado, with a special focus on institutions like Adams State University. Using OSINT tools like Shodan, this report documents potentially misconfigured or vulnerable public-facing services that could be of concern.



\## Purpose



To raise awareness about publicly visible services and to demonstrate how security research can be conducted responsibly and transparently.



\## Tools Used



\- \[Shodan](https://www.shodan.io/)

\- Python (for scripting, Shodan API)

\- PowerShell / CLI

\- Git + GitHub



\## Focus Areas



\- Public IP exposure

\- Default credentials

\- Open ports and services

\- Expired SSL certificates

\- Deprecated or vulnerable software



\## Ethical Statement



This report is generated using publicly available data. No unauthorized access, exploitation, or interference with services has taken place. All findings are intended to support cybersecurity awareness and responsible disclosure.



\## Notable Findings



\### 🔎 PaperCut NG Exposure at Adams State University



\- \*\*Discovered:\*\* August 2025

\- \*\*Target:\*\* Adams State University (Alamosa, CO)

\- \*\*Service:\*\* PaperCut NG login portal

\- \*\*Port:\*\* 443 (HTTPS)

\- \*\*Risk:\*\* Publicly exposed printing portal with no access control, which historically has had vulnerabilities (RCE, auth bypass)

\- \*\*Action Taken:\*\* Findings documented and shared responsibly in \[report.md](./report.md)



\## Author



Pascal Schaer

Cybersecurity student and researcher

\[github.com/PascalSchaer](https://github.com/PascalSchaer)





\## Disclaimer



This project is for educational and research purposes only.

