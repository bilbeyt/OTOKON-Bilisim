def write_menu():
    print "1.Add Record"
    print "2.Update Record"
    print "3.Delete Record"
    print "4.Search Record"
    print "5.Print Records"
    print "6.Exit"

def make_operations(c, phonebook):
    end = False
    while(end == False):
        if(c == 1):
            add(phonebook)
            break
        elif(c == 2):
            update(phonebook)
            break
        elif (c==3):
            delete(phonebook)
            break
        elif (c==4):
            search(phonebook)
            break
        elif (c==5):
            print_records(phonebook)
            break
        elif(c==6):
            end = True
            break
        else:
            write_menu()
            c = input("Wrong input. Please reenter one of the followings (1,2,3,4,5):\n")
            make_operations(c, phonebook)
            break
    return end

def add(phonebook):
    name = raw_input("Enter the name of the person\n")
    phonenumber = input("Enter the phone number of the person\n")
    add_record(phonebook,name,phonenumber)

def update(phonebook):
    name = raw_input("Enter the name of the person\n")
    count = search_record(phonebook,name)
    if(count==0):
        print "There is no record in the phonebook about "+name
    else:
        if(count == 1):
            print "The record has been found"
        elif(count>1):
            print "Records have been found. Please select one"
        index = input("Enter the selection\n")
        new_name = raw_input("Enter the name of the person\n")
        phonenumber = input("Enter the phone number of the person\n")
        update_record(phonebook,new_name,phonenumber,name)

def delete(phonebook):
    name = raw_input("Enter the name of the person to delete\n")
    count = search_record(phonebook,name)
    if(count == 0):
        print "There is no record in the phonebook about "+name
    else:
        if(count == 1):
            print "The record has been found\n"
        elif(count>1):
            print "Records have been found. Please select one"
        index = input("Enter the selection")
        delete_record(phonebook,name,index)

def search(phonebook):
    name = raw_input("Enter the name of the person to search\n")
    count = search_record(phonebook,name)
    if(count == 0):
        print "There is no record in the phonebook about "+name

def main():
    phonebook = []
    read_from_file(phonebook)
    end = False
    while(end == False):
        write_menu()
        command = input("Select one operation\n")
        end = make_operations(command,phonebook)
    write_to_file(phonebook)


def read_from_file(phonebook):
    with open("phonebook.txt", "r") as f:
        data = f.readlines()
    for line in data:
        words = line.split(",")
        add_record(phonebook, words[0].rstrip(), words[1].rstrip())

def write_to_file(phonebook):
    with open("phonebook.txt", "w") as f:
        for i in xrange(len(phonebook)):
            contact = phonebook[i]
            f.write(str(phonebook[i].values()[1])+","+str(phonebook[i].values()[0]))
            f.write("\n")

def add_record(phonebook,name,phonenumber):
    contact = {
        "name": name,
        "phone" : phonenumber
    }
    phonebook.append(contact)

def update_record(phonebook,newname,phonenumber,name):
    for i in xrange(len(phonebook)):
        if(phonebook[i]["name"] == name):
            index = i
            break
    del phonebook[index]
    add_record(phonebook,newname,phonenumber)

def delete_record(phonebook, name):
    for i in xrange(len(phonebook)):
        if(phonebook[i]["name"] == name):
            index = i
            break
    del phonebook[index]

def search_record(phonebook, name):
    count = 0
    for i in xrange(len(phonebook)):
        if(phonebook[i]["name"].lower()== name.lower()):
            print "{}. Name: {} Phone: {}".format(count+1, phonebook[i].values()[1], phonebook[i].values()[0])
            count += 1
    return count

def print_records(phonebook):
    count = 1
    newlist = sorted(phonebook, key = lambda k: k['name'])
    for i in xrange(len(phonebook)):
        print "{}. Name: {} Phone: {}".format(count, newlist[i].values()[1], newlist[i].values()[0])
        count += 1
__name__ = main()
