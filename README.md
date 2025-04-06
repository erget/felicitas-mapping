# Test of local 3d mapping of Felicitas cave

This repo is a bunch of utilities for making a 3d map of an underwater cave.
It's for me - don't expect it to work for you.
Right now I need to make things reproducible and may share more of that in the future.
Currently this is only so that I can work across computers.

## Requirements
- Use Python 3.10+
- Install the stuff in `requirements.txt`
- Get Meshroom

Currently I'm expecting a video that's referenced in the `extract_cube_faces.py`.
You can get it [here](https://drive.google.com/file/d/1cegWtwOpHCYiQ4aypzh_ni9uc2dr2GVp/view?usp=drive_link).

## 🐍 Python Setup

Set up a Python virtual environment:

```bash
# Navigate to your project directory
cd meshroom-workflow

# Create a virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

