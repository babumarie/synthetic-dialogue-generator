# src/synthetic_dialogue/prompts.py

def get_prompt(role, intent):
    templates = {
        "Analyst": f"As an Analyst, your goal is to {intent}. What indicators do you see?",
        "Attacker": f"As an Attacker, your goal is to {intent}. What exploit will you use?",
        "Defender": f"As a Defender, your goal is to {intent}. How will you respond?"
    }
    return templates.get(role, "No prompt available.")
