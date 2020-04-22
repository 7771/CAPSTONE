"Python code to create users and assign them to groups"

def genID(ids):

    #print(ids)  
    
    return [ids[-1]]


def person(ids,f_name, m_name, l_name, gender, age, dob, allergies,
           disabilities, medication,econtact, addr,p_num):
    full_name=[]
    full_name+=f_name,l_name
    gen=gender
    dob=dob
    allergies = allergies
    disabilities = disabilities
    medication = medication
    econtact = econtact
    addr = address
    phone = p_num
    comment=[]
    ids = genID(ids)

    persons+=(genID(),full_name,gen,dob,allergies,disabilities,medication,econtact,addr,phone,comment)
    return persons

def createChild(ids,f_name, m_name, l_name, gender, dob, allergies,
           disabilities, medication, p_num,econtact, addr,parent,children):
    parent=parent
    full_name=[]
    full_name+=f_name,l_name
    gen=gender
    dob=dob
    allergies = allergies
    disabilities = disabilities
    medication = medication
    econtact = econtact
    addr = addr
    phone = p_num
    comment=[]
    ids = genID(ids)
    children += (ids[-1],full_name,gen,dob,allergies,disabilities,medication,econtact,
                 addr,phone,parent,comment) 
    return 'successfully added', children[-1]


def createWorker(f_name, m_name, l_name, gender, dob, allergies,
                 disabilities, medication, econtact, addr, p_num):
    
    full_name = f_name, m_name, l_name
    gender = gender
    age = age
    dob = dob
    allergies = allergies
    disabilities = disabilities
    medication = medication
    emergency_contact = e_contact
    address = addr
    ids = genID(ids)
    workers += (ids,full_name, gender, age, dob, allergies,
                 disabilities, medication, econtact, addr)  
    return 'worker successfully added', worker[-1]

def attending(array):
    A_list=[]
    x=0
    for x in array:
        if retreat2020=='attending' is true:
             A_list+=x
        else:
            x+=1
            continue
    if A_list == []:
        return 'none'
    else:
        return A_list

def create(children,workers, persons,rooms, ids):
    print('Register Child     Register Worker     Set Rooms')#      Register Worker       Set Rooms')
    response=input()
    print(response)
    if response == "child":
        print("First Name: ")
        f_name=input()
        print("Middle Name: ")
        m_name = input()
        print("Last Name: ")
        l_name= input()
        print("Date of Birth: ")
        dob = input()
        print("Sex: ")
        gender=input()
        print("Allergies: ")
        allergies=input()
        print("Medication: ")
        medication=input()
        print("Disabilities: ")
        disabilities=input()
        print("Emergency Contact")
        econtact=input()
        print("Address: ")
        addr=input()
        print("Phone Number: ")
        p_num=input()
        print("Enter "+f_name+"'s parent's full name")
        parent=input()
        createChild(ids,f_name, m_name, l_name, gender, dob, allergies,
           disabilities, medication, econtact, addr,p_num,parent,children)

    
##def dormroom(age_range, gender, no_beds):
##    x=0
##    while x<=len(children) and y<=no_beds:
        
    
def main():
    x=10000
    ids=[x]
    rooms=[]
    persons=[]
    workers=[]
    children=[]

    create(children,workers, persons,rooms, ids)
    print(children)
                        
    
    
if __name__ == "__main__":
    main()
