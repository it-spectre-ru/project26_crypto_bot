import requests
import time
import hmac
import hashlib
from config import API_KEY, API_SECRET
from urllib.parse import urlencode



def get_info():
  values = dict()
  values['method'] = 'getInfo'
  values['nonce'] = str(int(time.time()))

  body = urlencode(values).encode('utf-8')
  sign = hmac.new(API_SECRET.encode('utf-8'), body, hashlib.sha512).hexdigest()

  print(sign)


  




def main():
  get_info()


if __name__ == '__main__':
  main()