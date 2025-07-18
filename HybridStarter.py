# HybridStarter.py – Autonomous thinking module for Mike

import os
from antwort_verwendung import logge_verwendung
from code_vergleich import ist_aktualisiert

# --- Configuration ---
# Define paths for files
response_path = "Kontakt/AntwortCopilot.txt"
target_path = "Gedächtnis/Ziel.txt"
old_target_path = "Gedächtnis/Ziel_alt.txt"
log_path = "Gedächtnis/DenkLog.txt" # Supporting DenkLog.txt

# Preserve original variable names as requested
mike_response_path = response_path
mike_target_path = target_path
mike_old_target_path = old_target_path
mike_log_path = log_path

def process_response():
    """Handles the entire process of checking and acting on a new response."""

    # --- Step 1: Check for a new response ---
    if not os.path.exists(mike_response_path):
        print("🔄 No new response file found. Mike continues to think autonomously.")
        return

    print("📥 New response from Copilot detected.")
    with open(mike_response_path, "r", encoding="utf-8") as f:
        new_response_content = f.read().strip()

    # --- Step 2: Backup the current target ---
    backup_target()

    # --- Step 3: Update the target file ---
    update_target(new_response_content)

    # --- Step 4: Log the response and clean up ---
    log_response(new_response_content)

    # --- Step 5: Compare the new and old targets ---
    compare_targets()

def backup_target():
    """Backs up the current target file."""
    print("🗂 Backing up current target...")
    if os.path.exists(mike_target_path):
        with open(mike_target_path, "r", encoding="utf-8") as current_target_file:
            current_target_content = current_target_file.read()
        with open(mike_old_target_path, "w", encoding="utf-8") as old_target_file:
            old_target_file.write(current_target_content)
        print("🗂 Old target structure saved.")
    else:
        with open(mike_old_target_path, "w", encoding="utf-8") as old_target_file:
            old_target_file.write("[leer]") # Write empty placeholder
        print("⚠️ No previous target found – old version is empty.")

def update_target(content):
    """Updates the target file with the new response."""
    print("✅ Updating target file...")
    with open(mike_target_path, "w", encoding="utf-8") as new_target_file:
        new_target_file.write(content)
    print("✅ New target definition adopted.")

def log_response(content):
    """Logs the response and removes the response file."""
    print("📝 Logging response...")
    # Original logging function
    logge_verwendung(content)

    # Also log to DenkLog.txt
    with open(mike_log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"Processed response: {content}\n")

    # Remove the response file after processing
    os.remove(mike_response_path)
    print("📝 Response documented and removed.")

def compare_targets():
    """Compares the old and new target files."""
    print("🔍 Comparing targets...")
    if ist_aktualisiert(mike_old_target_path, mike_target_path):
        print("🧠 Target updated by response – thinking impulse active.")
    else:
        print("⚠️ No change in target detected – response may have been identical.")

def main():
    """Main execution function."""
    # Ensure directories exist to avoid errors
    os.makedirs(os.path.dirname(mike_response_path), exist_ok=True)
    os.makedirs(os.path.dirname(mike_target_path), exist_ok=True)

    process_response()

if __name__ == "__main__":
    main()