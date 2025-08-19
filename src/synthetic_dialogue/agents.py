# src/synthetic_dialogue/agents.py

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_intent(self):
        role_intents = {
            "Analyst": "Investigate suspicious activity",
            "Attacker": "Exploit vulnerabilities",
            "Defender": "Mitigate threats and secure systems"
        }
        return role_intents.get(self.role, "Unknown intent")
