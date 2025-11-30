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


# Unistall package
echo "Unistalling package: $PACKAGE_NAME..."
pip uninstall -y "$PACKAGE_NAME"


# Remove build artifacts
echo "Removing build artifacts..."
rm -rf build/ dist/ *.egg-info/


# Remove package cache
echo "Removing package cache..."
if [ -d "$PACKAGE_NAME" ]; then
    rm -rf "$PACKAGE_NAME/__pycache__/"
    rm -rf "$PACKAGE_NAME/*/__pycache__/"
fi


# Find and remove all __pycache__ directories recursively
echo "Removing all __pycache__ directories..."
find . -type d -name "__pycache__" -exec rm -rf {} +


echo "Cleanup completed for $PACKAGE_NAME."