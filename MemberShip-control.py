admins = ['mahmoud', 'osama', 'ali', 'gamal']

name = input('please,enter your name : ').strip().lower()

if name in admins:
    print(f'Hello {name} , Welcome Back')
    editName = input('Do you want update your name or remove : ').lower()
    if editName == 'update' or editName == 'u':
        newName = input('Enter a new name : ')
        admins[admins.index(name)] = newName
        print(f'Name is updated {admins}')
    elif editName == 'remove' or editName == 'r':
        admins.remove(name)
        print(f'Your name have been removed {admins}')
    else:
        print('Wrong option')
else:
    print(f'Hello {name} You are not an admin ')
    status = input('Add you yes or no : ').lower()

    if status == 'y' or status == 'yes':
        admins.append(name)
        print(f'Now you are an admin , admins are : {admins}')
    else :
        print('You are nor added .')