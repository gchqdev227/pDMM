"""
Tests for the command line.
"""
import os
import random
import tempfile
import unittest

import pdmm.sampling
from pdmm.__main__ import check_arg
from pdmm.__main__ import main as pdmm_main

from .utils import read_contents_from_path, python_2_randint


class CommandLineTests(unittest.TestCase):

    def setUp(self):
        """Code to run before each test."""
        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self):
        """Code to run after each test."""
        self.tempdir.cleanup()

    def test_overall_output(self):
        """Test that the output is correct."""
        random.seed(1)
        # pdmm.sampling.random.randint = python_2_randint
        arg_string = "--corpus {} --output {} --iterations {}".format(
            "tests/data/sample_data",
            self.tempdir.name,
            50,
        )
        arguments_components = arg_string.split()
        parsed_args = check_arg(arguments_components)

        pdmm_main(parsed_args)

        expected_top_words = read_contents_from_path("tests/data/topWordsNew")
        expected_topic_assignments = read_contents_from_path("tests/data/topicAssignmentsNew")

        top_words = read_contents_from_path(os.path.join(self.tempdir.name, "topWords"))
        topic_assignments = read_contents_from_path(os.path.join(self.tempdir.name, "topicAssignments"))

        self.assertEqual(top_words, expected_top_words, "Top words should be equal.")
        self.assertEqual(topic_assignments, expected_topic_assignments, "Topic assignments should be equal.")
