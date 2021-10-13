from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Sort, rename and clean folder',
      url='https://github.com/korshunov-olexiy/goit-python/tree/main/module_6',
      author='AleXKaN',
      author_email='korshunov.olexiy@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={
          'console_scripts':
          ['clean-folder=clean_folder.clean:sort_dir']
      }
      )
