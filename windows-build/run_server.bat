@echo off
setlocal
cd /d "%~dp0"
set "NFS13_DATA_DIR=%~dp0"
if not defined NFS13_HOST (
  set /p NFS13_HOST=Enter this server's reachable LAN/VPN IP address: 
)
NFS13-Server.exe
pause
