@echo off
title The Architect's Blueprint - Engineers' Day
echo ========================================================
echo   THE ARCHITECT'S BLUEPRINT - ENGINEERS' DAY
echo ========================================================
echo Starting local web server at http://localhost:8080 ...
start "" "http://localhost:8080"
py -m http.server 8080
pause
