"""The banner's scenes. Every line is a product claim: keep each one true of
the shipped code (see the audit in the commit that introduced this file).
Synthetic data only. Max 4 lines per panel, 40 characters per line.

Segment kinds: n plain · pii detected on the device (turns orange) ·
tok replacement / label (orange, bold) · red · dim · late (first segment only:
the line arrives last).
"""


def L(*segs):
    return list(segs)


SCENES = [
    dict(
        chip="Mask", verb="DETECT · MASK", badge="dots",
        alt="personal data typed into a prompt is replaced with [PERSON], [EMAIL] and [CREDIT_CARD] before it leaves the device",
        left_label="TYPED ON THE DEVICE", right_label="SENT TO THE AI SERVICE",
        left=[L(("n", "Write to "), ("pii", "Jane Doe"), ("n", " about the claim.")),
              L(("n", "Email: "), ("pii", "jane.doe@example.com")),
              L(("n", "Card: "), ("pii", "4111 1111 1111 1111"))],
        right=[L(("n", "Write to "), ("tok", "[PERSON]"), ("n", " about the claim.")),
               L(("n", "Email: "), ("tok", "[EMAIL]")),
               L(("n", "Card: "), ("tok", "[CREDIT_CARD]"))],
    ),
    dict(
        chip="Pseudonymise", verb="PSEUDONYMISE", badge="dots",
        alt="names and emails are swapped for realistic stand-ins; the map stays on the device and the reply is restored to the real names",
        left_label="ON THE DEVICE", right_label="WHAT THE AI SERVICE SEES",
        left=[L(("n", "Draft a note to "), ("pii", "Jane Doe"), ("n", ".")),
              L(("n", "Email: "), ("pii", "jane.doe@example.com")),
              L(),
              L(("late", ""), ("dim", "You read: "), ("n", "Dear Jane Doe,"))],
        right=[L(("n", "Draft a note to "), ("tok", "Michael Carter"), ("n", ".")),
               L(("n", "Email: "), ("tok", "olivia_reed@inbox.com")),
               L(),
               L(("dim", "It replied: "), ("n", "Dear Michael Carter,"))],
    ),
    dict(
        chip="Block", verb="BLOCK", badge="block",
        alt="in Block mode a prompt containing an access key is not sent; the user is told why, and the organisation receives a record of what was detected",
        left_label="TYPED ON THE DEVICE", right_label="SHOWN TO THE USER",
        left=[L(("n", "Why does this deploy fail?")),
              L(("n", "AWS key: "), ("pii", "AKIAIOSFODNN7EXAMPLE"))],
        right=[L(("red", "A request was not sent")),
               L(("n", "It contained "), ("tok", "API_KEY"), ("n", ".")),
               L(("n", "Edit the prompt and try again.")),
               L(("dim", "IT gets a record: block, API_KEY"))],
    ),
    dict(
        chip="Shadow AI", verb="DISCOVER", badge="flag",
        alt="with discovery turned on by IT, traffic to an AI endpoint the firewall does not know yet is recognised as AI and reported to the organisation for review",
        left_label="UNKNOWN AI ENDPOINT · DISCOVERY ON", right_label="REPORTED TO YOUR ORGANISATION",
        left=[L(("n", "POST "), ("pii", "chat.new-ai.example"), ("n", "/v1")),
              L(("n", '{"messages":[{"role":"user",')),
              L(("n", '  "content":"…"}]}'))],
        right=[L(("tok", "AI_DISCOVERY")),
               L(("n", "Looks like an AI endpoint the")),
               L(("n", "firewall cannot inspect yet.")),
               L(("dim", "Admin review: Accept · Dismiss"))],
    ),
    dict(
        chip="MCP & Skills", verb="INVENTORY · RATE", badge="flag",
        alt="MCP servers and agent skills configured on the laptop are inventoried and rated low, medium or high risk with the reason, for IT",
        left_label="FOUND ON THIS LAPTOP", right_label="RISK INVENTORY FOR IT",
        left=[L(("dim", "~/.cursor/mcp.json")),
              L(("n", "  db-tools: "), ("pii", "bash -c ./run.sh")),
              L(("n", "  crm: "), ("pii", "https://mcp.crm.example")),
              L(("dim", "~/.claude/skills/"), ("n", "deploy"))],
        right=[L(("red", "HIGH  "), ("n", "db-tools")),
               L(("dim", "  shell interpreter: any command")),
               L(("tok", "MED   "), ("n", "crm")),
               L(("dim", "  remote: data leaves this machine"))],
    ),
    dict(
        chip="OWASP", verb="MAP TO OWASP", badge="check",
        alt="sensitive information disclosure (OWASP LLM02) is addressed by masking on the device, and agent skills are tagged with OWASP Agentic Skills Top 10 codes",
        left_label="OWASP RISK", right_label="HOW THE FIREWALL ANSWERS IT",
        left=[L(("tok", "LLM02 "), ("n", "Sensitive information")),
              L(("n", "      disclosure")),
              L(("tok", "AST "), ("n", "OWASP Agentic Skills")),
              L(("n", "    Top 10"))],
        right=[L(("n", "Personal data and secrets are")),
               L(("n", "masked before the prompt leaves.")),
               L(("n", "Each skill is tagged with its")),
               L(("n", "AST risk codes for IT review."))],
    ),
    dict(
        chip="DLP", verb="DETECT", badge="check",
        alt="the firewall inspects prompts, images and tool output, and detects names, financial and health identifiers, secrets and custom patterns in seven languages",
        left_label="INSPECTED ON THE DEVICE", right_label="DETECTED",
        left=[L(("n", "Prompts to ChatGPT, Claude,")),
              L(("n", "Gemini and other AI services")),
              L(("n", "Images: text found, blacked out")),
              L(("n", "Tool output sent by AI agents"))],
        right=[L(("n", "Names, orgs, places · 7 languages")),
               L(("n", "Card, IBAN, SSN, passport, phone")),
               L(("n", "MRN, NPI · API and private keys")),
               L(("tok", "+ "), ("n", "your own custom patterns"))],
    ),
]
