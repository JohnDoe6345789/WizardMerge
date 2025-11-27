#!/usr/bin/env sh
# Install Python dependencies system-wide or in the active environment.
set -eu

PYTHON_BIN=${PYTHON_BIN:-python3}

"$PYTHON_BIN" -m pip install --upgrade pip
"$PYTHON_BIN" -m pip install -r requirements.txt
