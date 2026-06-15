@echo off
chcp 65001 >nul
cd /d C:\TiendaColombia-main
echo Iniciando servidor en http://localhost:8000  (cierra esta ventana para detenerlo)
python manage.py runserver
pause
