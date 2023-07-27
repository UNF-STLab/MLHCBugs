# File Structure
```
root/
├── conda/
│   ├── config/     # Contains configuration files for conda environments, organized by package names.
│   ├── env/        # Directory to store conda environments. The "common" sub-directory holds non-persistent environments that are overwritten when recreated. Persistent environments use their own directories named as `<repo name>.<version>`.
├── docs/           # Documentation directory for project-related information and user guides.
├── repos/          # Stores downloaded repositories, each inside a subdirectory named after the package and/or repository.
├── test_scripts/   # Holds test scripts for the bugs, organized by package names.
├── index.json      # An index that lists all the example packages/repositories and their bugs.
├── main.ipynb      # Notebook-based framework for users who prefer interactive usage.
└── main.py         # Command-line framework for users who prefer script-based usage.
```

# Index Structure (index.json)

The `index.json` file is an essential component of the framework, serving as an organized index of repositories and related bugs. This JSON file follows a specific structure to store the necessary information for each package and its associated GitHub repositories and bugs. Please strictly follow the structure when adding new repositories and/or bugs.

## Structure Overview

The `index.json` file uses a nested JSON object to store information about each package. The top-level keys represent the package names, and their corresponding values are JSON objects containing the package's GitHub URL and an array of bug reports related to the package. An overview of the structure is shown below:

```
{
	<package name>: {
		"url": <GitHub URL>,
		"bugs": [
			{
				"title": <issue title followed by the issue number>,
				"version": <package release version or full commit hash from GitHub>
			},
			...
		]
	},
	...
}
```

## Explanation of Fields

1. **Package Name:** The top-level key in the JSON object is the name of the package. It serves as an identifier for each entry in the index.
2. **GitHub URL:** The `url` field within each package entry holds the corresponding GitHub URL where the package repository is hosted. The framework uses this URL to download the repository when a commit hash is given as version.
3. **Bugs:** The "bugs" field contains an array of bug reports associated with the package. Each bug is represented as a JSON object within the array. The framework will lists the bugs in the same order they are listed here. When adding new bugs, we recommend either to add them at the end  of the array or add them maintaining the incremental order of the issue numbers.
4. **Issue Title and Number:** The `title` field within each bug object stores the issue title, followed by the issue number. This combination provides a concise yet informative representation of the bug. The issue number must start with a hash sign (e.g. #123) and present at the end of the title. The framework uses the issue numbers to locate the Python test files.
5. **Version or Commit Hash:** The `version` field inside the bug object can store either the package release version or the full commit hash from GitHub. Package release versions must follow the version scheme outlined in PEP 440. The framework uses this information to install the specific version of the package that contains the bug.

> **Note**
> Bug id refers to the corresponding issue number in the GitHub repository. Bug number refers to the sequential order of specific bugs listed within each repository, with the first bug assigned the number 1, the second bug number 2, and so on. Bug index (`idx`) refers to the index of the bug in the `index.json` file. The bugs should be ordered in the ascending order of the issue ids. Therefore, bug index + 1 should be always equal to the bug number.
> 
> The script asks the user for bug numbers as the bug numbers are consecutive numbers and easier to remember over the issue numbers. Within the script the bugs are referenced using bug indices for programming convenience. However, the bug ids (i.e., issue numbers) are used to name the test files, as the bug numbers (also bug indices) may change upon adding new bugs.

# Conda Environment Configuration Files

## Structure Overview

The requirements for a package or repository changes over time. Thus, it is not possible to use a single Conda environment for all the bugs from a package or repository. Besides, multiple bugs can be from the same released version or commit and the requirement is exactly the same for all these bugs. Therefore, we define a Conda environment for each package version and commit that is listed for at least one bug. Please note that multiple version of the package or commits can have the exact same requirements but utilizing a single Conda environment for multiple versions and commits will require another index or translator and add another layer of complexity. Since, the config files has a small storage footprint, we decided to define an environment per version and commit. Hence, the Conda environments are named after the package name followed by the version or commit hash.

## Configuration Template

Conda environment configuration files must be formatted in YAML and must follow the following template:

```
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pip=20.0.2
  - nilearn
  - pip:
      - numpy==1.25.1
      - pandas>=1.3.0,<2.0.0,!=1.5.0rc0
install_repo: True
```

## Explanation of Fields

Under `channels`, list the repositories where conda should look for packages during the environment creation process. Under `dependencies`, first mention the python and pip version. If you want to install the package under test from a PyPI release, put the package name along with the specific version as a conda dependency like python or pip. If you want to install the package from the repository, then add the `install_repo` key and set it to True as shown in the template and the script will automatically install the repository using pip. The package under test may require additional packages and these packages should be listed as requirements under pip like numpy and pandas in the template. Please note that you should use a single equal sign (=) to specify the version in conda dependencies and double equal (==) in pip requirements. 

Each environment config file should include pip as a dependency. Pip is required to install dependencies mentioned under pip, if any, and the repository unless using a released version from PyPI or Conda. Unless a specific version of `pip` is required to reproduce the bug, use the `conda search` command to find the latest version of the `pip` for a given python version. When adding configuration for new bugs, we recommend listing the dependencies under `pip` as Conda often fails to resolve the environment. However, sometimes `pip` installs packages from source and throws errors when the package needs to be compiled before installation and the compilation fails. In such cases, check if Conda can install the package without any errors as Conda has a package repository of compiled wheel files and does not encounter build or compilation related errors.

# Python Test Script

The test scripts are organized under package names and files are named after the GitHub issue numbers. We have included test scripts for many bugs. If a bug does not have a test script and you want to add one, copy the test script to the package sub-directory, make sure the file is named after the issue number, and the framework will automatically detect and run the newly added script when you input `d` for `test_file`. If you want to run multiple test scripts, either combine them all into a single script or call the other scripts from this script. You may also store the callee scripts in the same directory as the caller script but the callee scripts must have a non-numerical postfix, e.g. `123a.py` or  `123-csi.py` where `123` is the issue number.