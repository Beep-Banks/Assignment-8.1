import os

def main():

    directory = input("Enter the directory you want to put the file: ")
    filename = input("What would you like to name the file: ")
    name = input("Enter your name: ")
    address = input('Enter your address: ')
    phone_number = input("Enter your phone number: ")

    if os.path.isdir(directory):
        
        writeFile = open(os.path.join(directory,filename), 'w')

        writeFile.write(name + ',')

        writeFile.write(address + ',')

        writeFile.write(phone_number)

        writeFile.close()

        print('File contents:')

        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry, that directory does not exist.")

main()

