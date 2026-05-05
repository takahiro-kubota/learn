from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get("/price/{jan_code}")
def get_price(jan_code: str):
    response = requests.get(
        "https://openapi.rakuten.co.jp/ichibaproduct/api/Product/Search/20250801",
        params={
            "applicationId": os.environ.get("RAKUTEN_APP_ID"),
            "accessKey": os.environ.get("RAKUTEN_ACCESS_KEY"),
            "productCode": jan_code,
            "format": "json",
            "formatVersion": 2,
            "hits": 1,
        }
    )
    data = response.json()
    product = data["Products"][0]
    return {
        "name": product["productName"],
        "price": product["salesMinPrice"],
    }