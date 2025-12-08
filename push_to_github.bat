@echo off
REM Batch script to push code to GitHub
REM Run this script after installing Git

echo 🚀 Pushing code to GitHub...

REM Check if git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git found
echo.

REM Initialize git if not already initialized
if not exist .git (
    echo 📦 Initializing git repository...
    git init
)

REM Add all files
echo 📝 Adding files...
git add .

REM Commit changes
echo 💾 Committing changes...
git commit -m "Add .env file support and multi-provider API integration - Add .env.example template - Add python-dotenv - Support OpenAI/Anthropic/Azure - Update UI with provider selection - Add documentation"

REM Rename branch to main
echo 🌿 Setting branch to main...
git branch -M main

REM Check if remote already exists
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo 🔗 Adding remote repository...
    git remote add origin https://github.com/mashmalol/python-core-agant-tamplatev1.git
) else (
    echo ℹ️  Remote already configured
)

REM Push to GitHub
echo ⬆️  Pushing to GitHub...
git push -u origin main

if errorlevel 1 (
    echo ❌ Push failed. You may need to:
    echo    1. Configure Git credentials
    echo    2. Use a personal access token instead of password
    echo    3. Check your internet connection
) else (
    echo ✅ Successfully pushed to GitHub!
    echo 🔗 Repository: https://github.com/mashmalol/python-core-agant-tamplatev1
)

pause

