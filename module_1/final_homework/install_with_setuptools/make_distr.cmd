REM MANUAL: https://packaging.python.org/en/latest/tutorials/packaging-projects/
del /Q /S .\dist\personal_manager.egg-info\*
del /S .\dist\personal_manager-0.7.tar.gz
pip uninstall personal-manager -y
python setup.py sdist
pip install .\dist\personal_manager-0.7.tar.gz
