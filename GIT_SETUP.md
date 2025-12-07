# Git Setup Instructions

## After Installing Git

Run these commands in order:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "first commit"

# Rename branch to main
git branch -M main

# Add remote repository
git remote add origin https://github.com/mashmalol/python-core-agant-tamplatev1.git

# Push to GitHub
git push -u origin main
```

## Files Ready to Commit

- `agent.py` - Main agent implementation
- `interactive.py` - Interactive chatbot interface
- `run_agent.py` - Launcher script
- `core.json` - Agent core specification
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

## Note

Make sure you have:
1. Git installed on your system
2. GitHub account credentials configured
3. Access to the repository: https://github.com/mashmalol/python-core-agant-tamplatev1.git

