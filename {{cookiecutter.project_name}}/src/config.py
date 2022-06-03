from pathlib import Path
import os

filepath = Path(os.path.abspath(__file__)).parent.parent

class Config():

    ROOT_PATH = Path(filepath)
    DATA_PATH = ROOT_PATH / Path('data')
    RAW_DATA = DATA_PATH / Path('raw')
    PROCESSED_DATA = DATA_PATH / Path('processed')

    TABLES = ROOT_PATH / Path('tables')
    FIGURES = ROOT_PATH / Path('figures')
