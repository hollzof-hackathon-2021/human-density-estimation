import os


def assert_file_path(file_path: str):
    """Asserts the existence of the file path.

    Args:
      file_path: Path of the file to check.
    """
    assert os.path.isfile(file_path), f"'{file_path}' file path is not valid"


def assert_folder_path(folder_path: str):
    """Asserts the existence of the folder path.

    Args:
      folder_path: Path of the folder to check.
    """
    assert os.path.isdir(folder_path), f"'{folder_path}' folder path is not valid"


def assert_newfile_path(newfile_path: str):
    """Asserts the validity of the path for a new file.
    1. It must be in a valid directory,
    2. The basename (file name) must exist.

    Args:
      newfile_path: Path to check for a new file.
    """
    assert os.path.isdir(os.path.dirname(newfile_path)), "new file path is not in a valid directory"
    assert os.path.basename(newfile_path) != "", "new file path does not lead to a file"
