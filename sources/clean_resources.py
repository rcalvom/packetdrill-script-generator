""" Clean Resources Functions """

# System
import logging
import shutil
import os

# Script generator
import configuration

# Constants
folders_to_recreate = [
    configuration.generated_folder,
    configuration.crashing_directory,
    configuration.hanging_directory,
    configuration.processing_directory
] 

def clean_resources():
    """
    Remove temporal files
    """
    for folder in folders_to_recreate:
        if os.path.exists(folder):
            logging.debug("Removing '{0}' folder.".format(folder))
            shutil.rmtree(folder)
        logging.debug("Creating '{0}' folder.".format(folder))
        os.mkdir(folder)
