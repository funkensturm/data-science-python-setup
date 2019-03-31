import os


def project_path():
    """Return absolute path for the project root

    Examples
    --------
    >>> utils.project_path()
    """

    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, '..', '..')


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
