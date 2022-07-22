import requests
from config import API_KEY, API_SECRET
import time




def get_info():
  values = {}
  values['method'] = 'getInfo'
  values['nonce'] = time.time()

  print(values)

  




def main():
  get_info()


if __name__ == '__main__':
  main()