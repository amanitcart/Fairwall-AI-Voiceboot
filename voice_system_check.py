import subprocess
import sys
import importlib

REQUIRED_PACKAGES = [
    "pyttsx3",
    "speech_recognition",
    "pyaudio",
    "openai"
]

def install_package(package):
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install():
    for package in REQUIRED_PACKAGES:
        try:
            importlib.import_module(package)
            print(f"{package} already installed ✅")
        except ImportError:
            print(f"{package} not found ❌")
            install_package(package)

if __name__ == "__main__":
    check_and_install()
