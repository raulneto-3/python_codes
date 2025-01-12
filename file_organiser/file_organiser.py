import os
import shutil
import logging
from datetime import datetime
import configparser

# Configuração de logging
logging.basicConfig(filename='file_organiser.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def organiser(path):
    for root, _, files in os.walk(path):
        for current_file in files:
            _, extension = os.path.splitext(current_file)
            os.makedirs(os.path.join(path, extension.lstrip('.')), exist_ok=True)
            source = os.path.join(root, current_file)
            destination = os.path.join(path, extension.lstrip('.'), current_file)
            try:
                shutil.move(source, destination)
                logging.info(f"Moved {source} to {destination}")
            except Exception as e:
                logging.error(f"Error moving {source} to {destination}: {str(e)}")

def rename_files(path, prefix='', suffix=''):
    for root, _, files in os.walk(path):
        for current_file in files:
            new_name = f"{prefix}{current_file}{suffix}"
            source = os.path.join(root, current_file)
            destination = os.path.join(root, new_name)
            try:
                os.rename(source, destination)
                logging.info(f"Renamed {source} to {destination}")
            except Exception as e:
                logging.error(f"Error renaming {source} to {destination}: {str(e)}")

def move_files(path, destination_path, file_type=None):
    for root, _, files in os.walk(path):
        for current_file in files:
            if file_type and not current_file.endswith(file_type):
                continue
            source = os.path.join(root, current_file)
            destination = os.path.join(destination_path, current_file)
            try:
                shutil.move(source, destination)
                logging.info(f"Moved {source} to {destination}")
            except Exception as e:
                logging.error(f"Error moving {source} to {destination}: {str(e)}")

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

if __name__ == '__main__':
    config = load_config('config.ini')
    path = config['DEFAULT']['Path']
    try:
        organiser(path)
        rename_files(path, prefix=config['RENAME']['Prefix'], suffix=config['RENAME']['Suffix'])
        move_files(path, config['MOVE']['DestinationPath'], file_type=config['MOVE']['FileType'])
    except Exception as e:
        logging.error(f"Error: {str(e)}")