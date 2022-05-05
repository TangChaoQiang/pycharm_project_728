from redis import Redis

redis_cli = Redis(
    port=6379,
    host="localhost",
    db=0
)

redis_cli.set("name", "中国")
print(redis_cli.get("name".encode("utf-8")))
print(redis_cli.keys("*"))
