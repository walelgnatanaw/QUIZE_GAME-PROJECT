import colorama
from colorama import Fore

colorama.init(autoreset=True)
import pyodbc
class wal():
    def __init__(self):
        self.score = []
    def my(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-L4LBIQ7T;'
                              'Database=Walelgn;'
                              'Trusted_Connection=yes;')
        print('well come to trivial project')
        print("select data from sql so print on pycham")
        cursor = conn.cursor()
        cursor.execute('select  Question from Atanaw')
        for row in cursor:
            while True:
                min = input("do you want start? YES or NO")
                if min == 'YES':
                    categ = input("please enter category")
                    if categ == 'A1':
                        cursor.execute('select Question from Atanaw where PersonID <=5 ')
                        row = cursor.fetchall()
                        for Question in row:
                            print(Question)
                            anw = input("please enter your answer ")
                            print("answer is", Fore.YELLOW + F"{anw} ")
                            cursor = conn.cursor()
                            cursor.execute('select  Answer from Atanaw where PersonID<=5')
                        for Answer in cursor:
                           rew = list(Answer)
                           print(Fore.RED + F"{rew}")
                    elif categ == 'B1':
                        cursor.execute('select Question from Atanaw where PersonID between 6 and 10')
                        row = cursor.fetchall()
                        for Question in row:
                            print(Question)
                            ans = input("please enter your answer ")
                            print("answer is ", Fore.BLUE + f"{ans}")
                            cursor = conn.cursor()
                            cursor.execute('select  Answer from Atanaw where PersonID between  6 and 10')
                        for Answer in cursor:
                           rew = list(Answer)
                           print(Fore.RED +'' F"{rew}")
                    elif categ == 'C1':
                        cursor.execute('select Question from Atanaw where PersonID >=11')
                        row = cursor.fetchall()
                        for Question in row:
                            print(Question)
                            ans = input("please enter your answer ")
                            print("User answer is", Fore.MAGENTA + F" {ans}")
                            cursor = conn.cursor()
                            cursor.execute('select   Answer from Atanaw where PersonID >=11')
                        for Answer in cursor:
                            rew = list(Answer)
                            print(Fore.RED + F"{rew}")
                    else:
                        print("please select one catagory from(A1, B1 and C1")
                        print("Thank you")




                else:
                    break