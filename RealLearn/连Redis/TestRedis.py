import redis

r = redis.Redis('10.52.23.108','6379')
print(r)

r.set('foo', 'bar')
print(r.get('foo'))
r.delete('foo')
print(r.get('foo'))