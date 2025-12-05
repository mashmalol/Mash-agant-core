# Setup Instructions for Pushing to GitHub

Since Git is not currently installed on your system, follow these steps to push the MASHCOOK agent to GitHub:

## Option 1: Install Git and Push

### 1. Install Git
- **Windows**: Download from https://git-scm.com/download/win
- Or use: `winget install Git.Git` (if winget is available)

### 2. Configure Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Initialize Repository and Push
```bash
# Navigate to your project directory
cd D:\AGANTE

# Initialize git repository
git init

# Add remote repository
git remote add origin https://github.com/mashmalol/MashCook-agant-core.git

# Add all files (excluding .gitignore items)
git add .

# Commit files
git commit -m "Initial commit: MASHCOOK PERSIAN GASTRONOME v5.2"

# Push to GitHub
git push -u origin main
```

If the repository uses `master` instead of `main`:
```bash
git branch -M main
git push -u origin main
```

## Option 2: Use GitHub Desktop

1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your GitHub account
3. File → Add Local Repository → Select `D:\AGANTE`
4. Publish repository to `mashmalol/MashCook-agant-core`

## Option 3: Use GitHub Web Interface

1. Go to https://github.com/mashmalol/MashCook-agant-core
2. Click "uploading an existing file"
3. Drag and drop these files:
   - `mashcook_agent.py`
   - `mashcook_interactive.py`
   - `mashcook_demo.py`
   - `run_mashcook.py`
   - `README.md`
   - `requirements.txt`
   - `.gitignore`
   - `MASHCOOK_README.md`
   - `MASHCOOK_SETUP.md`

## Files to Include

✅ **Include these files:**
- `mashcook_agent.py` - Main agent
- `mashcook_interactive.py` - Interactive interface
- `mashcook_demo.py` - Demo script
- `run_mashcook.py` - Launcher
- `README.md` - Repository README
- `requirements.txt` - Dependencies
- `.gitignore` - Git ignore rules
- `MASHCOOK_README.md` - Documentation
- `MASHCOOK_SETUP.md` - Setup guide

❌ **Do NOT include:**
- `agent-framework/` folder (too large, users install via pip)
- `agent-framework.zip`
- `__pycache__/` folders
- `.env` files (contains API keys)
- Any files with API keys

## After Pushing

1. Add a description to your GitHub repository
2. Add topics/tags: `python`, `ai-agent`, `persian-cuisine`, `culinary-ai`, `mashcook`
3. Consider adding a LICENSE file (MIT recommended)
4. Enable GitHub Pages if you want documentation site

## Security Note

⚠️ **IMPORTANT**: Make sure you've removed any API keys from the code before pushing!

The `.gitignore` file will prevent `.env` files from being committed, but double-check that no API keys are hardcoded in the Python files.

