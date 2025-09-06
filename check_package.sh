#!/bin/bash


# Set error handling
set -e

# Check if package name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <package_name>"
    echo "Example:"
    echo "  $0 ft_package                    # Clean package in current directory"
    echo "  $0 ft_package /path/to/package   # Clean package in specific path"
    exit 1
fi


PACKAGE_NAME=$1
PACKAGE_PATH=${2:-.}


# Check if directory exists
if [ ! -d "$PACKAGE_PATH" ]; then
    echo "Error: Directory $PACKAGE_PATH does not exist."
    exit 1
fi


# Check if tree command is available
if ! command -v tree &> /dev/null; then
    echo "Warning: 'tree' command not found. Installing..."
    sudo apt-get update -y
    sudo apt-get install -y tree
fi


# Move to package directory
cd "$PACKAGE_PATH" || exit 1


echo "=== Checking package: $PACKAGE_NAME structure ==="
echo "Directory Structure:"
tree -a --noreport

echo -e "\n=== Checking setup.py ==="
if [ -f "setup.py" ]; then
    echo "Package metadata:"
    python setup.py --name --version --description

    echo -e "\nPackage dependencies:"
    grep "install_requires" setup.py
    grep "extras_require" setup.py

    echo -e "\nPackage structure:"
    python -c "from setuptools import find_packages; print(find_packages())"

    echo -e "\nEntry points:"
    grep -A 5 "entry_points" setup.py
else
    echo "Error: setup.py not found in $PACKAGE_PATH."
    exit 1
fi

echo -e "\n=== Checking package import paths ==="
python -c "import sys; print('\n'.join(sys.path))"

echo -e "\n=== Running setup.py check ==="
required_packages=("docutils" "wheel" "twine")
for pkg in "${required_packages[@]}"; do
    if ! python -c "import $pkg" &> /dev/null; then
        echo "Installing missing package: $pkg"
        pip install "$pkg"
    fi
done
python setup.py check --strict --metadata --verbose

# Check README.md formatting directly
echo -e "\n=== Checking README.md format ==="
if [ -f "README.md" ]; then
    # Use python-markdown to check syntax
    python -c "import markdown; markdown.markdown(open('README.md').read())" 2>/dev/null \
        && echo "README.md format is valid" \
        || echo "README.md has formatting issues"
else
    echo "Warning: README.md not found"
fi

echo -e "\n=== Checking build distribution (dry-run) ==="
# Check if build module is installed
if ! python -c "import build" &> /dev/null; then
    echo "Installing build package..."
    pip install build
fi

# Run dry-run build check
python -m build --wheel --no-isolation --outdir /tmp/build_check . && \
    echo "Build check passed successfully" && \
    rm -rf /tmp/build_check || \
    echo "Build check failed"
    cd $HOME/pythonDataSience/ || exit 1
    # Running pip install with --dry-run --ignore-installed --verbose
    pip install --dry-run --ignore-installed --verbose $PACKAGE_PATH
    ./clean_package.sh "$PACKAGE_NAME" "$PACKAGE_PATH"



echo -e "\n=== Summary ==="
echo "Package Name: $PACKAGE_NAME"
echo "Package Path: $PACKAGE_PATH"
echo "Done checking package strucure and metadata."