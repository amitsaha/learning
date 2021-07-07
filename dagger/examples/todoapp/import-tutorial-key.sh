#!/bin/bash

set -eu

KEY_FILE="$HOME/.config/dagger/keys.txt"
mkdir -p "$(dirname "${KEY_FILE}")"

# check if dagger is already initialized
[ -f "$KEY_FILE" ] || {
    # Any dagger command inits the default key
    dagger help >/dev/null
}

# Check if the key has been already set
grep -q \
    age1gunf55cd2v30j76w4arxgmzks48v2a56pdw0vtn2j2ax6q2yp3wqgqlzxm \
    "$KEY_FILE" 2>/dev/null && {
        echo "Key already initialized"
        exit 0
    }

cat >> "$KEY_FILE" <<- EOF
# dagger/examples
# public key: age1gunf55cd2v30j76w4arxgmzks48v2a56pdw0vtn2j2ax6q2yp3wqgqlzxm
AGE-SECRET-KEY-1E7U8T98V5JTS7CWEWC6CN2A4ZP0H2SE3UTTQV4WZZ8JW26JC23GSEK76PG
EOF

echo "Key initialized"
