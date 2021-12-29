REM MANUAL: https://packaging.python.org/en/latest/tutorials/packaging-projects/
mkdir dist
REM uninstall package
pip uninstall personal-manager -y
python -m build
REM install package
pip install .\dist\personal-manager-0.7.tar.gz
REM delete temporary directories
rmdir /S /Q .\dist
rmdir /S /Q .\src\personal_manager.egg-info
REM clear pip cache
pip cache purge
