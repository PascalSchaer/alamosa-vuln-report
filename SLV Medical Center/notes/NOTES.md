\# SLV Medical Center — Recon Notes



\*\*IP:\*\* 205.189.99.50  

\*\*Organization:\*\* San Luis Valley Regional Medical Center  

\*\*Service Detected:\*\* SIP (VoIP) on UDP port 5060  

\*\*Status:\*\* Service responds to SIP OPTIONS and REGISTER with 403 Forbidden



---



\## Tools Used



\- Shodan (initial discovery)

\- Nmap with `--script=sip-methods`, `-sU -sV`

\- SIPVicious (`svmap`, `svwar`)



---



\## Observations



\- Port 5060 is \*\*open and reachable\*\* from the public internet

\- SIP responses include headers confirming service presence

\- No authentication bypass or SIP extension enumeration was performed

\- `sipvicious` installed but `sipvicious` CLI not available at first (`command not found`)

\- No active attack attempted — stayed passive



---



\## Evidence Files



\- `sip.scan.txt` — initial Nmap UDP scan with SIP methods

\- `nmap-service-detection-5060.txt` — full Nmap version detection

\- `sipvicious-svmap-svwar.txt` — passive SIPVicious output

\- Screenshots saved in `/screenshots/`

