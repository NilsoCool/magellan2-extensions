# Automation Kit for ConsoleMerger

This kit provides a robust, Python-based automation solution for merging multiple Eressea report files (`.cr`) sequentially using the ConsoleMerger JAR.

## Components

*   `run_auto_merge.bat`: The entry point script (Double-click to run). Checks for Python and launches the main script.
*   `auto_merge.py`: The logic script. Handles file detection, sorting, and sequential merging.

## Prerequisites

1.  **Python 3.x**: Must be installed and available in your system PATH.
2.  **ConsoleMerger JAR**: The `consolemerger-for2.1.1.jar` must be present in the parent or root directory (or configured path).
3.  **Library Dependencies**: All Magellan libraries must be in a `lib/` folder.

## Setup

The JAR is located in `../release/consolemerger-for2.1.1.jar` and libs in `../libs_2.1.1/`. The script handles these paths automatically.

## Usage

1.  Place your unzipped `.cr` files into the `input/` folder.
2.  Double-click `run_auto_merge.bat`.
    *   The script automatically sorts files by **SIZE (Descending)**. The largest file is treated as the base.
    *   It merges all subsequent files into the base one by one.
3.  Wait for the "ALL MERGES COMPLETED SUCCESSFULLY" message.
4.  Collect your result in `output/merged_final.cr`.

## Troubleshooting

*   **Process hangs?** Ensure you are using ConsoleMerger v1.0.3+ which includes the `System.exit(0)` fix.
*   **Encoding issues?** The script forces UTF-8 encoding for logs.
