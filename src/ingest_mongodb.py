import configparser
import datetime
from datetime import timedelta

from pymongo import MongoClient

CONNECT_TO = "mongo"
CONFIG_FILE = "./cnf/dev.conf"

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

hostname        = config.get(CONNECT_TO, "hostname")
database        = config.get(CONNECT_TO, "database")
port            = int(config.get(CONNECT_TO, "port"))
username        = config.get(CONNECT_TO, "username")
password        = config.get(CONNECT_TO, "password")

connection_string=f"mongodb://{hostname}:{port}/"


client = MongoClient(connection_string)
db = client[database]
events = db["events"]

event_1 = {
"event_id": 1,
"event_timestamp": datetime.datetime.today(),
"event_name": "signup"
}
event_2 = {
"event_id": 2,
"event_timestamp": datetime.datetime.today(),
"event_name": "pageview"
}
event_3 = {
"event_id": 3,
"event_timestamp": datetime.datetime.today(),
"event_name": "login"
}
# insert the 3 documents
events.insert_one(event_1)
events.insert_one(event_2)
events.insert_one(event_3)

start_date = datetime.datetime.today() + datetime.timedelta(days = -1)
end_date = start_date + datetime.timedelta(days = 1 )
mongo_query = { "$and":[{"event_timestamp" :{ "$gte": start_date }}, 
                        {"event_timestamp" :{ "$lt": end_date }}]}

event_docs = events.find(mongo_query,batch_size=3000)


# create a blank list to store the results
all_events = []
# iterate through the cursor
for doc in event_docs:
    event_id = str(doc.get("event_id", -1))
    event_timestamp = doc.get(
    "event_timestamp", None)
    event_name = doc.get("event_name", None)
    # add all the event properties into a list
    current_event = []
    current_event.append(event_id)
    current_event.append(event_timestamp)
    current_event.append(event_name)
    # add the event to the final list of events
    all_events.append(current_event)

print(all_events)