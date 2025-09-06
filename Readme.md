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

## VS Code Setup
1. Create `.vscode/settings.json` in project root
2. Configure Python interpreter to use Python 3.10.13
3. Restart VS Code to apply changes
