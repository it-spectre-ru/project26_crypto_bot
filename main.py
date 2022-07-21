import requests

def get_info():
  response = requests.get(url='https://yobit.net/api/3/info')

  with open('info.txt', 'w') as file:
    file.write(response.text)

  return response.text


def main():
  print(get_info())


if __name__ == '__main__':
  main()