
pyinstaller --onefile -w main.py

copy dist\main.exe
rd /s /q build
del /s /q main.spec