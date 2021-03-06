"""
Utility functions for the tests package.
"""


def read_contents_from_path(file_path):
    """Read the contents of a file as a string."""
    with open(file_path, "r") as rf:
        contents = rf.read()
    return contents
