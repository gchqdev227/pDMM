"""
Tests for generation after inference.
"""
import unittest

from pdmm import Corpus, GibbsSamplingDMM


class GenerationTests(unittest.TestCase):

    def setUp(self):
        """Code to run before each test."""
        corpus = Corpus.from_document_file("tests/data/sample_data")
        self.model = GibbsSamplingDMM(corpus, number_of_topics=20)
        self.model.randomly_initialise_topic_assignment(seed=1)
        self.model.inference(50)

    def test_generated_documents_lengths(self):
        """Test that the lengths of the generated documents are correct."""
        generated_documents, __ = self.model.generate_synthetic_documents(10, seed=5)
        document_sizes = [len(document) for document in generated_documents]
        expected_sizes = [6, 3, 5, 5, 3, 3, 3, 1, 7, 7]
        self.assertListEqual(document_sizes, expected_sizes)

    def test_generation_with_replacement(self):
        """Test the generation of sentences with replacement."""
        generated_documents, __ = self.model.generate_synthetic_documents(10, seed=5)
        expected_documents = [
            ['people', 'post', 'account', 'plan', 'show', 'media'],
            ['proves', 'numbers', 'numbers'],
            ['deals', 'people', 'great', 'time', 'neowin'],
            ['time', 'good', 'facebook', 'follow', 'good'],
            ['threat', 'excited', 'smm'],
            ['ipad', 'access', 'macbook'],
            ['hours', 'omg', 'account'],
            ['android'],
            ['ipad', 'brand', 'improve', 'professional', 'red', 'neowin', 'great'],
            ['logged', 'reliable', 'tests', 'things', 'play', 'reports', 'make']
        ]

        self.assertListEqual(generated_documents, expected_documents)
