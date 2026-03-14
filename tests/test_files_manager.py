import unittest
import os
import shutil
from pathlib import Path

from src.files_manager import create_file
from src.constants import *

# The three test cases below are identical as for now that's what they have to check
class TestWhenNothingExists(unittest.TestCase):
    def setUp(self):
        if os.path.exists(DATA_FOLDER):
            shutil.rmtree(DATA_FOLDER)
        return super().setUp()
    
    def tearDown(self):
        if os.path.exists(DATA_FOLDER):
            shutil.rmtree(DATA_FOLDER)
        return super().tearDown()
    
    def test_nothing_exists(self):
        file_path = create_file()
        self.assertEqual(
            file_path,
            os.path.join(DATA_FOLDER, TABLE_NAME)
        )
        self.assertTrue(
            os.path.exists(file_path)
        )

class TestWhenFolderExists(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(DATA_FOLDER):
            os.mkdir(DATA_FOLDER)
        return super().setUp()
    
    def tearDown(self):
        if os.path.exists(DATA_FOLDER):
            shutil.rmtree(DATA_FOLDER)
        return super().tearDown()
    
    def test_folder_exists(self):
        file_path = create_file()
        self.assertEqual(
            file_path,
            os.path.join(DATA_FOLDER, TABLE_NAME)
        )
        self.assertTrue(
            os.path.exists(file_path)
        )

class TestWhenFileExists(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(DATA_FOLDER):
            create_file()
        return super().setUp()
    
    def tearDown(self):
        if os.path.exists(DATA_FOLDER):
            shutil.rmtree(DATA_FOLDER)
        return super().tearDown()
    
    def test_file_exists(self):
        file_path = create_file()
        self.assertEqual(
            file_path,
            os.path.join(DATA_FOLDER, TABLE_NAME)
        )
        self.assertTrue(
            os.path.exists(file_path)
        )
    
    #TODO - calling create_file() twice doesn't corrupt or recreate the existing file (e.g. check that a pre-written value inside the file survives)

