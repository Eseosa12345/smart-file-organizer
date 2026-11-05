from pathlib import Path 
import os 
import shutil

# Establish the base home directory to ensure cross-platform compatibility (Mac/Windows/Linux)
h = Path.home()

# Mapping destination folders to their targeted file extensions
suffix_dict = {
    h / 'Downloads/Pdf': ['.pdf'],
    h / 'Downloads/Documents': ['.doc', '.docx', '.rtf', '.odt', '.txt'],
    h / 'Downloads/Books': ['.epub', '.mobi', '.azw3', '.fb2'],
    h / 'Downloads/Zip files': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    h / 'Downloads/Autocad files': ['.dwg', '.dxf'],
    h / 'Downloads/Revit files': ['.rvt', '.rfa', '.rte'],
    h / 'Downloads/Videos': ['.mkv', '.mp4', '.avi', '.mov', '.wmv', '.flv'],
    h / 'Downloads/Pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
    h / 'Downloads/Excel and CSV files ': ['.xlsx', '.xls', '.csv', '.ods', '.xlsm']
}

# Automatically generate all targeted destination subdirectories if they don't exist yet
for folder in suffix_dict.keys():
    folder.mkdir(exist_ok=True)

# Create a specialized project landing folder on the Desktop for engineering work
(h / 'Desktop/Engineering').mkdir(exist_ok=True)

# High-priority keywords used to intercept and redirect engineering-specific files
keywords = ['engineering', 'bs code', 'civil', 'steel', 'design', 'arup', 'concrete', 'structural', 'detailing']

# Global list to track files that failed to move (e.g., due to permission locks or corruption)
error_files = []

def file_organizer():
    # Recursively scan through the Downloads folder, including all nested subfolders
    for file_path in (h / 'Downloads').rglob('*'):
        print('Checking file:', file_path.name)
        
        # Guard Clause: Skip directories; we only want to process actual files
        if not file_path.is_file():
            continue
            
        # Safety Check: Prevent the script from processing files that are already inside 
        # our designated target folders, avoiding a destructive infinite processing loop.
        if any(target_folder in file_path.parents for target_folder in suffix_dict.keys()):
            continue

        # Evaluate the file against our extension rules
        for folder_path, extensions in suffix_dict.items():
            if file_path.suffix.lower() not in extensions:
                continue  # Skip to the next dictionary item if the extension doesn't match

            # Cache the original names to preserve the filename foundation during duplicate increments
            original_stem = file_path.stem
            original_suffix = file_path.suffix
            
            # Establish the default fallback path parameters
            destination_name = file_path.name
            target_directory = folder_path
            
            # Content Interception: Route file to Desktop if it matches professional keywords
            if any(word in file_path.name.lower() for word in keywords):
                target_directory = h / 'Desktop/Engineering'

            # Collision Handler: Append a counter (e.g., filename(1).pdf) if a file already exists
            count = 1
            while (target_directory / destination_name).exists():
                destination_name = f"{original_stem}({count}){original_suffix}"
                count += 1

            # Execution Layer: Safe file transfer wrapper
            try:
                shutil.move(str(file_path), str(target_directory / destination_name))
            except Exception as e:
                # Catch system errors (like open files or permission limits) without stopping the whole script
                print(f"Error moving {file_path.name}: {e}")
                error_files.append(file_path)

            break  # Break out of the extension matching loop once the file finds its home

# Standard Python entry point execution guard
if __name__ == '__main__':
    file_organizer()
    if error_files:
        print("\nFiles that encountered errors:")
        for f in error_files:
            print("-", f)
    else:
        print("\nDownloads folder successfully organized! 🚀")
