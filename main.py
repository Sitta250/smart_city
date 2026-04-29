import os
from confluent_kafka import SerializingProducer
import simplejson as json

LONDON_COORDINATE = {"latitude": 51.5074, "longitude": -0.1278}
BIRMINGHAM_COORDINATE = {"latitude": 52.4862, "longitude": -1.8904}

# calculate movement increments
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATE['latitude'] - LONDON_COORDINATE['latitude']) / 100
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATE['longitude'] - LONDON_COORDINATE['longitude']) / 100


