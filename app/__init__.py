from flask import Flask
import redis
from app.carCache import CarCache

app = Flask(__name__)
#will just use some hardcoded redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

cars_cache = CarCache()

#We need to load our data, we should do it in batches, but for this test I'll just get everything
data = redis_client.hgetall("cars_info")

cars_cache.insertBatch(data)
