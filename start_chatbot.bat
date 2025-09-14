@echo off
echo ========================================
echo    INGRES ChatBot MVP - Starting...
echo ========================================
echo.

echo [1/2] Starting Backend Server...
cd backend
start cmd /k "python app.py"

echo [2/2] Waiting for server to start...
timeout /t 3 /nobreak > nul

echo.
echo ========================================
echo    ChatBot is ready!
echo ========================================
echo.
echo Opening the ChatBot interface in your browser...
start frontend\index.html

echo.
echo Press any key to exit this window...
pause > nul
