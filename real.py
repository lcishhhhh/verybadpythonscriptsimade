import time

stop = 0
pin = 900
real = 0
while not stop == 1:
    test = input('Insert command, say help for commands: ')
    if test.lower() == 'help':
        print('Commands:')
        print('stop')
        print('guess')
    elif test.lower() == 'stop':
     break
    elif test.lower() == 'guess':
        while not pin == real:
            time.sleep(0.001)
            real = real + 1
            print(real)
        else:
            print(f'found pass, {real}')