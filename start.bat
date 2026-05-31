@echo off
cd /d "C:\以圖搜圖"
echo 正在啟動以圖搜圖...
start /min "以圖搜圖" python app.py
timeout /t 5 /nobreak >nul
echo.
echo 以圖搜圖已啟動！
echo.
echo 使用方式：
echo 1. 手機開熱點，電腦連手機 WiFi
echo 2. 打開電腦瀏覽器輸入 http://127.0.0.1:5000 測試
echo 3. 手機瀏覽器輸入 http://[電腦IP]:5000
echo.
echo 查看電腦IP：在 cmd 輸入 ipconfig 找 IPv4 位址
echo 關閉程式：雙擊 stop.bat
pause
