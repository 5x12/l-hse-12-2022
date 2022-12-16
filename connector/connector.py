import pandas as pd 
from conf.conf import logging

# Example of a clean code

def get_data(link: str) -> pd.DataFrame:
    """
    This function extracts data from ...
    """
    logging.info('Extracting df')
    df = pd.read_csv(link)
    logging.info('Df is extracted')

    return df
