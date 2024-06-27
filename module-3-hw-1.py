import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def copy_file(file_path, target_dir):
   
    target_subdir = target_dir / file_path.suffix[1:].upper()
    target_subdir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, target_subdir / file_path.name)


def process_directory(source_dir, target_dir):

    with ThreadPoolExecutor() as executor:
        futures = []
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                futures.append(executor.submit(copy_file, file_path, target_dir))

        for future in as_completed(futures):
            future.result()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<target_directory>]")
        sys.exit(1)

    source_directory = Path(sys.argv[1])
    target_directory = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_directory.is_dir():
        print(f"Source directory {source_directory} does not exist.")
        sys.exit(1)

    target_directory.mkdir(parents=True, exist_ok=True)

    process_directory(source_directory, target_directory)
    print("Files have been sorted and copied successfully.")
