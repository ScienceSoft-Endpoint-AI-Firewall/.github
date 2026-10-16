<p align="center">
  <img src="https://github.com/ScienceSoft-Endpoint-AI-Firewall.png" width="96" alt="ScienceSoft Endpoint AI Firewall">
</p>

<h1 align="center">ScienceSoft Endpoint AI Firewall</h1>
<p align="center"><b>Use AI assistants at work without letting confidential data leave in the prompt.</b></p>

<p align="center">
  <a href="https://sciencesoft-endpoint-ai-firewall.github.io/">Documentation</a> ·
  <a href="https://github.com/ScienceSoft-Endpoint-AI-Firewall/trial-releases/releases">Download the trial</a> ·
  <a href="https://github.com/ScienceSoft-Endpoint-AI-Firewall/utilities">Deployment scripts</a>
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

- **Detects** names, contact details, account and ID numbers, health data and
  other personal data, plus secrets such as keys and tokens — using patterns, a
  named-entity model, and OCR for uploaded images.
- **Masks on the device.** The AI service receives the prompt with those values
  replaced; the original text is not sent to the vendor.
- **Proves it happened.** A tamper-evident audit trail, per-organisation policy
  distribution and a fleet console give IT and compliance evidence of protection.

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

---

<p align="center">
  Developed and maintained by <a href="https://www.scnsoft.com/"><b>ScienceSoft</b></a>.<br>
  © ScienceSoft. All rights reserved.
</p>
