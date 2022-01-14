@echo off

REM CHECK IF MODULE PYLINT INSTALLED
python -c "import pylint"
IF %ERRORLEVEL% NEQ 0 (
  echo "Module 'pylint' not found. Try install..."
  python -m pip install pylint
)

REM CREATE classes.dot for dot tool (include into graphviz) by package name
pyreverse personal_manager/
dot -Tpng classes.dot -o personal_manager_uml.png

@echo on
