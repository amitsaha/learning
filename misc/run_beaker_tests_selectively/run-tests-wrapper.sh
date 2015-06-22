#!/bin/bash
NOSEARGS=`./find_dir_changes ../`
if [[ "$NOSEARGS" != "No tests will be run" ]]; then
    ./run-tests.sh "$NOSEARGS"
else
    echo "No tests will be run"
fi
