try:
    fileName = input('Enterthe file name to read: ')
    
    with open(fileName, 'rt') as file:
        fileContent = file.read()
        print('File Contents\n',fileContent)
except FileNotFoundError:
    print('File doesn\'t exist')
except PermissionError:
    print('You have no permission to read this file')
except Exception as e:
    print('Something went wrong',e)
                   