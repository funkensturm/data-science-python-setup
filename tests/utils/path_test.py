import os
import unittest

import utils


class TestUtilsPath(unittest.TestCase):

    def test_project_path(self):
        path = utils.project_path()

        self.assertTrue(type(path) == str)

    def test_path_to(self):
        project_path = utils.project_path()
        data_path = utils.path_to('data')

        self.assertEqual(data_path, f'{project_path}/data')

    def test_ensure_directories(self):
        folder_name = '-temp-test-folder-should-be-removed'
        data_path = utils.path_to('data', folder_name, 'data.csv')

        # Make sure the path does not exists
        path = os.path.dirname(data_path)
        if os.path.exists(path):
            os.rmdir(path)

        utils.ensure_directories(data_path)

        self.assertTrue(os.path.exists(path))

        # Cleanup
        os.rmdir(path)
