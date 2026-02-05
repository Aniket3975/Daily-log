# Learning Objective:
# This script teaches you how to build a basic file organizer in Python.
# You will learn to:
# 1. Use the 'pathlib' module for modern, object-oriented file path manipulation.
# 2. Define custom rules (keywords and file extensions) to categorize files.
# 3. Create directories and move files programmatically using 'shutil'.
# 4. Implement a clean, modular structure with functions and a main execution block.
# 5. Handle common scenarios like uncategorized files and existing directories.

import pathlib
import shutil
from typing import Dict

# --- Configuration Section ---
# These are the settings you can easily change to customize the script's behavior.

# Define the source directory where your unorganized files are located.
# We use pathlib.Path to create a Path object, which is more powerful than
# simple strings for path manipulation and ensures platform-independent paths.
# pathlib.Path('.') refers to the current working directory where the script is run.
# You can change this to a specific path, e.g., pathlib.Path('/Users/YourName/Downloads')
SOURCE_DIRECTORY = pathlib.Path('./unorganized_files')

# Define the base directory where the organized category folders will be created.
# This will be the parent directory for 'Documents', 'Images', 'Videos', etc.
DESTINATION_BASE_DIRECTORY = pathlib.Path('./organized_output')

# Define the category rules.
# This is a dictionary where keys are criteria (file extensions or keywords)
# and values are the names of the destination folders.
# The script will try to match files based on these rules.
#
# IMPORTANT NOTES on CATEGORIES:
# - Keys starting with '.' are treated as file extensions (e.g., '.pdf').
# - Other keys are treated as keywords that should appear in the filename (case-insensitive).
# - The order matters: The script checks for extension matches FIRST, then keyword matches.
#   Within each type (extensions, then keywords), the first rule encountered in the dictionary
#   that matches the file will be applied.
# - If no rule matches, files will go into an 'Other' category.
CATEGORIES: Dict[str, str] = {
    # Document types (matched by file extension)
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.rtf': 'Documents',

    # Keyword-based categories (matched by keywords in the filename)
    'report': 'Reports',     # Files with 'report' in their name (e.g., 'final_report.pdf')
    'invoice': 'Bills',      # Files with 'invoice' in their name (e.g., 'client_invoice.xlsx')
    'resume': 'Career',      # Files with 'resume' in their name (e.g., 'john_doe_resume.pdf')
    'project': 'Projects',   # Files with 'project' in their name

    # Image types
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.svg': 'Images',

    # Video types
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',

    # Audio types
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.flac': 'Audio',

    # Compressed archives
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.7z': 'Archives',

    # Spreadsheets
    '.xls': 'Spreadsheets',
    '.xlsx': 'Spreadsheets',
    '.csv': 'Spreadsheets',

    # Presentations
    '.ppt': 'Presentations',
    '.pptx': 'Presentations',
}

# Define a default category for files that don't match any of the above rules.
UNCATEGORIZED_FOLDER = 'Other'


# --- Core Logic Functions ---

def get_destination_category(file_path: pathlib.Path, categories: Dict[str, str]) -> str:
    """
    Determines the category folder name for a given file based on the defined rules.

    This function implements the "intelligence" of our organizer by matching file
    properties (extension or filename keywords) against the CATEGORIES dictionary.

    Args:
        file_path (pathlib.Path): The Path object of the file to categorize.
        categories (Dict[str, str]): A dictionary of categorization rules.

    Returns:
        str: The name of the category folder (e.g., 'Documents', 'Images').
             Returns UNCATEGORIZED_FOLDER if no rule matches.
    """
    # Get the file extension (e.g., '.pdf', '.jpg'). We convert to lowercase
    # to make matches case-insensitive and more robust.
    file_extension = file_path.suffix.lower()
    # Get the filename without extension (the 'stem'), also converted to lowercase
    # for case-insensitive keyword matching.
    file_name_stem_lower = file_path.stem.lower()

    # Strategy for determining category:
    # 1. Prioritize extension matches: If a file has a specific extension, that rule wins first.
    # 2. Then, check for keyword matches within the filename.
    # The first rule that matches in this order will determine the category.

    # 1. Check for extension-based categories
    if file_extension in categories:
        # If the file's extension is a key in our categories dictionary,
        # we found a match! Return the corresponding folder name.
        return categories[file_extension]

    # 2. Check for keyword-based categories in the filename
    # We iterate through the category rules to find a keyword match.
    for keyword, folder_name in categories.items():
        # Only process keys that are not file extensions (i.e., don't start with '.')
        if not keyword.startswith('.') and keyword in file_name_stem_lower:
            # If this keyword is found within the file's name (stem),
            # return its associated folder name.
            return folder_name

    # If neither extension nor keyword rules matched, return the default
    # uncategorized folder name.
    return UNCATEGORIZED_FOLDER


