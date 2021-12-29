@echo off
REM MANUAL: https://packaging.python.org/en/latest/tutorials/packaging-projects/

IF "%VIRTUAL_ENV%" == "" (
  echo "Virtual environment not activated. Try activate..."
  .\env\Scripts\activate.bat
)

IF %ERRORLEVEL% NEQ 0 (
  echo "Virtual environment not found in 'env' directory. Try configure..."
  python -m venv env
  echo "Upgrade pip..."
  python.exe -m pip install --upgrade pip
)

REM CHECK IF MODULE BUILD INSTALLED
python -c "import build"
IF %ERRORLEVEL% NEQ 0 (
  echo "Module 'build' not found. Try install..."
  python -m pip install build
)

mkdir dist
REM try uninstall old version of package
pip uninstall personal-manager -y
python -m build
REM install package
pip install .\dist\personal-manager-0.7.tar.gz
REM delete temporary directories
rmdir /S /Q .\dist
rmdir /S /Q .\src\personal_manager.egg-info
REM clear pip cache
pip cache purge

@echo on
