"""
Setup Guide for Voice Commander AI
Follow these steps to get the application running
"""

import subprocess
import sys
import os


def run_command(cmd):
    """Run a shell command"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def check_python_version():
    """Check if Python version is 3.7 or higher"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✅ Python version {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} - Need Python 3.7+")
        return False


def install_requirements():
    """Install requirements from requirements.txt"""
    print("\n📦 Installing required packages...")
    
    success, stdout, stderr = run_command(f"{sys.executable} -m pip install -r requirements.txt")
    
    if success:
        print("✅ All packages installed successfully")
        return True
    else:
        print("❌ Failed to install packages")
        print(stderr)
        return False


def install_pyaudio_windows():
    """Install PyAudio on Windows (special handling)"""
    print("\n🔧 Installing PyAudio (Windows specific)...")
    
    # Try pipwin method
    print("  Attempting to install via pipwin...")
    run_command(f"{sys.executable} -m pip install pipwin")
    success, _, _ = run_command("pipwin install pyaudio")
    
    if success:
        print("✅ PyAudio installed via pipwin")
        return True
    
    # Fallback: try pip directly
    print("  Trying direct pip installation...")
    success, _, _ = run_command(f"{sys.executable} -m pip install pyaudio")
    
    if success:
        print("✅ PyAudio installed via pip")
        return True
    else:
        print("⚠️  PyAudio installation may have issues")
        print("   Try: pip install pipwin ; pipwin install pyaudio")
        return False


def verify_installation():
    """Verify that all dependencies are installed"""
    print("\n🔍 Verifying installation...")
    
    modules = [
        'speech_recognition',
        'pyttsx3',
        'pyaudio',
        'requests',
    ]
    
    all_ok = True
    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module} - OK")
        except ImportError:
            print(f"❌ {module} - NOT FOUND")
            all_ok = False
    
    return all_ok


def setup():
    """Main setup function"""
    print("\n" + "="*60)
    print("🤖 VOICE COMMANDER AI - SETUP WIZARD")
    print("="*60)
    
    # Step 1: Check Python version
    print("\n📋 Step 1: Checking Python version...")
    if not check_python_version():
        print("\n❌ Setup failed: Python 3.7+ is required")
        return False
    
    # Step 2: Install requirements
    print("\n📋 Step 2: Installing dependencies...")
    if not install_requirements():
        print("\n⚠️  Some packages failed to install")
    
    # Step 3: Special handling for PyAudio on Windows
    print("\n📋 Step 3: Verifying PyAudio installation...")
    try:
        import pyaudio
        print("✅ PyAudio already installed")
    except ImportError:
        print("⚠️  PyAudio not found. Attempting to install...")
        install_pyaudio_windows()
    
    # Step 4: Verify all installations
    print("\n📋 Step 4: Verifying all components...")
    if not verify_installation():
        print("\n⚠️  Some components are missing")
        print("Please install them manually:")
        print("  pip install SpeechRecognition pyttsx3 requests")
        print("  pipwin install pyaudio (or pip install pyaudio)")
    
    print("\n" + "="*60)
    print("✅ Setup complete!")
    print("="*60)
    print("\n📖 Next steps:")
    print("  1. Test the installation: python test_components.py")
    print("  2. Run the application: python main.py")
    print("  3. Check README.md for documentation")
    print("\n" + "="*60 + "\n")
    
    return True


if __name__ == "__main__":
    try:
        setup()
    except KeyboardInterrupt:
        print("\n\n⛔ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup error: {e}")
        sys.exit(1)
