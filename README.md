# smart-file-organizer
A Python script that automatically organizes download folders and sorts engineering files
Smart File Organizer for Engineering & Downloads

A Python automation script that keeps your `Downloads` folder completely spotless while automatically sorting engineering blueprints, documents, and project data to your Desktop.

✨ Features
- Intelligent Sorting:** Automatically organizes files by their extensions into distinct folders (PDFs, Images, Datasets, CAD, Revit, etc.).
- Engineering Hot-Lane:** Automatically scans filenames for industry keywords (`civil`, `structural`, `arup`, `detailing`) and routes them directly to a dedicated workspace folder on your Desktop.
- Recursive Safety Logic:** Uses recursive path checking (`.rglob`) to organize nested downloads while avoiding recursive infinite loops.
- No Overwrite Safety:** Smart renaming system automatically appends counters (e.g., `document(1).pdf`) if a file with the same name already exists in the target directory.
- Error Resilient:** Implements try-except blocks to catch corrupted or locked files without crashing the script execution.

## 🚀 How It Works
The script maps extensions out to specialized folders:
- CAD & Architecture:`.dwg`, `.dxf`, `.rvt`, `.rfa`, `.rte`
-Data & Calculations:`.xlsx`, `.csv`, `.ods`
- Media & Docs: PDFs, Word docs, Videos, Pictures, and Archives.

🛠️ Requirements & Installation
No external libraries are required! The script runs purely on Python's built-in standard library (`pathlib`, `shutil`, `os`).

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the folder:
   ```bash
   cd YOUR_REPO_NAME
   ```
3. Run the script:
   ```bash
   python organizer.py
   ```
