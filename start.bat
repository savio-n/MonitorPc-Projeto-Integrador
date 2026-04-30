@echo off

cd /d "C:\Users\%USERNAME%\MonitorPc"

echo ================================
echo Diretorio atual:
cd
echo ================================

IF NOT EXIST venv (
    echo Criando ambiente virtual...
    python -m venv venv
)

echo ================================
echo Ativando ambiente virtual...
echo ================================

call venv\Scripts\activate

echo ================================
echo Atualizando pip...
echo ================================

python -m pip install --upgrade pip

echo ================================
echo Instalando dependencias...
echo ================================

pip install -r requirements.txt

echo ================================
echo Iniciando aplicacao...
echo ================================

streamlit run main.py

pause