import json
import os
from scanner import scan_directory

DB_PATH = "db.json"
TARGET_DIR = "C:/Users/Benjamin/Documents/watched_folder"

def load_database():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as db_file:
            try:
                return json.load(db_file)
            except json.JSONDecodeError:
                print("[!] Warning: db.json is corrupted or empty. Starting fresh.")
                return {}
    return {}

def save_database(data):
    with open(DB_PATH, "w") as db_file:
        json.dump(data, db_file, indent=4)

def compare_hashes(old, new):
    added = {f: h for f, h in new.items() if f not in old}
    removed = {f: h for f, h in old.items() if f not in new}
    modified = {f: h for f, h in new.items() if f in old and old[f] != h}

    return added, removed, modified

def main():
    print("[*] Starting file integrity scan...")
    previous_hashes = load_database()
    current_hashes = scan_directory(TARGET_DIR)

    added, removed, modified = compare_hashes(previous_hashes, current_hashes)

    if not added and not removed and not modified:
        print("[+] No changes detected.")
    else:
        if added:
            print("[+] New files detected:")
            for f in added:
                print(f" +{f}")
        if removed:
            print("[-] Files removed:")
            for f in removed:
                print(f" - {f}")
        if modified:
            print("[!] Modified files:")
            for f in modified:
                print(f" * {f}")
    
    save_database(current_hashes)
    print("[*] Scan complete. Database updated.")

if __name__ == "__main__":
    main()