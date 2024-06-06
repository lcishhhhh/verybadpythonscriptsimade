import os
import time

register = False
name = 'placeholder'
password = 'placeholder'
login = False
showdays = True # shows the amount of days

available_user = {'deez', 'nuts'}
balance = '5000'
bills = 0
while not register == True:
    print("account registration")
    print("")
    finalname = input("please enter your name: ")
    finalpassword = input("please enter your password: ")
    os.system("cls")
    name = finalname
    password = finalpassword
    register = True
else:
    while True:
        if login == True:
            d = 1
            while d == 1:
                real = input(
                    f"hello, {name}, your balance is {balance} rotokens and you have {bills} rotokens worth of bills, type help for commands: ")
                try:
                    if real == 'help':
                        print('Commands:')
                        print('withdraw')
                        print('deposit')
                        print('paybills')
                        print('loan')
                        print('wait')
                        print('transfer')
                        print('logout')
                        print('exit')
                    elif real == 'deposit':
                        finish = 0
                        while not finish == 1:
                            print('how much would you like to deposit: ')
                            amount = input()
                            if amount == 'exit':
                                finish = 1
                                os.system('cls')
                                break
                            elif amount:
                                j = (float(balance) + float(amount))
                                if j:
                                    balance = int(j)
                                    print(f'current balance is {balance}')
                                    print('type exit to leave this menu')

                    elif real == 'withdraw':
                        finish = 0
                        while not finish == 1:
                            print('how much would you like to withdraw: ')
                            amount2 = input()
                            if amount2 == 'exit':
                                finish = 1
                                os.system('cls')
                                break
                            elif amount2:
                                try:
                                    j = (float(balance) - float(amount2))
                                    if j:
                                        balance = int(j)
                                        print(f'current balance is {balance}')
                                        print('type exit to leave this menu')
                                except:
                                    print("please enter a number")
                    elif real == 'paybills':
                        done = 0
                        while not done == 1:
                            h = input(
                                f'you currently have {bills} rotokens worth of bills, would you like to pay them all (Y/N)')
                            if h.lower() == 'y':
                                v = (float(balance) - float(bills))
                                balance = int(v)
                                bills = int(float('0'))
                                print('type n to exit')
                            elif h.lower() == 'n':
                                done = 1
                                os.system('cls')
                                break
                    elif real == 'loan':
                        d = 0
                        while not d == 1:
                            loanamount = input(
                                'how much would you want to loan, it will be added to your bills wih a 2% interest: ')
                            if loanamount == 'exit':
                                os.system('cls')
                                d = 1
                                break
                            else:
                                try:
                                    hh = (float(loanamount) * float(0.02)) + float(loanamount)
                                    jj = int(float(bills)) + int(hh)
                                    bills = jj
                                    final = int(balance) + int(loanamount)
                                    balance = final
                                    print('type exit to leave this menu')
                                    print(
                                        f'you have gotten a loan of {loanamount}, your current balance is {balance} and your bills is {bills}')
                                except:
                                    print("please enter a number")
                    elif real == 'wait':
                        f = 0
                        while f == 0:
                            daystowait = input("how many days would you like to wait: ")
                            if daystowait == 'exit':
                                os.system('cls')
                                break
                            else:
                                waited = 0
                                try:

                                    while not waited == int(daystowait):
                                        try:
                                            interestj = (float(balance) * float(0.02))
                                            final = int(balance) + int(interestj)
                                            balance = final
                                            j = waited + 1
                                            waited = j
                                            if showdays == True:
                                                print(f'Day {waited}, {balance} Current rotokens')
                                        except:
                                            print("please enter a number")
                                            break
                                except:
                                    print("please enter a number")
                                else:
                                    print(f"you have waited {waited} days, type exit to leave this menu")
                    elif real == 'logout':
                        os.system('cls')
                        login = False
                        break
                    elif real == 'transfer':
                        while True:
                            print('people you can transfer money to: ')
                            for i in available_user:
                                print(i)
                            prompt = input('please enter a name to transfer: ')
                            if prompt == 'exit':
                                os.system('cls')
                                break
                            elif prompt in available_user:
                                os.system('cls')
                                prompt2 = input(f'how much would you like to transfer to {prompt} : ')
                                transferred = float(balance) - float(prompt2)
                                balance = int(transferred)
                                print(f'transferred {prompt2} to {prompt}, your balance is {balance}, type exit to leave this menu')

                    elif real == 'exit':
                        d = 0
                        exit(-1)
                except:
                    print("invalid input")
        else:
            confirm = input("would you like to login, y/n: ")
            try:
                if str(confirm.lower()) == 'y':
                    print("login")
                    print("")
                    accountname = input("please enter your account name: ")
                    try:
                        if accountname == name:
                            print("correct name")
                            accountpassword = input("please enter your password: ")
                            if accountpassword == password:
                                os.system("cls")
                                print("correct password")
                                login = True
                            else:
                                os.system("cls")
                                print("invalid info")
                        else:
                            os.system("cls")
                            print("invalid info")
                    except:
                        print("invalid information, please try again")
                elif str(confirm.lower()) == 'n':
                    break
            except:
                print("invalid input")
