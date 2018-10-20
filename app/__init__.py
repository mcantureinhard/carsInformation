from flask import Flask
import redis

app = Flask(__name__)
#will just use some hardcoded redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

cars_cache = CarCache()
