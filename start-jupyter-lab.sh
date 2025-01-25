#!/bin/sh

SCRIPT_DIR=$(dirname "$0")
NOTEBOOKS_DIR="$SCRIPT_DIR/notebooks"

mkdir -p "$NOTEBOOKS_DIR"

jupyter lab "--notebook-dir=$NOTEBOOKS_DIR"
