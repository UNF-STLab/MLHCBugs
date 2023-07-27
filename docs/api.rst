
API
***

**main.clone_repo(name: str, url: str, commit_id: str) -> None**

   Clones a remote Git repository and checks out a specific commit.

   Arguments:
      name (str): The name of the repository. This name will be used to create the local directory inside which the repository will be cloned.
      url (str): The URL of the remote Git repository to clone.
      commit_id (str): The ID of the commit to check out after cloning.

**main.init() -> None**

   Initializes the framework by creating the required directories. This method must be
   executed before the main method to using the framework. This method needs to be
   executed only once. However, subsequent executions will not override anything.

**main.main(repo: str | None = None, bug_num: int | None = None, test_file: str | None = None, env_readonly: bool = False, env_install_repo_only: bool = False, env_persistent: bool = False) -> None**

   Automatically prepares Conda environments and runs saved/given Python scripts to reproduce bugs in packages
   and repositories. The process of preparing the Conda environment includes installing the specific version
   of the package under test and its dependencies from Conda, PyPI and GitHub repositories.

   Arguments:
      repo (str, optional): The name of the repository or Python package under test. If not provided, the repositories will be listed and the user will be prompted to choose one.
      bug_num (int, optional): The specific bug number you want to replicate where 1 indicates the first bug. The bug number corresponds to the sequential order of the bugs listed for the chosen repository. If not provided, the bugs will be listed and the user will be prompted to choose one.
      test_file (str, optional): The path to the Python test script to execute. If not provided or set to None, the user will be prompted. If set to an empty string (‘’), skips running any test files. If set to ‘d’, runs the default test file (if one exists). Defaults to None.
      env_readonly (bool, optional): If True, the conda environment will be set to read-only mode. This can be handy to run test files in a customized conda environment. Defaults to False.
      env_install_repo_only (bool, optional): If True, only installs the repository on the existing conda environment. Defaults to False.
      env_persistent (bool, optional): If True, creates a persistent conda environment in a dedicated directory. Otherwise, creates and overrides the conda environment in the “common” directory. Defaults to False.

**main.prepare_conda_env(env_path: str, repo: str, version: str, install_repo_only: bool = False) -> bool**

   Prepares a conda environment and/or installs the repository as a dependency in the created or existing environment.

   Arguments:
      env_path (str): The path where the conda environment will be created.
      repo (str): The name of the repository or Python package under test.
      version (str): The version of the Python package (must follow the version scheme outlined in PEP 440) or the commit id (full hash) of the repository.
      install_repo_only (bool, optional): If True, only installs the repository on the existing conda environment. Defaults to False.

   Returns:
      bool: True if all operations are successful; otherwise, False or None.

**main.run_command(command: str | List[str], *, env: str | None = None, **other_run_kwargs) -> CompletedProcess**

   Runs command in the environment of the current process or a conda environment.

   Arguments:
      command (Union[str, List[str]]): The command to execute.
      env (str, optional): The path to the conda environment to use.

**main.run_test(env_path: str, test_file: str) -> None**

   Runs a Python test file using a conda environment.

   Arguments:
      env_path (str): The path to the conda environment to use.
      test_file (str): The path to the Python test file to execute.

-----------

.. |copy| unicode:: U+000A9 .. COPYRIGHT SIGN
   :ltrim:

|copy| Copyright 2023, Nazmul Kazi.

Built with Sphinx.