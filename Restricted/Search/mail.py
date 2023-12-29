import random

class Mail:
    def __init__(self):
        self.mail = input("Введите электронный адрес: ")
        self.mailreport()
    def mailbase(self):
        with open('Search/basefio.txt', mode="r", encoding="utf-8") as r_file:
            file_text = r_file.readlines()
            fio_text = random.choice(file_text)

            mailget = {
                'fio': fio_text,
                'mail': self.mail
            }

            return mailget
    def mailreport(self):
        mailr = self.mailbase()

        print(f'''        ================================================\n
          Почта:        {mailr['mail']}
          Пред. ФИО:    {mailr['fio']}
        ================================================''')