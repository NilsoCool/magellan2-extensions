# -*- coding: utf-8 -*-
import os
import glob
import subprocess
import shutil
import datetime
import sys

# ==========================================================
# CONFIGURATION
# ==========================================================
ROOT = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(ROOT, 'input')
OUTPUT_DIR = os.path.join(ROOT, 'output')
TEMP_DIR = os.path.join(ROOT, 'temp') # Isolated Temp Folder
LOG_DIR = os.path.join(ROOT, 'logs')
LIB_DIR = os.path.join(ROOT, '..', 'libs_2.1.1')
JAR_PATH = os.path.join(ROOT, '..', 'release', 'consolemerger-for2.1.1.jar')

# ==========================================================
# LOGGING SETUP
# ==========================================================
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(LOG_DIR, f"merge_session_{timestamp}.log")

def log(message, console=True):
    """Log to file and optionally console."""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")
    if console:
        print(message)

# ==========================================================
# MAIN LOGIC
# ==========================================================
def main():
    log("========================================================")
    log(f" AUTO MERGE SESSION STARTED at {datetime.datetime.now()}")
    log("========================================================")

    # 1. Setup Directories
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Ensure clean TEMP dir
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR)

    # 2. Get Files (CR ONLY as requested)
    files = glob.glob(os.path.join(INPUT_DIR, "*.cr"))
    
    # Filter out any files that might be in temp if regex failed (safety check)
    files = [f for f in files if TEMP_DIR not in os.path.abspath(f)]
    
    if len(files) < 2:
        log(f"[ERROR] Need at least 2 .cr files in '{INPUT_DIR}' to merge.")
        log(f"Found: {len(files)}")
        input("Press Enter to exit...")
        sys.exit(1)

    # 3. Sort by Size (Descending)
    # This ensures the largest file (likely the base) is processed first
    files.sort(key=lambda x: os.path.getsize(x), reverse=True)

    log(f"Found {len(files)} files to merge (Sorted by Size DESC).")
    for f in files:
        log(f" - {os.path.basename(f)} ({os.path.getsize(f)} bytes)")

    # 4. Build Classpath
    if not os.path.exists(LIB_DIR):
        log(f"[ERROR] '{LIB_DIR}' not found.")
        input("Press Enter to exit...")
        sys.exit(1)

    classpath_jars = [os.path.abspath(JAR_PATH)] + glob.glob(os.path.join(LIB_DIR, "*.jar"))
    classpath = ";".join(classpath_jars)

    # 5. Merge Loop
    current_base = None
    temp_base = os.path.join(TEMP_DIR, "working_base.cr")
    temp_merged = os.path.join(TEMP_DIR, "working_merged.cr")

    for i, file_path in enumerate(files):
        filename = os.path.basename(file_path)

        if current_base is None:
            # First file is just copied as the starting base
            log(f"\n[INIT] Base: {filename}")
            shutil.copy2(file_path, temp_base)
            current_base = temp_base
        else:
            # Subsequent files are merged into the base
            log(f"\n--------------------------------------------------------")
            log(f"[MERGE #{i}] Adding '{filename}'...")
            
            # Construct Java Command
            cmd = [
                "java", 
                "-cp", classpath,
                "magellan.ext.console.merge.ConsoleMerger",
                os.path.abspath(os.path.join(ROOT, '..')),
                current_base,
                file_path,
                temp_merged
            ]

            try:
                # Run Java Process
                process = subprocess.Popen(
                    cmd, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,
                    encoding='utf-8', 
                    errors='replace'
                )

                for line in process.stdout:
                    line = line.rstrip()
                    print(line)
                    with open(log_file, "a", encoding="utf-8") as f:
                        f.write(line + "\n")
                
                process.wait()

                if process.returncode != 0:
                    log(f"[CRITICAL ERROR] Merge failed for file: {filename}")
                    sys.exit(1)
                
                # Success: Move merged result to be the new working base
                if os.path.exists(temp_merged):
                    shutil.move(temp_merged, temp_base)
                    log(f"[SUCCESS] Merge #{i} complete.")
                else:
                    log(f"[ERROR] Output file not created: {temp_merged}")
                    sys.exit(1)

            except Exception as e:
                log(f"[EXCEPTION] {str(e)}")
                sys.exit(1)

    # 6. Finalize
    final_name = "merged_final.cr"
    final_path = os.path.join(OUTPUT_DIR, final_name)
    
    if os.path.exists(temp_base):
        if os.path.exists(final_path):
            os.remove(final_path)
        shutil.move(temp_base, final_path)
    
    # Clean Temp
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    
    log("\n========================================================")
    log(" ALL MERGES COMPLETED SUCCESSFULLY")
    log(f" Final Output: {final_path}")
    log("========================================================")
    
    input("Done! Press Enter to close.")

if __name__ == "__main__":
    main()
