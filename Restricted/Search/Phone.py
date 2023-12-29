import pycountry
import phonenumbers
import random
from phonenumbers import carrier, region_code_for_country_code

with open('Search/basemail.txt', mode="r") as r_file:
    file_text = r_file.readlines()
    random_text = random.choice(file_text)
class color:
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


class Phone:
    def __init__(self):
        self.number = input("\n Введите номер: ")
        self.number = self.number.replace("+", "")
        self.dl()

    def base(self):
        try:
            phone_num = phonenumbers.parse(f"+{self.number}", None)
        except:
            raise ValueError("Неверный номер")

        country_iso = region_code_for_country_code(phone_num.country_code)
        country = pycountry.countries.get(alpha_2=country_iso)

        operator = carrier.name_for_number(phone_num, None)

        with open('Search/basemail.txt', mode="r") as r_file:
            file_text = r_file.readlines()
            mail_text = random.choice(file_text)

        if operator == "":
            operator = "Не найдено"

        get = {
            "country": country.name,
            "operator": operator,
            "mail": mail_text
        }

        return get

    def dl(self) -> object:
        data = self.base()

        print(f'''        ================================================\n
          Страна:        {data['country']}
          Оператор:      {data['operator']}
          Почта:         {data['mail']}
        ================================================''')