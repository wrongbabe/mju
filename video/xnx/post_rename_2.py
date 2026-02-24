import os
import random
import string

def generate_random_string(length=5):
    """
    Generates a random alphanumeric string of a given length.
    Characters will be lowercase letters and digits.
    """
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# --- Configuration ---
folder_path = r'C:\Users\SOHAN-PC-08\Documents\New folder (19)'  # Change as needed

# --- Main Script ---
if not os.path.isdir(folder_path):
    print(f"Error: The folder was not found at the specified path.")
    print(f"Please check if this path is correct: {folder_path}")
else:
    files = os.listdir(folder_path)
    used_random_parts = set()
    renamed_count = 0

    print(f"Scanning for .html files in '{folder_path}'...")

    for filename in files:
        if filename.lower().endswith('.html'):
            name_part = filename[:-10]  # Removes "-xxxxx.html"
            if '-' in name_part:
                base_name = '-'.join(name_part.split('-')[:-1])  # Removes old random part
            else:
                base_name = name_part

            # Generate unique random suffix
            while True:
                random_part = generate_random_string(5)
                if random_part not in used_random_parts:
                    used_random_parts.add(random_part)
                    break

            new_name = f"{base_name}-{random_part}.html"
            source_path = os.path.join(folder_path, filename)
            destination_path = os.path.join(folder_path, new_name)

            try:
                os.rename(source_path, destination_path)
                print(f"Renamed: '{filename}' -> '{new_name}'")
                renamed_count += 1
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")

    # --- Final Report ---
    if renamed_count > 0:
        print(f"\nDone. Renamed {renamed_count} file(s).")
    else:
        print("\nNo .html files found to rename.")
