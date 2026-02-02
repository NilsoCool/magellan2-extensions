# ConsoleMerger for Magellan 2.1.1

[![Version](https://img.shields.io/badge/version-1.0.3-blue.svg)](https://github.com/NilsoCool/magellan2-extensions)
[![Magellan](https://img.shields.io/badge/magellan-2.1.1-green.svg)](https://github.com/Magellan2/Magellan2)

Automated report merging tool for Magellan 2.1.1 / Eressea.
Now includes an **Automation Kit** for easy setup.

## 🚀 Quick Start

This project comes with an automated setup script.

1.  Download this repository.
2.  Go to the **`automation_kit`** folder.
3.  Run **`setup_environment.bat`**.

This script will automatically copy the necessary JARs and create this structure:
* `lib/` (Libraries)
* `input/` (Drop your .cr files here)
* `output/` (Merged files appear here)

4.  **Important**: Copy your `etc` and `rules` folders from your Magellan game directory into this folder.
5.  **Run**: Double-click `run_auto_merge.bat` to start merging.

## Manual Usage (Developers)
* **Production JAR**: Located in `release/`.
* **Source Code**: Located in `src/`.

---
[Report Issues](https://github.com/NilsoCool/magellan2-extensions/issues)
