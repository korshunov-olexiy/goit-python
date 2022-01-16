@echo off

IF [%1] == [] (
  SET python_version="c:\Progra~1\Python39\python.exe"
) ELSE (
  SET python_version=%1
)

fsutil dirty query %systemdrive% > nul
IF NOT %ERRORLEVEL%==0 (
    echo The script is run with user rights. We get administrator rights...
    for /F "tokens=1,2 delims=0x" %%a in ('reg query "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v "ConsentPromptBehaviorAdmin"') do set uac=%%b
    IF NOT "%uac%"=="0" (
        rem Start batch again with UAC
        echo Set UAC = CreateObject^("Shell.Application"^) > "%~dp0getadmin.vbs"
        echo UAC.ShellExecute "%~s0", %python_version%, "%~dp0", "runas", 1 >> "%~dp0getadmin.vbs"
        "%~dp0getadmin.vbs"
        del "%~dp0getadmin.vbs"
        echo Re-run this script with administrative privileges.
      ) ELSE (
        echo UAC disabled on the system. Continued work is not possible.
    )
    exit /B
)

cd /D "%~dp0"

IF NOT EXIST "%~dp0env\Scripts\activate.bat" ( virtualenv -p %python_version% env)

echo "Activate virtual environment..."
CALL "%~dp0env\Scripts\activate.bat"
echo "Upgrade pip..."
python.exe -m pip install --upgrade pip

REM CHECK IF MODULE BUILD INSTALLED
python.exe -c "import build"
IF NOT %ERRORLEVEL%==0 (
  echo "Module 'build' not found. Try install..."
  python.exe -m pip install build
)

mkdir "%~dp0dist"
echo Try uninstall old version of package
pip uninstall personal-manager -y
python -m build
echo Check version of package from setup.cfg...
@REM setlocal EnableDelayedExpansion
for /F "tokens=1,2 delims== " %%a in ('findstr /r /C:"^version = [0-9]\.[0-9]*$" setup.cfg') do set version=%%b
echo Specific package version is: %version%

IF NOT EXIST "%~dp0dist\personal-manager-%version%.tar.gz" ( GOTO :EOF )
IF [%version%]==[] ( GOTO :EOF )
echo Install the package on the system
pip install "%~dp0dist\personal-manager-%version%.tar.gz"
echo Delete temporary directories
rmdir /S /Q "%~dp0dist"
rmdir /S /Q "%~dp0src\personal_manager.egg-info"
echo clear pip cache
pip cache purge
pause
@echo on
