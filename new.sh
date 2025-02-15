#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
NOTEBOOK_DIR="$SCRIPT_DIR/notebooks"
NOTEBOOK_TITLE="$@"

YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY=$(date +%d)

# Convert the input string to lowercase, replace spaces with hyphens, and trim
# leading/trailing spaces or hyphens.
FILENAME=$(echo "$NOTEBOOK_TITLE" | tr '[:upper:]' '[:lower:]' | tr -s ' ' '-' | sed 's/^[ \-]*//;s/[ \-]*$//')

# Define the notebook path
NOTEBOOK_PATH="$NOTEBOOK_DIR/$YEAR-$MONTH-$DAY-$FILENAME.ipynb"

# Create the new jupyter notebook
cp "$NOTEBOOK_DIR/template.ipynb" "$NOTEBOOK_PATH"

# Replace the placeholders in the notebook
sed -i "s/NOTEBOOK_TITLE/$NOTEBOOK_TITLE/g" "$NOTEBOOK_PATH"
sed -i "s/YEAR/$YEAR/g" "$NOTEBOOK_PATH"

# Open the jupyter notebook
./start-jupyter-lab.sh "$NOTEBOOK_PATH"
