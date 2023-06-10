#! /bin/sh

exec "${PYTHON:-python3}" -bb -Werror -Xdev "$(dirname "$(realpath "$0")")/__main__.py" "$@"

