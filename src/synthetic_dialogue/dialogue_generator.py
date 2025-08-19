# src/synthetic_dialogue/dialogue_generator.py

from synthetic_dialogue.agents import Agent
from synthetic_dialogue.prompts import get_prompt

class DialogueGenerator:
    def __init__(self):
        pass

    def generate(self, role_sequence):
        dialogue = []
        for i, role in enumerate(role_sequence):
            agent = Agent(name=f"Agent{i+1}", role=role)
            intent = agent.get_intent()
            prompt = get_prompt(role, intent)
            dialogue.append({
                "agent": agent.name,
                "role": role,
                "intent": intent,
                "message": prompt
            })
        return dialogue
