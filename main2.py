import requests
import time
from config import API_KEY, API_SECRET
from urllib.parse import urlencode



def get_info():
  values = dict()
  values['method'] = 'getInfo'
  values['nonce'] = str(int(time.time()))

  body = urlencode(values).encode('utf-8')
  print(body)

  




def main():
  get_info()


if __name__ == '__main__':
  main()