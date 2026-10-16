<p align="center">
  <a href="https://www.scnsoft.com/artificial-intelligence/firewall">
    <img src="https://raw.githubusercontent.com/ScienceSoft-Endpoint-AI-Firewall/.github/main/assets/banner.svg" width="100%" alt="ScienceSoft Endpoint AI Firewall, an animated journey in seven steps: mask personal data, pseudonymise it with realistic stand-ins, block a prompt with a secret, discover unknown AI endpoints, inventory and rate MCP servers and skills, map to OWASP, and the DLP detectors behind it all">
  </a>
</p>

<p align="center">
  <a href="https://www.scnsoft.com/artificial-intelligence/firewall"><b>Product page</b></a> ·
  <a href="https://www.scnsoft.com/artificial-intelligence/gateway-firewall">AI Firewall &amp; MCP Gateway</a> ·
  <a href="https://sciencesoft-endpoint-ai-firewall.github.io/">Documentation</a> ·
  <a href="https://github.com/ScienceSoft-Endpoint-AI-Firewall/trial-releases/releases">Download the trial</a>
</p>

## The problem

Employees paste client names, contact details, account numbers, health records
and credentials into ChatGPT, Claude, Gemini and other AI assistants every day.
Once a prompt leaves the device the organisation cannot take it back, and a
policy document alone does not stop it.

## What it does

AI Firewall is an agent that runs on each employee's own computer (macOS and
Windows). It inspects that device's outbound requests to AI services, finds
personal and confidential data in them, and **masks or redacts it before the
request leaves the machine**.

<table>
  <tr>
    <td align="center" valign="top" width="25%"><img src="https://raw.githubusercontent.com/ScienceSoft-Endpoint-AI-Firewall/.github/main/assets/detect.svg" width="72" alt=""><br><b>Detect</b><br><sub>Names, contact details, account and ID numbers, health data and secrets — patterns, a named-entity model, OCR for images.</sub></td>
    <td align="center" valign="top" width="25%"><img src="https://raw.githubusercontent.com/ScienceSoft-Endpoint-AI-Firewall/.github/main/assets/mask.svg" width="72" alt=""><br><b>Mask</b><br><sub>The AI service receives the prompt with those values replaced. The original text is not sent to the vendor.</sub></td>
    <td align="center" valign="top" width="25%"><img src="https://raw.githubusercontent.com/ScienceSoft-Endpoint-AI-Firewall/.github/main/assets/audit.svg" width="72" alt=""><br><b>Audit</b><br><sub>A tamper-evident audit trail gives IT and compliance evidence that the data was protected.</sub></td>
    <td align="center" valign="top" width="25%"><img src="https://raw.githubusercontent.com/ScienceSoft-Endpoint-AI-Firewall/.github/main/assets/fleet.svg" width="72" alt=""><br><b>Fleet policy</b><br><sub>Policy is set once per organisation and distributed to every enrolled device, with a fleet console.</sub></td>
  </tr>
</table>

<p align="center">
  <img src="https://raw.githubusercontent.com/ScienceSoft-Endpoint-AI-Firewall/.github/main/assets/how-it-works.svg" width="100%" alt="How it works: the agent on the employee's computer detects personal data in a prompt and replaces it. The AI service receives the masked prompt. An enrolled device also sends the organisation's workspace what was detected and the masked message. The raw prompt and the detected values stay on the device.">
</p>

## Privacy: what is protected, and what is recorded

Protected: detected values are never collected, and the raw prompt never leaves
the device. Matching happens locally.

Recorded: on a device enrolled in an organisation, the organisation's workspace
receives a record of what was detected and the message with those values already
replaced. Your employer can see that record.

## Who it is for

Organisations in regulated or client-confidential fields whose staff use AI
assistants and who need to show that personal data did not leave in a prompt.

## Repositories

| Repository | Purpose |
|---|---|
| [`ScienceSoft-Endpoint-AI-Firewall.github.io`](https://github.com/ScienceSoft-Endpoint-AI-Firewall/ScienceSoft-Endpoint-AI-Firewall.github.io) | User and administrator documentation |
| [`trial-releases`](https://github.com/ScienceSoft-Endpoint-AI-Firewall/trial-releases) | Trial builds for macOS and Windows (releases only, no source) |
| [`utilities`](https://github.com/ScienceSoft-Endpoint-AI-Firewall/utilities) | Scripts for deploying the application and rolling out agents |

## Learn more

- [ScienceSoft On-Device AI Firewall](https://www.scnsoft.com/artificial-intelligence/firewall) — the product page
- [Enterprise AI Control Layer: AI Firewall & MCP Gateway](https://www.scnsoft.com/artificial-intelligence/gateway-firewall) — the wider ScienceSoft offering, including governing how AI applications reach internal systems

---

<p align="center">
  <img src="https://raw.githubusercontent.com/ScienceSoft-Endpoint-AI-Firewall/.github/main/assets/logo-animated.svg" width="48" alt=""><br>
  Developed and maintained by <a href="https://www.scnsoft.com/"><b>ScienceSoft</b></a>.<br>
  © ScienceSoft. All rights reserved.
</p>