def organize_file(
    file_path: pathlib.Path,
    categories: Dict[str, str],
    destination_base_dir: pathlib.Path
) -> None:
    """
    Moves a single file to its determined category folder.

    This function handles the physical movement of files on your system.

    Args:
        file_path (pathlib.Path): The Path object of the file to organize.
        categories (Dict[str, str]): The dictionary of categorization rules.
        destination_base_dir (pathlib.Path): The root directory for organized files.
    """
    # First, figure out which category folder this specific file belongs to.
    category_name = get_destination_category(file_path, categories)

    # Construct the full path for the destination category folder.
    # pathlib.Path objects allow easy joining of paths using the '/' operator.
    # Example: './organized_output' / 'Documents' -> './organized_output/Documents'
    target_category_dir = destination_base_dir / category_name

    # Create the destination category folder if it doesn't already exist.
    # 'parents=True' ensures that any necessary parent directories are also created.
    # 'exist_ok=True' prevents an error if the directory already exists, which is
    # useful when running the script multiple times.
    target_category_dir.mkdir(parents=True, exist_ok=True)

    # Construct the full path for the file's new location.
    # The file will be placed inside its category folder with its original filename.
    destination_file_path = target_category_dir / file_path.name

    try:
        # Move the file from its current location to the new destination.
        # shutil.move is a robust way to move files, handling cross-device moves
        # and renaming files as needed. We convert Path objects to strings
        # because shutil functions historically expect string paths.
        shutil.move(str(file_path), str(destination_file_path))
        print(f"Moved: '{file_path.name}' -> '{destination_file_path}'")
    except Exception as e:
        # Catch any potential errors during the move operation (e.g., permissions issues)
        # and report them to the user, without stopping the entire script.
        print(f"Error moving '{file_path.name}': {e}")


def main() -> None:
    """
    Main function to orchestrate the entire file organization process.
    This function sets up the environment and iterates through the files to organize them.
    """
    print(f"Starting file organization from: '{SOURCE_DIRECTORY}'")
    print(f"Organized files will go into: '{DESTINATION_BASE_DIRECTORY}'")
    print("-" * 40) # A separator for better readability

    # Step 1: Check if the source directory exists.
    if not SOURCE_DIRECTORY.is_dir():
        print(f"Error: Source directory '{SOURCE_DIRECTORY}' does not exist or is not a directory.")
        print("Creating an empty source directory for testing purposes.")
        # If the source doesn't exist, create it so the script can still run
        # (though it will find no files). In a real-world scenario, you might
        # want to exit here or prompt the user.
        SOURCE_DIRECTORY.mkdir(parents=True, exist_ok=True)
        print(f"Source directory '{SOURCE_DIRECTORY}' created. Please add files to it.")
        # Since the directory was just created, there are no files to organize.
        return # Exit the main function.

    # Step 2: Ensure the base destination directory exists.
    # If it doesn't, .mkdir() will create it (and any parent directories)
    # just like we did for the target category directories.
    DESTINATION_BASE_DIRECTORY.mkdir(parents=True, exist_ok=True)

    # Step 3: Iterate through all items (files and subdirectories) in the source directory.
    # .iterdir() is a generator, which is memory-efficient for listing directory contents.
    found_files = 0
    for item in SOURCE_DIRECTORY.iterdir():
        # We only want to organize actual files, not subdirectories or other filesystem objects.
        if item.is_file():
            found_files += 1
            # Call our helper function to organize this specific file.
            organize_file(item, CATEGORIES, DESTINATION_BASE_DIRECTORY)

    if found_files == 0:
        print("\nNo files found in the source directory to organize.")
    print("-" * 40) # Another separator
    print("File organization complete!")


# This is a standard Python idiom that ensures 'main()' is called only when
# the script is executed directly (e.g., 'python your_script.py'),
# not when it's imported as a module into another Python script.
if __name__ == "__main__":
    main()

# --- Example Usage Instructions ---
#
# To test this script and see it in action:
#
# 1.  Save this code as a Python file (e.g., 'file_organizer.py').
#
# 2.  In the same directory where you saved the script, create a folder named 'unorganized_files'
#     (or whatever you set SOURCE_DIRECTORY to be in the Configuration Section).
#     You can do this from your terminal:
#     mkdir unorganized_files
#
# 3.  Inside the 'unorganized_files' folder, create some dummy files. You can use your
#     operating system's commands or manually create empty files.
#     For example, on Linux/macOS, navigate into 'unorganized_files' and use 'touch':
#     cd unorganized_files
#     touch my_important_report.pdf
#     touch holiday_photo.jpg
#     touch meeting_notes.txt
#     touch my_new_song.mp3
#     touch project_invoice_2023.docx
#     touch random_document.rtf
#     touch some_video.mp4
#     touch misc_file.log            # This file should go to the 'Other' category
#     touch my_resume_v2.pdf         # Will match 'resume' keyword
#     touch project_plan_v1.xlsx     # Will match 'project' keyword
#     touch backup_archive.zip
#     cd .. # Go back to the script's directory
#
# 4.  Run the script from your terminal:
#     python file_organizer.py
#
# 5.  Observe the 'organized_output' folder (or whatever you set DESTINATION_BASE_DIRECTORY to be).
#     You should see new subfolders like 'Documents', 'Images', 'Reports', 'Bills', 'Other', etc.,
#     with your dummy files moved into their respective categories.
#
# Experiment by adding more rules to the CATEGORIES dictionary or changing existing ones
# to tailor the organization to your specific needs!