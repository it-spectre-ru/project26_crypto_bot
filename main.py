import requests

def get_info():
  response = requests.get(url='https://yobit.net/api/3/info')

  with open('info.txt', 'w') as file:
    file.write(response.text)

  return response.text


def get_ticker():
  response = requests.get(url='https://yobit.net/api/3/ticker/eth_btc-xrp_btcccc?ignore_invalid=1')

  with open('ticker.txt', 'w') as file:
    file.write(response.text)

  return response.text



def main():
  # print(get_info())
  print(get_ticker())


if __name__ == '__main__':
  main()