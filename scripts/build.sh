#!/bin/bash

# Check for Python interpreter and use python3 if default python is not available
PYTHON_COMMAND=python
if ! command -v $PYTHON_COMMAND &> /dev/null
then
    PYTHON_COMMAND=python3
    if ! command -v $PYTHON_COMMAND &> /dev/null
    then
        echo "Python is not installed. Please install it and try again."
        exit 1
    fi
fi

# Remove the dist directory safely by checking its existence first
DIST_DIR="dist"
if [ -d "$DIST_DIR" ]; then
    echo "Removing existing $DIST_DIR directory"
    rm -rf $DIST_DIR
else
    echo "$DIST_DIR directory does not exist, so not removed."
fi

# Build the package
echo "Building package with $PYTHON_COMMAND..."
$PYTHON_COMMAND setup.py sdist bdist_wheel

echo "Build completed."
