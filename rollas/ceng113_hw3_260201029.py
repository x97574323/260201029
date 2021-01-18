def create_checker1(a):
    returner=True
    for i in list(a):
        if(not i.islower()):
            if(not i.isdigit()):
                returner=False
                break
    return returner
def create_checker2(a):
    digit=0
    letter=0
    returner=False
    if(4<len(a)<8):
        for i in list(a):
            if(digit==1 and letter==1):
                returner=True
                break
            else:
                if(digit<2):
                    if(i.isdigit()==True):
                        digit=digit+1
                if(letter<2):
                    if(i.isalpha()==True):
                        letter=letter+1
    return returner
def dosya(path):
    file = open(path, "r")
    dictionary = {}

    for i in file:
        data=i.split(";")
        data[-1]=data[-1].strip("\n")
        if(data[-1]==''):
            data.remove('')
        dictionary[data[0]]=data[1]
        data[-1] = data[-1].strip()
        dictionary[data[0]+"_friends"]=data[2:]
    file.close()
    return dictionary
def name_checker(name,dictionary):
    if (name in dictionary):
        return True
    else:
        return False
def password_checker(name,password,dictionary):
    checker=dictionary[name]
    if(checker==password):
        return True
    else:
        return False

def enter(dictionary):
    username=input("Please enter username:\n")
    if(name_checker(username,dictionary)==True):
        password=input("Please enter password:\n")
        if(password_checker(username,password,dictionary)==True):
            print("Logged in\n")
            logger=[username]
            return logger
        else:
            print("Wrong password or username\n")
    else:
        password = input("Please enter password:\n")
        print("Wrong password or username\n")
def create(dictionary,path):
    username=input("Please enter username:\n")
    if(username in dictionary):
        print("Username not valid\n")
    elif(create_checker1(username)==False):
        print("Username not valid\n")
    else:
        password = input("Please enter password:\n")
        if(create_checker2(username)==True):
            dictionary[username] = password
            dictionary[username+"_friends"]=[]
            documan=open(path,"w")
            zero=0
            one=1
            for i in dictionary:
                if(one<len(dictionary)):
                    first=list(dictionary.keys())
                    second=list(dictionary.values())
                    if(second[one]!=[]):
                        data=first[zero]+";"+second[zero]+";"+second[one][0]+"\n"
                        documan.write(data)
                    else:
                        data = first[zero] + ";" + second[zero] + ";\n"
                        documan.write(data)
                zero=zero+2
                one=one+2
            documan.close()
        else:
            print("Password not valid\n")

def add(logger,dictionary,path):

    if(logger==None):
        print("You need to log in first\n")
    else:
        friend=input("Please enter the name of your new friend:\n")
        if(friend in dictionary):
            if(dictionary[logger[0] + "_friends"]!=[]):
                dictionary[logger[0] + "_friends"] = [dictionary[logger[0] + "_friends"][0] + ","+friend]
            else:
                dictionary[logger[0] + "_friends"] = [friend]
            if (dictionary[friend + "_friends"] != []):
                dictionary[friend + "_friends"] = [dictionary[friend + "_friends"][0] + "," + logger[0]]
            else:
                dictionary[friend + "_friends"] = logger
            documan = open(path, "w")
            zero = 0
            one = 1
            for i in dictionary:
                if (one < len(dictionary)):
                    first = list(dictionary.keys())
                    second = list(dictionary.values())
                    if (second[one] != []):
                        data = first[zero] + ";" + second[zero] + ";" + second[one][0] + "\n"
                        documan.write(data)
                    else:
                        data = first[zero] + ";" + second[zero] + ";\n"
                        documan.write(data)
                zero = zero + 2
                one = one + 2
            documan.close()
        else:
            print("Friend not found\n")
def show(logger,dictionary):
    if(logger==None):
        print("You need to log in first\n")
    else:
        liste=dictionary[logger[0] + "_friends"]
        print(liste[0])

def menu():
    path = "users.txt"
    logger = None
    dictionary=dosya(path)
    while(True):
        menu_text = "1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit"
        print(menu_text)
        choice=input()
        if(choice=="1"):
            logger=enter(dictionary)
        elif(choice=="2"):
            create(dictionary,path)
        elif(choice=="3"):
            add(logger,dictionary,path)
        elif(choice=="4"):
            show(logger,dictionary)
        elif(choice=="5"):
            break
        else:
            print("Invalid option\n")
menu()