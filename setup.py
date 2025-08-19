import os

# Define your folder and file structure
structure = {
    "src/synthetic_dialogue": [
        "__init__.py",
        "agents.py",
        "dialogue_generator.py",
        "prompts.py",
        "llm_wrapper.py"
    ],
    "tests": [
        "test_agents.py",
        "test_dialogue_generator.py",
        "test_prompts.py"
    ],
    "notebooks": [
        "synthetic_dialogue_ui.ipynb"
    ],
    ".": [
        "README.md",
        "requirements.txt",
        ".gitignore",
        "setupfile.py"
    ]
}

def create_structure(base_path="."):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")  # Create empty file
    print("✅ Project structure created successfully.")

if __name__ == "__main__":
    create_structure()
