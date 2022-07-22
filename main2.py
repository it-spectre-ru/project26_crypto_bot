import requests
import time
import hmac
import hashlib
from config import API_KEY, API_SECRET
from urllib.parse import urlencode



def get_info():
  values = dict()
  values["method"] = "getInfo"
  values["nonce"] = str(int(time.time()))

  body = urlencode(values).encode("utf-8")
  sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

  headers = {
    "key": API_KEY,
    "sign": sign
  }

  response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
  return response.json()



def get_deposit_address(coin_name="btc"):
  values = dict()
  values["method"] = "GetDepositAddress"
  values["coinName"] = coin_name
  values["need_new"] = 0
  values["nonce"] = str(int(time.time()))

  body = urlencode(values).encode("utf-8")
  sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

  headers = {
    "key": API_KEY,
    "sign": sign
  }

  response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
  return response.json()


  

def main():
  # print(get_info())

  coin_name = input("Enter coin name: ")
  print(get_deposit_address(coin_name=coin_name))


if __name__ == "__main__":
  main()