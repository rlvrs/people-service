# Movies Service
I started this project to grasp the Python best practices
in order to build a Continuous Integration pipeline.

This project holds a dummy service that registers the information about movies received
from other services, such as web scrapping services.

## IDE Configuration
I used Pycharm to setup the environment. Since, I am using pytest, I need to configure Pycharm accordingly.

By default, the suggested default test runner is unittest.
So, to utilize pytest, you need to make it the default test runner first as follows:
1. Open the Settings/Preferences | Tools | Python Integrated Tools settings dialog.
2. In the Default test runner field select pytest.
3. Click OK to save the settings.

### This project is using:
 - **Setuptools**: for packaging purposes.
 - **PyTest**: for testing purposes.
 - **Tox**: to execute the tests with different Python versions.
 - **Pipenv**: to install and manage Python package dependencies.
 - **Makefile**: to automate the execution of simple tasks.

### Deps
 - pytest       # Test framework.
 - pytest-mock  # Thin-wrapper around the mock package for easier use with py.test.
 - pytest-cov   # Coverage plugin for pytest.
 - codecov      # Tool for measuring code coverage of Python programs
 - pytest-xdist # Pytest distributed testing plugin.
 - flake8       # PEP 8 linter.
 - tox          # Test with multiple versions of Python.
 - detox        # Tox with parallelism. (not currently working)