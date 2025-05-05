import os
from utils import hash_file

def scan_directory(path):
    """
    Recursively scan the given directory and return a dictionary mapping file paths to their SHA-256 hashes.
    """
    file_hashes = {}
    for root, _, files in os.walk(path):
        for filename in files:
            full_path = os.path.join(root, filename)
            file_hash = hash_file(full_path)
            if file_hash:
                file_hashes[full_path] = file_hash
    return file_hashes