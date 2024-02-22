import csv
import sqlite3
from configparser import ConfigParser

import boto3
import psycopg2
import pymysql

CONNECT_TO = "postgres" #"mysql"
CONFIG_FILE = "./cnf/dev.conf"
LOCAL_FILE = "./data/order_extract.csv"
QUERY = """
SELECT
*
FROM sales.orders;
"""

def fetch_database (connect_to, config_file, query):
    """
    Connect and query postgres db using a configuration file
    """

    query_response = None

    config = ConfigParser()
    config.read(config_file)

    try:
        if connect_to == "postgres":
            db_connection = psycopg2.connect(
                host    = config.get(connect_to, "hostname"),
                dbname  = config.get(connect_to, "database"),
                port    = int(config.get(connect_to, "port")),
                user    = config.get(connect_to, "username"),
                password= config.get(connect_to, "password"),
            )
        elif connect_to == "mysql":
            db_connection = pymysql.connect(
            host    = config.get(connect_to, "hostname"),
            database= config.get(connect_to, "database"),
            port    = int(config.get(connect_to, "port")),
            user    = config.get(connect_to, "username"),
            password= config.get(connect_to, "password"),
            )
        else:
            print("connect to not correct defined")
        
        print("database connection established")

        try:
            cursor = db_connection.cursor()
            cursor.execute(query)
            query_response = cursor.fetchall()
            cursor.close()
        
        except: 
            if connect_to == "postgres":
                print(psycopg2.Error.pgcode, psycopg2.Error.pgerror)
            elif connect_to == "mysql":
                print('mysql issue')
            
        finally:
            db_connection.close()
            print("database connection closed")  
    
    except:
        print("connection error")

    return query_response


def s3_file_upload (config_file, local_file):
    """
    connects and uploads a file to s3 bucket using credentials
    from a configuration file
    """
    
    start = local_file.rfind("/") + 1
    s3_file_name = local_file[start:]
    
    parser = ConfigParser()
    parser.read(config_file)

    s3 = boto3.client(
        's3',
        aws_access_key_id       = parser.get("aws_s3_access", "access_key"),
        aws_secret_access_key   = parser.get("aws_s3_access", "secret_key")
    )
    s3.upload_file(
        local_file, 
        parser.get("aws_s3_access", "bucket_name"),
        s3_file_name
    )
    print(f"local file: {local_file} uploaded to s3 bucket")

def main():
    """this is main"""

    query_response = fetch_database(CONNECT_TO, CONFIG_FILE, QUERY)

    if query_response is not None:

        with open(LOCAL_FILE, 'w') as fp:
            csv_w = csv.writer(fp, delimiter='|')
            csv_w.writerows(query_response)
            fp.close()
            print("csv written")

        s3_file_upload (CONFIG_FILE, LOCAL_FILE)

if __name__ == "__main__":
    main()