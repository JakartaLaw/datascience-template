import argparse

from src.config import Config

def cli():
    parser = argparse.ArgumentParser('command')
    parser.add_argument('command', help="Choose a commando: download_data, run")
    args = parser.parse_args()
    arg = args.command

    # action to do based on command
    if arg == 'run':
        run_all()
    elif arg == 'download_data':
        download_data()
    # you should add your own functions here. Maybe you want to run only a subset of your analysis. Re-train your model. Added to a function and use this file.

    else:
        print("You have chosen a command that is currently not possible.")
    

def download_data():
    raise NotImplemented('No automatic download of data is currently implemented')

def run_all():
    # Add you entire 
    print("runs everything")

if __name__ == '__main__':
    cli()