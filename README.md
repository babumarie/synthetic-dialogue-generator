
# Synthetic Dialogue Generator

This project simulates structured conversations between agents in cybersecurity scenarios. It’s designed to support research in multi-agent systems, secure communication, and NLP-driven dialogue modeling.

---

## Agent Roles & Intents

Agents are assigned roles and generate intent-driven messages:

- **Analyst**: Investigates suspicious activity
- **Attacker**: Exploits vulnerabilities
- **Defender**: Responds to threats and secures systems

Each agent produces context-aware prompts based on their role and intent.

---

## Features

- Role-based intent modeling
- Domain-specific prompt templates (e.g., phishing, intrusion detection)
- Modular architecture for easy extension
- Unit-tested for reliability
- Optional LLM integration via HuggingFace (`distilGPT2`)
- Colab notebook with interactive UI and dialogue flow visualization

---

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

## Usage Example

from synthetic_dialogue.dialogue_generator import DialogueGenerator

roles = ["Analyst", "Attacker", "Defender"]
generator = DialogueGenerator()
dialogue = generator.generate(roles)

for turn in dialogue:
    print(f"{turn['agent']} ({turn['role']}): {turn['message']}")
--

##Running Tests

PYTHONPATH=src python -m unittest discover tests

### Project Structure

synthetic-dialogue-generator/
├── src/
│   └── synthetic_dialogue/
│       ├── agents.py
│       ├── dialogue_generator.py
│       ├── prompts.py
│       ├── llm_wrapper.py
│       └── __init__.py
├── tests/
│   ├── test_agents.py
│   ├── test_dialogue_generator.py
│   ├── test_prompts.py
├── notebooks/
│   └── synthetic_dialogue_ui.ipynb
├── README.md
├── requirements.txt
├── setup.py
├── setupfile.py
└── .gitignore
