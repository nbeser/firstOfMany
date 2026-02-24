# firstOfMany

A collection of early Python/PyQt code projects — kept here for reference and future cleanup.

This repository contains initial tools and UI modules for a desktop application built with Python and PyQt. It includes forms and logic for basic database-backed workflows such as machine, customer, and analysis management.

> ⚠️ No single entrypoint or polished application state yet — this is a work-in-progress archive.

---

## 📦 What’s Included

These files represent early iterations of UI and functionality:

- `.py` modules — core logic (DB manager, models, app entrypoint)
- `.ui` files — Qt Designer UI definitions
- Supporting scripts for importing & exporting data  
- A PyInstaller spec for packaging into an executable

All code is experimental and evolving.

---

## 🧠 Motivation

This repo started as a first of many projects intended to explore a Python + Qt desktop workflow, including:

- Building forms and views with Qt Designer
- Connecting UI to Python backend logic
- Managing local data via a simple database layer

Eventually the repo can evolve into a more cohesive product, but for now it serves as a sandbox and reference point.

---

## 🚀 How to Use

If you want to explore or run the code:

1. Clone the repository  
   ```bash
   git clone https://github.com/nbeser/firstOfMany.git
   cd firstOfMany

2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows


python app.py

