import redis

"""
    restart server remember remove dump.rdb file
"""
def set(host,port, key, val):
    r = redis.Redis(host=host, port=port)
    r.set(key,val)

def get(host,port,key):
    r = redis.Redis(host=host, port=port)
    v= r.get(key)
    if v:
        return v.decode('utf-8')
    return ''