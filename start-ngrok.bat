@echo off
cd /d "C:\以圖搜圖"
start /min "以圖搜圖" python app.py
timeout /t 8 /nobreak >nul
start /min "ngrok" ngrok http 5000
echo 以圖搜圖 + ngrok 已啟動！
echo 手機瀏覽器輸入：https://matador-tasty-chop.ngrok-free.dev
echo.
echo 關閉程式：雙擊 stop.bat
pause
