from colorama import Fore

import Search.Phone as p
import Search.IP as ip
import Search.fio as f
import Search.tg as t
import Search.inst as ins
import Search.vk as v
import Search.faq as fa
import Search.mail as m
import Search.snils as sn
import Search.inn as i
import Search.car as c
import Search.ddosip as dip
import Search.winlock as wl

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
   magenta = Fore.MAGENTA

def logo():
    print(color.magenta + "██████╗░███████╗░██████╗████████╗██████╗░██╗░█████╗░████████╗███████╗██████╗░\n"
                    "██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗\n"
                    "██████╔╝█████╗░░╚█████╗░░░░██║░░░██████╔╝██║██║░░╚═╝░░░██║░░░█████╗░░██║░░██║\n"
                    "██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██╗██║██║░░██╗░░░██║░░░██╔══╝░░██║░░██║\n"
                    "██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║██║╚█████╔╝░░░██║░░░███████╗██████╔╝\n"
                    "╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═════╝░\n"
                    "\t\t\t\tDeveloped by !zxckeshy ; !zxcbuldozer")

def menu():
    print(color.BOLD + "╭---------------------------------------------------╮", color.END, color.magenta + "\n"
                   "|\t\t\t\t\t\t",color.BOLD + "MENU" + color.END,color.magenta + "\t\t\t\t\t\t|\n"
                   "|\t\t\t\t\t\t\t\t\t\t\t\t\t|\n"
                   "|  ",color.BOLD,color.RED + "[" + color.END,"1",color.BOLD,color.RED + "]"," Поиск по номеру" + "\t\t\t",color.BOLD,color.RED + "[" + color.END,"2",color.BOLD,color.RED + "]","Поиск по почте",color.END,color.magenta + "\t|\n"
                   "|  ",color.BOLD,color.RED + "[" + color.END,"3",color.BOLD,color.RED + "]"," Поиск по IP" + "\t\t\t\t",color.BOLD,color.RED + "[" + color.END,"4",color.BOLD,color.RED + "]","Поиск по СНИЛС",color.END,color.magenta + "\t|\n"
                   "|  ",color.BOLD,color.RED + "[" + color.END,"5",color.BOLD,color.RED + "]"," Поиск по ФИО" + "\t\t\t\t",color.BOLD,color.RED + "[" + color.END,"6",color.BOLD,color.RED + "]","Поиск по ИНН",color.END,color.magenta + "\t\t|\n"
                   "|  ",color.BOLD,color.RED + "[" + color.END,"7",color.BOLD,color.RED + "]"," Поиск по Telegram" + "\t\t",color.BOLD,color.RED + "[" + color.END,"8",color.BOLD,color.RED + "]","Поиск по машине",color.END,color.magenta + "\t|\n"
                   "|  ",color.BOLD,color.RED + "[" + color.END,"9",color.BOLD,color.RED + "]"," Поиск по inst" + "\t\t\t",color.BOLD,color.RED + "[" + color.END,"10",color.BOLD,color.RED + "]","Ddos-IP",color.END,color.magenta + "\t\t\t|\n"
                   "|  ",color.BOLD,color.RED + "[" + color.END,"11",color.BOLD,color.RED + "]"," Поиск по VK" + "\t\t\t\t",color.BOLD,color.RED + "[" + color.END,"12",color.BOLD,color.RED + "]","Создать WinLock",color.END,color.magenta + "\t|\n"
                   "|  ",color.BOLD,color.RED + "[" + color.END,"13",color.BOLD,color.RED + "]"," О Туле?" + "\t\t\t\t\t" ,color.BOLD,color.RED + "[" + color.END,"14",color.BOLD,color.RED + "]","Выйти",color.END,color.magenta + "\t\t\t|\n"
                   "|  \t\t\t\t\t\t\t\t\t\t\t\t\t"
                   "|  \n"
                   "╰---------------------------------------------------╯\n", sep="")
    main_page = int(input(color.RED + "[WHY] " + color.BOLD + "Ваш Выбор?: "))

    if main_page == 1:
        p.Phone()
    elif main_page == 2:
        m.Mail()
    elif main_page == 3:
        ip.Ip()
    elif main_page == 4:
        sn.snils
    elif main_page == 5:
        f.fio
    elif main_page == 6:
        i.inn
    elif main_page == 7:
        t.tg
    elif main_page == 8:
        c.car
    elif main_page == 9:
        ins.inst
    elif main_page == 10:
        dip.ddosip
    elif main_page == 11:
        v.vk
    elif main_page == 12:
        wl.winlock
    elif main_page == 13:
        fa.Faq
    else:
        quit()

if __name__ == "__main__":
    logo()
    menu()