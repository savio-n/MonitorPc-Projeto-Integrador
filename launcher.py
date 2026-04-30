import os
import subprocess
import sys
import time

PROJECT_DIR = rf"C:\Users\{os.getlogin()}\MonitorPc"

os.chdir(PROJECT_DIR)

frames = ["|", "/", "-", "\\"]

print("\nInicializando HardwareAnalysis...\n")

for i in range(30):
    sys.stdout.write(f"\rCarregando {frames[i % 4]}")
    sys.stdout.flush()
    time.sleep(0.1)

print("\n")

if not os.path.exists("venv"):
    print("Criando ambiente virtual...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])

python_path = os.path.join("venv", "Scripts", "python.exe")
pip_path = os.path.join("venv", "Scripts", "pip.exe")

print("Atualizando pip...")
subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"])

print("Instalando dependencias...")
subprocess.run([pip_path, "install", "-r", "requirements.txt"])

print("Iniciando aplicacao...\n")

subprocess.run([
    python_path,
    "-m",
    "streamlit",
    "run",
    "main.py"
])