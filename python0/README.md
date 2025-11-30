# PythonDataSiencePiscine
Data science piscine at 42

## Requirements
- Python 3.10.13
- Required packages: None (using only standard library)

## Setup
1. Install pyenv
2. Run `pyenv install 3.10.13`
3. In project directory, run `pyenv local 3.10.13`
4. Reload shell: `exec "$SHELL"`
5. Verify version: `python --version`

## Troubleshooting
If Python version is incorrect:
1. Add to ~/.bashrc:
   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init -)"
   ```
2. Reload shell: `exec "$SHELL"`

## Documentation
1. What is the package root?
   A: Project folder containing pyproject.toml (or setup.py), README, LICENSE, package dir(s) and tests.
2. 

## VS Code Setup
1. Create `.vscode/settings.json` in project root
2. Configure Python interpreter to use Python 3.10.13
3. Restart VS Code to apply changes

## setup.py configuration
# name="ft_package",
# version=get_version(),
# version="0.0.1",
# description="A small package to learn how to pack",
# package_dir={"": "ft_package"},
## packages=find_packages(),
# entry_points={
#     "console_scripts": [
#         "ft_package = ft_package.count_in_list.__main__:main",
#     ]
# },
# long_description=long_description,
# long_description_content_type="text/markdown",
# need this url format since toml will give a format different from this
# author="eseferi",
# author_email="eseferi@42.fr",
# license="MIT",
# license_files=["LICENSE"],
# classifiers=[
#     "License :: OSI Approved :: MIT License",
#     "Programming Language :: Python :: 3.10",
#     "Operating System :: OS Independent",
# ],
# install_requires=["ipython >= 8.37.0"],
# extras_require={
#     "dev": ["pytest>=7.0", "twine>=4.0.2"],
# },
# python_requires=">=3.10",