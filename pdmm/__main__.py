"""
Contains the main function for running inference from the command line.
"""
import argparse
import logging
import os
import sys

from .corpus import Corpus
from .sampling import GibbsSamplingDMM


def main(parameters):
    """Main function."""
    logger = logging.getLogger(__name__)

    corpus = Corpus.from_document_file(parameters.corpus_path)

    model = GibbsSamplingDMM(
        corpus,
        parameters.output_path,
        parameters.number_of_topics,
        parameters.alpha,
        parameters.beta,
        parameters.number_of_iterations,
        parameters.number_of_top_words,
        parameters.name
    )
    model.topic_assignment_initialise()
    model.inference()

    logger.debug("Writing Results")
    model.save_top_topical_words_to_file(parameters.output_path + parameters.name + ".topWords")
    model.save_topic_assignments_to_file(parameters.output_path + parameters.name + ".topicAssignments")


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Topic Modelling')
    parser.add_argument('-c', '--corpus-file', help='Path to corpus file', dest="corpus_path", required=True, metavar="<path>")
    parser.add_argument('-o', '--output-path', help='Output directory', dest="output_path", default="./output/", metavar="<path>")
    parser.add_argument('-n', '--num-topics', help='Number of topics', dest="number_of_topics", default=20, metavar="<integer>")
    parser.add_argument('-a', '--alpha', help='Alpha value', default=0.1, metavar="<double>")
    parser.add_argument('-b', '--beta', help='Beta value', default=0.001, metavar="<double>")
    parser.add_argument('-ni', '--iterations', help='Number of iterations', dest="number_of_iterations", default=2000, metavar="<integer>")
    parser.add_argument('-t', '--num_words', help='Number of most probable topical words', dest="number_of_top_words", default=20, metavar="<integer>")
    parser.add_argument('-e', '--name', help='Name of the experiment', default="model", metavar="<string>")
    parameters = parser.parse_args(args)
    return parameters


if __name__ == '__main__':
    parsed_parameters = check_arg(sys.argv[1:])
    main(parsed_parameters)
