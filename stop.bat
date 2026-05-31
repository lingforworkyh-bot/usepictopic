@echo off
taskkill /fi "WINDOWTITLE eq 以圖搜圖*" /f >nul 2>&1
taskkill /fi "WINDOWTITLE eq ngrok隧道*" /f >nul 2>&1
echo 已關閉以圖搜圖
pause
