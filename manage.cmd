@echo off
setlocal
call "C:\ProgramData\miniconda3\condabin\conda.bat" activate "%~dp0.conda"
python "%~dp0manage.py" %*
endlocal