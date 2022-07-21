import requests

def get_info():
  response = requests.get(url='https://yobit.net/api/3/info')

  with open('info.txt', 'w') as file:
    file.write(response.text)

  return response.text


def get_ticker(coin1='btc', coin2='usd'):
  # response = requests.get(url='https://yobit.net/api/3/ticker/eth_btc-xrp_btcccc?ignore_invalid=1')
  response = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1')

  with open('ticker.txt', 'w') as file:
    file.write(response.text)

  return response.text



def main():
  # print(get_info())
  print(get_ticker())
  print(get_ticker(coin1='eth'))


if __name__ == '__main__':
  main()