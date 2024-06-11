# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:13:22 2024

@author: Bornand
"""

# adding git-hash to a filename

import git

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



    