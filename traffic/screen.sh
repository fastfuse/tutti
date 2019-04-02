#! /bin/bash

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $SOURCE_DIR

source .venv/bin/activate

python traffic.py
