# ==============================
# MAIN FILE — Run Entire Project
# ==============================

import subprocess
import sys

def run_script(script_name):
    print("\n==============================")
    print(f"Running {script_name}")
    print("==============================\n")
    subprocess.run([sys.executable, script_name])

if __name__ == "__main__":
    run_script("generate_data.py")
    run_script("preprocessing.py")
    run_script("regression_model.py")
    run_script("classification_model.py")
    run_script("recommendation_model.py")
    run_script("visualization.py")

    print("\n✅ ALL MODULES EXECUTED SUCCESSFULLY")
