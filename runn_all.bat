@echo off
echo ================================
echo 🧹 LIMPIANDO EL PROYECTO
echo ================================

REM Eliminar carpetas __pycache__ y archivos .pyc
for /r %%i in (__pycache__) do (
    echo Eliminando %%i ...
    rmdir /s /q "%%i"
)

for /r %%i in (*.pyc) do (
    echo Eliminando %%i ...
    del /q "%%i"
)

REM Eliminar reporte anterior
if exist reports\report.html (
    echo Eliminando reporte HTML anterior...
    del /q reports\report.html
)

REM Eliminar capturas si existen
if exist screenshots (
    echo Eliminando capturas de pantalla...
    rmdir /s /q screenshots
)

echo ================================
echo 🔧 INSTALANDO DEPENDENCIAS
echo ================================
poetry install

echo ================================
echo 🌐 INSTALANDO PLAYWRIGHT
echo ================================
poetry run playwright install

echo ================================
echo 🧪 EJECUTANDO PRUEBAS
echo ================================
poetry run pytest

echo ================================
echo 📊 ABRIENDO REPORTE HTML
echo ================================
start reports\report.html

pause
