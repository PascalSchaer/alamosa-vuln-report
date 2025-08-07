\# Findings: San Luis Valley Medical Center



\*\*Target IP:\*\* 205.189.99.50  

\*\*Organization:\*\* San Luis Valley Regional Medical Center  

\*\*City:\*\* Alamosa, CO  

\*\*ISP:\*\* San Luis Valley Regional Medical Center  

\*\*ASN:\*\* AS32170  

\*\*Last Seen:\*\* 2025-08-02 (via Shodan)



---



\## Summary



A publicly accessible SIP (Session Initiation Protocol) service was discovered running on UDP port 5060. This service responds to SIP OPTIONS and REGISTER requests with a `403 Forbidden` response, confirming it is active and processing SIP traffic. While this alone may not represent an immediate vulnerability, publicly exposed VoIP services are often targeted for enumeration, abuse, toll fraud, or denial-of-service attacks if not secured properly.



---



\*\*Port:\*\* 5060/UDP  

\*\*Service:\*\* SIP (VoIP Signaling)  

\*\*Response:\*\* SIP/2.0 403 Forbidden  

\*\*Detection Methods:\*\*  

&nbsp; - \[x] Shodan.io  

&nbsp; - \[x] Nmap with `--script=sip-methods` and service version detection  

&nbsp; - \[x] SIPVicious toolkit (`svmap`, `svwar`)



\### Nmap Output (Excerpt)



```txt

PORT     STATE         SERVICE

5060/udp open|filtered sip

| sip-methods:

|   SIP/2.0 403 Forbidden

|   From: <sip:nmap@mg>;tag=root

|   To: <sip:nmap@mg>;tag=zxcvbn098mnb0984e8

|   CSeq: 42 OPTIONS

|   Call-ID: 50000

|   Via: SIP/2.0/UDP mg;branch=foo;port

|   Content-Length: 0

\## Risk Overview



| Risk | Details |

|------|---------|

| \*\*Exposure\*\* | Port 5060 is open to the public internet |

| \*\*Service Confirmation\*\* | Service replies to SIP OPTIONS and REGISTER |

| \*\*Risk Level\*\* | 🟡 Medium (Informational exposure) |

| \*\*Potential Threats\*\* | SIP enumeration, DoS, toll fraud, VoIP recon |



---



\## Supporting Evidence



\- `screenshots/shodan-sip-5060.png`

\- `screenshots/nmap-sip-scan.png`

\- `screenshots/nmap-service-detection-5060.png`

\- `screenshots/sipvicious-svmap-svwar-results.png`

\- `raw/sip.scan.txt`

\- `raw/nmap-service-detection-5060.txt`

\- `raw/sipvicious-svmap-svwar.txt`



---



\## Recommendations



\- Restrict access to UDP port 5060 using firewall rules or ACLs

\- Ensure SIP authentication is enabled and properly enforced

\- Apply rate limiting and SIP-aware IDS/IPS filtering

\- Monitor for unauthorized SIP traffic and scanning activity

\- Disable or move SIP services if unused externally



---



\## Additional Notes



Tools from the SIPVicious toolkit (`svmap`, `svwar`) were used strictly for passive or blocked information gathering. No brute force, extension enumeration, or exploit attempts were performed.



All reconnaissance was conducted legally and ethically to raise awareness of exposed services in critical infrastructure.

