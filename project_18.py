import requests
import os

url="https://api.blockcypher.com/v1/btc/test3/txs/44b0e7aef67bd56f35e34ef62275883b19378d448b9050b91b35603f3a3040dc?limit=50&includeHex=true" \

response=requests.get(url)
response.encoding="utf-8"
html=response.text
f=open("tx.txt","wb")
f.write(html.encode("utf-8"))
f.close()

