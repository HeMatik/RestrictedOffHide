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

class Faq(object):
    print(color.BOLD,color.RED + "\t\t\tПриветствую купивших данный тул!\n")
    def __init__(self):
        self.start()
    def start(self):
        print(color.BOLD, color.RED + "Привет!\n"
                                      "Вероятно ты - покупатель нашего тула\n"
                                      "Спасибо за его покупку, мы старались!\n")
        (color.BOLD, color.PURPLE + "Данный тул представляет собой программу,\n"
        ("Которая поможет тебе в поисках твоих жертв!\n"
         ("В этом туле есть буквально все, нужное тебе\n"
          "Надеемся, ты будешь пользоваться нашим тулом,\n"
          "А так же оставишь хороший отзыв!")))