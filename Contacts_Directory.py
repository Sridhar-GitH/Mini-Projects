import sys

def phonebook():
    outer_matrix = []
    rows,col = int(input('\nhow many contacts do you want : ')),5
    for i in range(rows):
        temp = []

        print('\'!\' means it\'s MANDATORY to enter a given column ')
        print(f'Enter your {i+1} contact ')

        for j in range(col):
            if j == 0:
                temp.append(str(input('NAME ! : ')))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit('name must be enter \n\tRun again :(')

            elif j == 1 :
                temp.append(int(input('NUMBER ! : ')))

            elif j == 2:
                temp.append(str(input('MAIL : ')))
                if temp[j] == '' or temp[j] == ' ':
                    temp [j] = None

            elif j == 3:
                temp.append(str(input('Date Of Birth (dd/mm/yyyy) : ')))
                if temp[j] == '' or temp[j] == ' ':
                    temp [j] = None

            elif j == 4:
                temp.append(str(input('Category (Family/Friends/Work/Others) : ')))
                if temp[j] == '' or temp[j] == ' ':
                    temp [j] = None

        outer_matrix.append(temp)

    print(outer_matrix)
    return outer_matrix

def menu (arg):
    print('\nENTER A INT TO SELECT GIVEN OPTIONS '
                       '\n1. add new contact '
                       '\n2. remove contact '
                       '\n3. delete all '
                       '\n4. search '
                       '\n5. display'
                       '\n6. exit')
    choice = int(input('\nENTER : '))

    return choice

def add_contact(arg):
    temp_1 =[]
    for j in range(len(arg[0])):
        if j == 0:
            temp_1.append(str(input('NAME ! : ')))
            if temp_1[j] == '' or temp_1[j] == ' ':
                sys.exit('name must be enter \n\tRun again :(')

        elif j == 1:
            temp_1.append(int(input('NUMBER ! : ')))

        elif j == 2:
            temp_1.append(str(input('MAIL : ')))
            if temp_1[j] == '' or temp_1[j] == ' ':
                temp_1[j] = None

        elif j == 3:
            temp_1.append(str(input('Date Of Birth (dd/mm/yyyy) : ')))
            if temp_1[j] == '' or temp_1[j] == ' ':
                temp_1[j] = None

        elif j == 4:
            temp_1.append(str(input('Category (Family/Friends/Work/Others) : ')))
            if temp_1[j] == '' or temp_1[j] == ' ':
                temp_1[j] = None

    arg.append(temp_1)
    return arg

def remove_contact(arg):
    remove_name = str(input('which name you want to remove : '))
    non = 0

    for i in range (len(arg)):
        if remove_name == arg[i][0]:
            non += 1
            print(arg.pop(i))
            print('it\'s removed ')
            return arg

    if non == 0:
       print(f'{remove_name} is not there , enter valid name')
       return arg

def delete_all_contacts(arg):

    return arg.clear()

def searching(arg):
    not_there = -1
    dummy = []
    options = int(input('\nwhich option do you want to search'
                    '\n1. NAME'
                    '\n2. NUMBER'
                    '\n3. MAIL'
                    '\n4. D.O.B (dd/mm/yyyy)'
                    '\n5. category (family/friends/work/others)'
                    '\nEnter : '))

    if options == 1:
        name = input('which name u want to search : ')
        for i in range(len(arg)):
            if name == arg[i][0]:
                not_there +=1
                dummy.append(arg[i])
                
    elif options == 2:
        number = int(input('which number u want to search : '))
        for i in range(len(arg)):
            if number == arg[i][1]:
                not_there +=1
                dummy.append(arg[i])


    elif options == 3:
        mail = int(input('which mail u want to search : '))
        for i in range(len(arg)):
            if mail == arg[i][2]:
                not_there +=1
                dummy.append(arg[i])


    elif options == 4:
        d_o_b = int(input('which D.O.B u want to search : '))
        for i in range(len(arg)):
            if d_o_b == arg[i][3]:
                not_there +=1
                dummy.append(arg[i])


    elif options == 5:
        category = int(input('which number u want to search : '))
        for i in range(len(arg)):
            if category == arg[i][4]:
                not_there += 1
                dummy.append(arg[i])

    else:
        print('criteria is invalid')
        return -1

    if not_there == -1:
        return -1
    else:
        display_all_contacts(dummy)
        return not_there

def display_all_contacts(arg):
    if not arg:
        print('it\'s empty []')
    else:
        for i in range(len(arg)):
            print(arg[i])

def thanks():
    print('...........*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..............'
          '\n\t\t\t\tTHANK YOU '
              '\n\t\t:)'
      '\n...........*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..............')
    sys.exit('GOOD BYE :)')


print('\n...........*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..............'
          '\n\tHello dear user, welcome to our smartphone directory system'
              '\n\t\tYou may now proceed to explore this directory'
      '\n...........*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..............')

if __name__ == '__main__':
    choices = 1
    arg = phonebook()

    while choices in (1,2,3,4,5):
        choices = menu(arg)
        if choices == 1:
           arg = add_contact(arg)
        elif choices == 2:
            arg = remove_contact(arg)
        elif choices == 3:
            arg = delete_all_contacts(arg)
        elif choices == 4:
            some = searching(arg)
            if some == -1:
                print('the entered variable is not there try again ')
        elif choices == 5:
           display_all_contacts(arg)
        else:
            thanks()
