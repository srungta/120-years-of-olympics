import argparse
import pandas as pd
from elasticsearch import Elasticsearch


def main(athletefile, nocfile,
         indexname, chunksize, doctype, verbose):
    # print(athletefile, nocfile,
    #       indexname, chunksize, doctype, verbose)
    None


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
    args = parser.parse_args()
    main(args.athletefile, args.nocfile,
         args.indexname, args.chunksize, args.doctype, args.verbose)
