import argparse
import pandas as pd
from elasticsearch import Elasticsearch
import logging
import sys
logging.basicConfig(level=logging.DEBUG)

def setup_custom_logger(name, logfilename):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(logfilename, mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

def main(athletefile, nocfile,
         indexname, chunksize, doctype, deleteexisting, verbose, logfilename):
    logger = setup_custom_logger(name=__name__, logfilename=logfilename)
    if verbose == False:
        logger.disabled = True
    logger.info("All arguments received. Starting to index.")

    logger.debug("Reading athlete file.")
    athlete_events = pd.read_csv(athletefile, iterator=True,chunksize=chunksize)
    logger.debug("Athlete file read in a dataframe.")

    logger.debug("Reading noc file.")
    noc_file = pd.read_csv(nocfile,iterator=True, chunksize=chunksize)
    logger.debug("Noc file read in a dataframe.")

    logger.info("Initializing elastic search.")
    es = Elasticsearch(timeout=30)
    if deleteexisting:
        try:
            logger.debug("Trying to delete the index.")
            es.indices.delete(index=indexname)
            logger.debug("Deleted the index.")
        except Exception as e:
            logger.error('Could not delete index.',e)
    logger.debug("Trying to create the index.")
    es.indices.create(index=indexname)
    logger.debug("Index created successfully.")
    for i, df in enumerate(athlete_events):
        logger.debug("Iteration" + str(i) + " : dataframe size "+ str(len(df.index)))
        records = df.where(pd.notnull(df),None).T.to_dict()
        list_records = [records[value] for value in records]
        for record in list_records:
            try:
                es.index(indexname, doctype, body=record)
            except:
                logger.error(sys.exc_info()[0])
                pass
    logger.debug("Indexing complete.")
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
    parser.add_argument('--logfilename', '-l', default='log.log',
                        help='Path to the log file.')
    args = parser.parse_args()
    main(args.athletefile, args.nocfile,
         args.indexname, args.chunksize, args.doctype, args.deleteexisting, args.verbose, args.logfilename)
