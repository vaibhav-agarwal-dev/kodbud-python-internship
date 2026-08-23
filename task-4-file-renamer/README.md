# Task 4: Automate File Renaming in a Folder

A beginner-friendly, robust CLI-based Python script that automates the bulk renaming of files in a selected directory. This script utilizes Python's built-in `os` module for filesystem operations, ensuring a clean and library-free implementation.

---

## 🌟 Features

1. **Custom Prefix Patterns**: Allows users to specify a prefix (e.g., `document`, `photo`, `file`) to generate structured names like `prefix_1.txt`, `prefix_2.txt`, etc.
2. **Predictable Ordering**: Files are processed in alphabetical order (`sorted` sequence) before being renamed.
3. **Extension Preservation**: Safely extracts and preserves the original file extension of each file.
4. **Collision Prevention**: Checks for naming conflicts before performing the rename. If a file with the target name already exists, the rename is skipped to prevent accidental overwrites.
5. **Directory Safe**: Does not touch, rename, or traverse subdirectories.
6. **Graceful Error Handling**: Handles non-existent directories, empty folders, permission restrictions, and file access errors gracefully.
7. **Clean Summary Log**: Displays the old name, new name, and a final summary showing successful, skipped, and failed count.

---

## 📋 Requirements

* Python 3.x
* No external libraries (uses Python standard library modules `os` and `sys`)

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the task directory:
   ```bash
   cd task-4-file-renamer
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Follow the interactive CLI prompts:
   - **Folder Path**: Enter the absolute or relative path to the folder containing files you wish to rename.
   - **Naming Prefix**: Enter the word you want to prefix your files with (defaults to `file` if left blank).

---

## 📝 Example

### 1. Folder Setup Before Execution
Suppose you have a directory named `my_documents` with the following structure:
```text
my_documents/
│
├── notes.txt
├── report.docx
├── invoice.pdf
└── archive_folder/  <-- (Subdirectory; will not be renamed)
```

### 2. Execution Run
```text
============================================================
           AUTOMATED FILE RENAMER UTILITY
============================================================
Enter the path to the folder: C:\Users\Username\Desktop\my_documents
Enter the naming prefix (default: 'file'): document

Found 3 file(s) to process. Starting renaming...

------------------------------------------------------------
[Renamed]  'invoice.pdf' -> 'document_1.pdf'
[Renamed]  'notes.txt' -> 'document_2.txt'
[Renamed]  'report.docx' -> 'document_3.docx'
------------------------------------------------------------
Renaming Summary:
  Successfully processed: 3
  Skipped (no overwrite): 0
  Failed (errors):        0
------------------------------------------------------------
```

### 3. Folder Setup After Execution
```text
my_documents/
│
├── document_1.pdf
├── document_2.txt
├── document_3.docx
└── archive_folder/  <-- (Untouched subdirectory)
```
