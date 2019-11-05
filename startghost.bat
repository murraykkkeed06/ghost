@echo off

@echo @echo off >> ghost.bat

@echo python %~dp0ghost.py >> ghost.bat

rem echo python ghost.py >> ghost.bat

copy ghost.bat C:\Python36\Scripts

copy ghost.bat c:\Python27\Scripts


del "ghost.bat" /s /f /q

cls

rem setx path "%PATH%;%~dp0" 

rem setx path "%PATH%; [filename] "
