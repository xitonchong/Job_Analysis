import datetime
import csv
import time
import os
import logging


''' this creates a singletone object'''
def create_logfile():
    date_time = datetime.datetime.today().strftime('%d-%b-%y_%H:%M:%S')
    logfile = f"log/{date_time}.log"
    logging.basicConfig(filename=logfile, filemode='w',
                        level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', force=True)
    logging.info(f'Log file {logfile} created')
    return logging


def create_file(file, logging):
    # delete existing file if re-running
    logging.info("checking if current daily csv exists...")
    if os.path.exists(file):
        os.remove(file)
        logging.info(f"{file} deleted")
    else:
        logging.info(f"{file} does not exists")
        
    # create file and add header
    header = ['date_time', 'search_keyword', 'search_count', 'job_id', 'job_title', 'company', 'location', 'remote', 'update_time', 'applicants', 'job_pay', 'job_time', 'job_position', 'company_size', 'company_industry', 'job_details']
    with open(file, 'w') as f:
        w = csv.writer(f)
        w.writerow(header)
        logging.info(f"{file} created")
        
        
        
    