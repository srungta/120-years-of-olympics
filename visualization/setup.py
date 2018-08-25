import argparse
import pandas as pd
from elasticsearch import Elasticsearch
import logging
logging.basicConfig(level=logging.DEBUG)


def main(athletefile, nocfile,
         indexname, chunksize, doctype, deleteexisting, verbose):
    logger = logging.getLogger(name=__name__)
    if verbose == False:
        logger.disabled = True
    logger.info("All arguments received. Starting to index.")
    logger.debug("Reading athlete file.")
    athlete_events = pd.read_csv(athletefile, chunksize=chunksize)
    logger.debug("Athlete file read in a dataframe.")
    logger.debug("Reading noc file.")
    noc_file = pd.read_csv(nocfile, chunksize=chunksize)
    logger.debug("Noc file read in a dataframe.")
    logger.debug("Initializing elastic search.")
    logger.disabled = False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Indexes the dataset in the Elastic Search index.')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Show verbose logs generated during the script execution.')
    parser.add_argument('athletefile',
                        help="Path to athlete_events.csv file.")
    parser.add_argument('nocfile',
                        help="Path to noc_regions.csv file.")
    parser.add_argument('indexname',
                        help="Name of the search index.")
    parser.add_argument('--chunksize', '-c',
                        default=10, type=int,
                        help="Name of the search index.")
    parser.add_argument('--doctype', '-d', default='av-lp',
                        help='Doc type for the search index.')
    parser.add_argument('--deleteexisting', '-de', action='store_false',
                        help='If set to True, existing indices will be deleted.')

    args = parser.parse_args()
    main(args.athletefile, args.nocfile,
         args.indexname, args.chunksize, args.doctype, args.deleteexisting, args.verbose)
