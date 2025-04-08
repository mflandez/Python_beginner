#!/usr/bin/env bash

# PDF Merger Script Runner
# Usage: ./auto_script.sh [file1.pdf] [file2.pdf]

SCRIPT_DIR="/d/Python_projects/Basic_projects/pdf_merger"
PY_SCRIPT="pdf_merger.py"
OUTPUT_FILE="combined.pdf"

# Change to the script directory
if ! cd "$SCRIPT_DIR"; then
    echo "Error: Failed to change to directory $SCRIPT_DIR" >&2
    exit 1
fi

# Check if Python script exists
if [ ! -f "$PY_SCRIPT" ]; then
    echo "Error: Python script $PY_SCRIPT not found" >&2
    exit 1
fi

# Run the merger with arguments if provided
if [ $# -eq 0 ]; then
    echo "Merging all PDFs in directory..."
    python "$PY_SCRIPT"
else
    echo "Merging specified PDFs: $*"
    python "$PY_SCRIPT" "$@"
fi

# Check if output was created
if [ -f "$OUTPUT_FILE" ]; then
    echo "Success: Output file created at $SCRIPT_DIR/$OUTPUT_FILE"
else
    echo "Warning: No output file was created" >&2
    exit 1
fi