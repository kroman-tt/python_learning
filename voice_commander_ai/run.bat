@echo off
REM Voice Commander AI - Windows Batch Launcher
REM This script sets up and runs the Voice Commander AI

setlocal enabledelayedexpansion

echo.
echo ================================
echo  VOICE COMMANDER AI LAUNCHER
echo ================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.7+
    pause
    exit /b 1
)

echo ✓ Python found

REM Change to script directory
cd /d "%~dp0"

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo.
    echo Creating virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements if not already installed
python -c "import speech_recognition" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Installing dependencies...
    pip install -r requirements.txt -q
    echo ✓ Dependencies installed
)

REM Ask user what to do
echo.
echo What would you like to do?
echo 1. Run main application
echo 2. Run component tests
echo 3. Run setup wizard
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Voice Commander AI...
    echo.
    python main.py
) else if "%choice%"=="2" (
    echo.
    echo Running component tests...
    echo.
    python test_components.py
) else if "%choice%"=="3" (
    echo.
    echo Running setup wizard...
    echo.
    python setup.py
) else (
    echo Exiting...
    exit /b 0
)

echo.
pause
