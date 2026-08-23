"""
Task 4: Automate File Renaming in a Folder
A CLI-based Python script that automates bulk renaming of files in a selected directory.
It preserves the original file extensions, processes files in a sorted order, prevents
accidental file overwriting, and handles errors gracefully.
"""

import os
import sys

def rename_files(directory: str, prefix: str) -> None:
    """
    Renames all files in the given directory using the pattern: prefix_1.ext, prefix_2.ext, etc.
    Preserves original file extensions and handles conflicts/errors gracefully.
    """
    # 1. Verify directory exists
    if not os.path.exists(directory):
        print(f"\nError: The path '{directory}' does not exist. Please check the path and try again.")
        return
        
    # 2. Verify path is a directory
    if not os.path.isdir(directory):
        print(f"\nError: The path '{directory}' is not a directory.")
        return

    # 3. Retrieve directory contents
    try:
        items = os.listdir(directory)
    except PermissionError:
        print(f"\nError: Permission denied to access the directory '{directory}'.")
        return
    except Exception as e:
        print(f"\nError reading directory: {e}")
        return

    # 4. Filter out subdirectories, only keep files
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]

    # 5. Handle empty directory (no files)
    if not files:
        print(f"\nNotice: The directory '{directory}' contains no files (excluding subfolders). Nothing to rename.")
        return

    # 6. Process files in a predictable, sorted order
    files.sort()

    print(f"\nFound {len(files)} file(s) to process. Starting renaming...\n")
    print("-" * 60)
    
    success_count = 0
    skipped_count = 0
    error_count = 0

    for idx, filename in enumerate(files, start=1):
        old_filepath = os.path.join(directory, filename)
        
        # Preserve original file extension
        _, ext = os.path.splitext(filename)
        
        # Construct new filename and filepath
        new_filename = f"{prefix}_{idx}{ext}"
        new_filepath = os.path.join(directory, new_filename)

        # Case A: File is already named correctly (e.g. rerun scenario)
        if filename == new_filename:
            print(f"[Kept]     '{filename}' (Already correctly named)")
            success_count += 1
            continue

        # Case B: Avoid overwriting an existing file
        if os.path.exists(new_filepath):
            print(f"[Skipped]  '{filename}' -> '{new_filename}' (Error: Target file already exists)")
            skipped_count += 1
            continue

        # Case C: Perform rename with try-except block for error handling
        try:
            os.rename(old_filepath, new_filepath)
            print(f"[Renamed]  '{filename}' -> '{new_filename}'")
            success_count += 1
        except PermissionError:
            print(f"[Failed]   '{filename}' (Error: Permission denied)")
            error_count += 1
        except FileNotFoundError:
            print(f"[Failed]   '{filename}' (Error: Source file not found)")
            error_count += 1
        except Exception as e:
            print(f"[Failed]   '{filename}' (Error: {e})")
            error_count += 1

    # 7. Print execution summary
    print("-" * 60)
    print("Renaming Summary:")
    print(f"  Successfully processed: {success_count}")
    print(f"  Skipped (no overwrite): {skipped_count}")
    print(f"  Failed (errors):        {error_count}")
    print("-" * 60)

def main():
    """
    Main entry point for the CLI File Renamer application.
    Prompts the user for folder path and prefix, then initiates renaming.
    """
    print("=" * 60)
    print("           AUTOMATED FILE RENAMER UTILITY")
    print("=" * 60)

    # Prompt user for the folder path
    directory = input("Enter the path to the folder: ").strip()
    if not directory:
        print("Error: Folder path cannot be empty.")
        return

    # Prompt user for naming pattern prefix (with a default fallback)
    prefix = input("Enter the naming prefix (default: 'file'): ").strip()
    if not prefix:
        prefix = "file"

    rename_files(directory, prefix)

if __name__ == "__main__":
    main()
