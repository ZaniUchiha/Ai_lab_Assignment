# Lab 5 — AI Helper (Zain Abdullah)

This repository contains a Jupyter Notebook with 5 small tasks demonstrating simple rule-based NLP, decision logic, recommendations, an FSM simulator, and a chat-summary bot.

Files
- [lab_5_Zain_Abdullah.ipynb](lab_5_Zain_Abdullah.ipynb)
- [.ipynb_checkpoints/lab_5_Zain_Abdullah-checkpoint.ipynb](.ipynb_checkpoints/lab_5_Zain_Abdullah-checkpoint.ipynb)

Summary of tasks / key functions
- Task 1 — Intent classification: [`classify_intent`](lab_5_Zain_Abdullah.ipynb) — simple keyword matching for intents (greeting, goodbye, thanks, food, study).
- Task 2 — Scholarship decision: [`decide_scholarship`](lab_5_Zain_Abdullah.ipynb) — decides "Full", "Half", or "No scholarship" based on CGPA, family salary, and achievements. Rules include checks like $CGPA \ge 3.70$ and salary $\le 60000$.
- Task 3 — Activity recommender: [`activity_recomendor`](lab_5_Zain_Abdullah.ipynb) — recommends activities (read, walk, nap, music) based on feeling and time of day.
- Task 4 — FSM traffic light: [`run_traffic_lights`](lab_5_Zain_Abdullah.ipynb) — cycles RED → GREEN → YELLOW and returns visited states.
- Task 5 & Chat — Bot reply and session: [`bot_reply`](lab_5_Zain_Abdullah.ipynb) — uses `classify_intent` and `activity_recomendor` to generate replies and stores conversation history.

Requirements
- Python 3.8 or newer.
- Jupyter Notebook or VS Code (Notebook support).
- No external Python packages required (uses standard library: `time`, built-ins).
- Optional: to run as a script, install Jupyter to convert the notebook:
  - pip install jupyter

Running
- Open [lab_5_Zain_Abdullah.ipynb](lab_5_Zain_Abdullah.ipynb) in Jupyter or VS Code and run the cells interactively.
- To convert to a Python script and run from terminal:
  - jupyter nbconvert --to script lab_5_Zain_Abdullah.ipynb
  - python lab_5_Zain_Abdullah.py

Notes for GitHub
- The notebook file is the primary artifact; GitHub will render the notebook automatically.
- Add a short LICENSE if you want an explicit license.
- Keep the README.md at the repository root (this file) for immediate project context.

If you want, I can add a minimal requirements.txt or convert the notebook to a runnable script.