import os


def project_path():
    """Return absolute path for the project root

    Examples
    --------
    >>> utils.project_path()
    """

    cwd = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(cwd, '..', '..')

    return os.path.abspath(project_root)


def path_to(*pathsegments):
    """Return absolute path to the specified folder or file

    Parameters
    ----------
    pathsegments : One or more string components

    Examples
    --------
    >>> utils.path_to('data', 'data-set', 'raw', 'data.csv')
    """

    return os.path.join(project_path(), *pathsegments)


def ensure_directories(path):
    """Create directories for the path if they don't exist

    Parameters
    ----------
    path : The path in question. Can also contain a filename

    Examples
    --------
    >>> path = utils.path_to('data', 'data-set', 'data.csv')
    >>> utils.ensure_directories(path)
    """

    path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)

    return path
