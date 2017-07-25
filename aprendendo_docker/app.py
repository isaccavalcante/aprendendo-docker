#/usr/bin/env python
#coding: utf-8
from flask import Flask
from redis import Redis, RedisError
import os, socket

# Conectando-se ao Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i> Não foi possivel conectar-se ao redis, contador desabilitado. </i>"
        html = "<h3> Hello {name} </h3>" \
            "<b> Nome do host:</b> {hostname} <br/>" \
            "<b> Visitas: </b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname = socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


