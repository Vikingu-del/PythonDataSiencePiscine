#!/bin/bash


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


# Move to package directory
cd "$PACKAGE_PATH" || exit 1


# Build package
echo "Building package: $PACKAGE_NAME..."
python -m build
# python setup.py bdist_wheel sdist # --- using setup.py
# python -m build


# Install package
echo "Installing package: $PACKAGE_NAME..."
pip install ./dist/ft_package-0.0.1.tar.gz
#pip install ./dist/ft_package-0.0.1-py3-none-any.whl
