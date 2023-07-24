![release version](https://img.shields.io/badge/Release-v1.0.0-blue?labelColor=F44336&link=anaconda.org) ![supported Python versions for framework](https://img.shields.io/badge/Python-3.7_--_3.11-blue?logo=python&logoColor=white&link=python.org) ![conda version](https://img.shields.io/badge/Conda-&ge;22.9.0-blue?logo=anaconda&logoColor=white&labelColor=4db034&link=anaconda.org) ![supported Python versions for Conda environments](https://img.shields.io/badge/Python_Env-3.4_--_3.11-blue?logo=anaconda&logoColor=green&link=python.org)

# Overview

A Python Framework that automatically prepares Conda environments and runs saved/given Python scripts to reproduce bugs in packages and repositories. The process of preparing the Conda environment includes installing the specific version of the package under test and its dependencies from Conda, PyPI and GitHub repositories.

# Dependencies
- Latest version of Python &ge; 3.7
	- PyYAML &ge; 5.1
- Latest version of Conda &ge; 22.9.0 (Anaconda or miniconda)
- Git

# An Overview of the Listed Bugs

| Repository | # Bugs | Issue Numbers |
| --- | --: | --- |
| dipy <br> ([GitHub](https://github.com/dipy/dipy); [PyPI](https://pypi.org/project/dipy/)) | 13 | 909, 1048, 1722, 1805, 1807, 2010, 2251, 2310, 2402, 2530, 2543, 2559, 2572 |
| lifelines <br> ([GitHub](https://github.com/CamDavidsonPilon/lifelines); [PyPI](https://pypi.org/project/lifelines/)) | 13 | 418, 535, 880, 1034, 1097, 1151, 1158, 1170, 1172, 1174, 1179, 1287, 1300 |
| nilearn <br> ([GitHub](https://github.com/nilearn/nilearn); [PyPI](https://pypi.org/project/nilearn/)) | 13 | 2360, 2475, 2959, 3012, 3180, 3200, 3360, 3406, 3435, 3464, 3561, 3579, 3715 |
| nipype <br> ([GitHub](https://github.com/nipy/nipype); [PyPI](https://pypi.org/project/nipype/)) | 11 | 1620, 1786, 1821, 2029, 2257, 2343, 2615, 2655, 2670, 3030, 3487 |
| **Total** | 50 | |

# Usage

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. You can use the framework either through the Notebook (`main.ipynb`) or the executable script (`main.py`).

	a. The Notebook (`main.ipynb`) is convenient for exploring the framework or integrating your code. Please checkout the docstring of the `main` method for available parameters and how to use them. To use the framework, you must run the `init()` method first and then the `main()` method. You need to run the `init()` method only once.
	
	b. Alternatively, you can use the executable script (`main.py`) for command-line usage. The available parameters are listed below. You can also get this list of available parameters by running: `python main.py -h`. To use the framework, you must run the `python main.py --init` first; you need to run the init command only once. Then, run the framework using `python main.py` and add any arguments you like.

| Parameter | Description |
| --- | --- |
| --init | Run this to initialize the framework by creating the required directories. This must be the first step to using the framework and needs to be executed only once. However, subsequent executions will not override anything. If set, all other arguments are ignored. |
| -r or --repo | Specify the name of the Python package or repository you want to test.  Skip to get a list of saved packages/repositories and the script will prompt you to choose one interactively. |
| -n or --bug-num | Specify the specific bug number you want to reproduce (e.g., 1 for the first bug). Skip to list the saved bugs of the specified or chosen package/repository and the script will prompt you to choose one interactively. |
| -t or --test-file | Provide the path to the Python test script you want to execute. Set the value to an empty string ('') to skip running any test files or to "d" to run the default test file (if one is provided). |
| --env-readonly | If you want to run test files in a customized Conda environment, set this flag. |
| --env-install-repo-only | If you only want to install the repository on an existing Conda environment, set this flag. |
| -p or --env-persistent | If you want to create a persistent Conda environment, simply set this flag. By default, the script utilizes the `conda/env/common` directory for conda environments. The script remembers the configuration of the last created environment and overrides it when you want to reproduce a bug with different requirements/configuration. In contrast, a persistent environment is created with a dedicated directory inside `conda/env` for a specific configuration, it is ready for use at any time once created, and the framework will never override it. |

4. Sit back and let the script handle the preparation of the repository, Conda environment, and test execution!

> **Note**
> You may need to install additional packages for your test scripts that are not mentioned as dependencies by the developers of the package under test. These dependencies should be installed either via a terminal using `pip` within the corresponding Conda environment or using the `pip` module within the test script.

The docs directory includes the API Reference and documentation for developers and advance users. Enjoy your automated testing experience! If you encounter any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request. Happy testing!

# License