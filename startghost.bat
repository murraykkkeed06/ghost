@echo off

@echo @echo off >> ghost.bat

@echo start /B python %~dp0ghost.py >> ghost.bat

@echo start /B python %~dp0shaped_window_test.py >> ghost.bat

@echo start /B python %~dp0shaped_window_ghost2.py >> ghost.bat

@echo start /B python %~dp0shaped_window_ghost3.py >> ghost.bat

@echo start /B python %~dp0shaped_window_ghost4.py >> ghost.bat

@echo start /B python %~dp0set_brightness.py >> ghost.bat

@echo start /B python %~dp0horror_sound.py >> ghost.bat

rem echo python ghost.py >> ghost.bat

copy ghost.bat C:\Python36\Scripts

copy ghost.bat c:\Python27\Scripts


del "ghost.bat" /s /f /q

pip install -r requirement.txt

rem cls

rem setx path "%PATH%;%~dp0" 

rem setx path "%PATH%; [filename] "
