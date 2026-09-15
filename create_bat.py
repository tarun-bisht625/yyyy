bat_content = """@echo off
title The Architect's Blueprint - Engineers' Day
echo ========================================================
echo   THE ARCHITECT'S BLUEPRINT - ENGINEERS' DAY
echo ========================================================
echo Starting local web server at http://localhost:8080 ...
start "" "http://localhost:8080"
py -m http.server 8080
pause
"""

paths = [
    r"C:\Users\pathr\OneDrive\Desktop\Engineers-Day-Blueprint\run.bat",
    r"C:\Users\pathr\.gemini\antigravity\scratch\engineers-day-blueprint\run.bat"
]

for p in paths:
    with open(p, "w", encoding="utf-8") as f:
        f.write(bat_content)
    print("Created", p)
