# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:13:22 2024

@author: Bornand
"""

# adding git-hash to a filename

import git
import os
import requests

def generate_versioned_filename(basename, ext):
    """
    Generate a filename with the current git hash.

    Parameters:
    basename (str): The base name of the file.
    ext (str): The extension of the file.

    Returns:
    str: The generated filename with git hash and possibly '-dirty' appended.
    """
    # Get the current repository
    repo = git.Repo(search_parent_directories=True)
    # Get the short git hash
    git_hash = repo.git.rev_parse(repo.head.commit.hexsha, short=10)
    # Check for uncommitted changes
    is_dirty = repo.is_dirty()

    # Construct the filename
    filename = f"{basename}-{git_hash}"
    if is_dirty:
        filename += "-dirty"
    filename += f".{ext}"

    return filename




def download_file(url, destination_file):
    """
    # Example usage:
    url = "https://example.com/datafile.txt"
    destination_file = "data/datafile.txt"
    download_file(url, destination_file)
    """

    # Ensure the directory exists
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)

    if os.path.isfile(destination_file):
        # Do nothing if the file already exists
        print(f"Already downloaded {destination_file}")
    else:
        # Download the file
        print(f"Downloading {destination_file} ... ", end="")
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        with open(destination_file, 'wb') as f:
            f.write(response.content)
        print("done.")



import zipfile

def unzip_one_file(zipfile_path, filename, destination_file):
    """
    Unzips a specific file from a zip archive and saves it to a specified location.

    Parameters:
    zipfile_path (str): Path to the zip file.
    filename (str): The name of the file to extract from the zip file.
    destination_file (str): The destination path where the extracted file will be saved.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)

    with zipfile.ZipFile(zipfile_path, 'r') as z:
        if filename in z.namelist():
            with z.open(filename) as source, open(destination_file, 'wb') as target:
                target.write(source.read())
            print(f"Extracted {filename} to {destination_file}")
        else:
            print(f"{filename} not found in the zip archive.")

# Example usage:
# zipfile_path = 'data/archive.zip'
# filename = 'datafile.txt'
# destination_file = 'data/unzipped_datafile.txt'
# unzip_one_file(zipfile_path, filename, destination_file)

    