import requests

class adaptive:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Ip:
   def __init__(self):
      self.ip = input("Введите ip-adress: ")
      self.get_whois()
   def get_ip(self,ip):
      find = requests.request('get', f"http://free.ipwhois.io/json/{ip}").json()
      global whois
      whois = dict(find)

      data = {
         'ip': whois['ip'],
         'country': whois['country'],
         'city': whois['city'],
         'timezone': whois['timezone_gmt']
      }
      return data


   def get_whois(self):
      data = self.get_ip(self.ip)
      print(f"=================================\n"
            f"\tАдрес:    {data['ip']}\n"
            f"\tСтрана:    {data['country']}\n"
            f"\tГород:    {data['city']}\n"
            f"\tВремя:    {data['timezone']}\n"
            f"=================================\n")
      input()