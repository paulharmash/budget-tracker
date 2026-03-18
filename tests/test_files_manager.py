import unittest
import os
import shutil
import csv
# from pathlib import Path

from budget_tracker.files_manager import create_file
from budget_tracker.constants import *

# The three test cases below are identical as for now that's what they have to check
class TestWhenNothingExists(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TEST_DATA_FOLDER):
            shutil.rmtree(TEST_DATA_FOLDER)
        return super().setUp()
    
    def tearDown(self):
        if os.path.exists(TEST_DATA_FOLDER):
            shutil.rmtree(TEST_DATA_FOLDER)
        return super().tearDown()
    
    def test_nothing_exists(self):
        file_path = create_file(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        self.assertEqual(
            file_path,
            os.path.join(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        )
        self.assertTrue(
            os.path.exists(file_path)
        )
        with open(file_path, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)
            self.assertEqual(
                header,
                HEADINGS
            )

class TestWhenFolderExists(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(TEST_DATA_FOLDER):
            os.mkdir(TEST_DATA_FOLDER)
        return super().setUp()
    
    def tearDown(self):
        if os.path.exists(TEST_DATA_FOLDER):
            shutil.rmtree(TEST_DATA_FOLDER)
        return super().tearDown()
    
    def test_folder_exists(self):
        file_path = create_file(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        self.assertEqual(
            file_path,
            os.path.join(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        )
        self.assertTrue(
            os.path.exists(file_path)
        )

class TestWhenFileExists(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(TEST_DATA_FOLDER):
            create_file(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        return super().setUp()
    
    def tearDown(self):
        if os.path.exists(TEST_DATA_FOLDER):
            shutil.rmtree(TEST_DATA_FOLDER)
        return super().tearDown()
    
    def test_file_exists(self):
        file_path = create_file(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        with open(file_path, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            number_of_rows_before = len(list(csvreader))
        create_file(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        with open(file_path, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            number_of_rows_after = len(list(csvreader))
        self.assertEqual(number_of_rows_before, number_of_rows_after)

        self.assertEqual(
            file_path,
            os.path.join(TEST_DATA_FOLDER, TEST_TABLE_NAME)
        )
        self.assertTrue(
            os.path.exists(file_path)
        )