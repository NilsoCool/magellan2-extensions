# PROJECT HIBERNATION MEMO

**Status:** HIBERNATED / RELEASED (v1.0.3)
**Date:** 31 Jan 2026

This project ("Magellan 2 Extensions") is currently stable and released.
The key component is `ConsoleMerger`, an automated report merger for Magellan/Eressea.

## 📂 Key Locations
*   **Source Code:** `src/magellan/ext/console/merge/`
*   **Production JAR:** `release/consolemerger-for2.1.1.jar`
*   **Automation Kit:** `automation_kit/` (Python scripts + batch launcher)

## 🚀 How to Resume
To restart development or apply a new update:

1.  **Git Pull:** Ensure you have the latest version.
    ```bash
    git pull origin master
    ```
2.  **Edit Code:** Modify Java files in `src/`.
3.  **Build:** Use Ant to compile.
    ```bash
    ant -f build.consolemerger.xml create-consolemerger
    ```
4.  **Test:** Use the `test-prod` folder (external to git) or create a new test env using `automation_kit`.
5.  **Release:** Copy the new JAR to `release/` and update `CHANGELOG.txt`.

## 📦 For New Installations
Simply use the content of `automation_kit/` and `release/` on any machine with Java 11+ and Python 3.x.
See `README.md` for details.
