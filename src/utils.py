import hashlib

def hash_file(file_path):
    """Returns the SHA-256 hash of the specified file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
            return sha256.hexdigest()
    except (FileNotFoundError, PermissionError) as e:
        print(f"[ERROR] Unable to hash {file_path}: {e}")
        return None