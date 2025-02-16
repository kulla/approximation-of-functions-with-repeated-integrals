#!/bin/sh

SCRIPT_DIR=$(dirname $(readlink -e "$0"))
NOTEBOOKS_DIR="$SCRIPT_DIR/notebooks"

mkdir -p "$NOTEBOOKS_DIR"

PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH}" jupyter lab "--notebook-dir=$NOTEBOOKS_DIR" "$@"
