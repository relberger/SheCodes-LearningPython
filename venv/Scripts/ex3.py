"""for i in range(51):
    if i % 7 == 0:
        print('boom')
    else:
        print(i)"""

"""for i in range(21):
    user_input = input('enter next number: ')
    if i % 7 == 0 and user_input == 'boom':
        continue
    if i != int(user_input):
        print('incorrect')
        break
    else:
        continue"""

"""turn = False
for i in range(21):
    if turn == False:
        user_input = input('enter next number: ')
        if i % 7 == 0 and user_input == 'boom':
            turn = True
        elif i != int(user_input):
            print('incorrect')
            break
        else:
            turn = True
    elif turn == True:
        if i % 7 == 0:
            print('boom')
        else:
            print(i)
        turn = False"""

for i in range(51):
    if i % 14 == 0:
        print('splat')
    if i % 7 == 0:
        print('boom')
    else:
        print(i)