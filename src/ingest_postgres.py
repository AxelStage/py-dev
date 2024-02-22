#!python3



import configparser
import psycopg

CONFIG_FILE = "./dev.conf"
CONNECTION_CONFIG = "rds-pg13"

# get config
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

# Connect to an existing database
with psycopg.connect(
    host=config.get(CONNECTION_CONFIG, "host"),
    port=config.get(CONNECTION_CONFIG, "port"),
    dbname=config.get(CONNECTION_CONFIG, "database"),
    user=config.get(CONNECTION_CONFIG, "username"),
    password=config.get(CONNECTION_CONFIG, "password")
    ) as connection:

    # conn.autocommit = True

    # Open a cursor to perform database operations
    with connection.cursor() as db_cursor:

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        db_cursor.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def")
        )

        # Make the changes to the database persistent
        connection.commit()