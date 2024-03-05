import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="9437",database='parkingsys') 
mycursor=mydb.cursor()

def Menu():
    print("Enter 1 : To Add Parking Details")
    print("Enter 2 : To View Parking Details")
    print("Enter 3 : To Add Vehicle Details")
    print("Enter 4 : To Remove Vehicle Record")
    print("Enter 5 : To see the details of Vehicle")
    print("Enter 6 : To exit")
    input_dt = int(input("Please Select An Above Option: "))
    if input_dt== 1:
        Add_Record()
    elif input_dt== 2:
        Rec_View()
    elif input_dt== 3:
        Vehicle_Detail()
    elif input_dt== 4:
        remove()
    elif input_dt== 5:
        Vehicle_View()
    elif input_dt== 6:
        exit()
    else:
        print("Invalid option entered...")
        runAgain()


def runAgain():
    if_run=input('If you want to run Again (yes/no):')
    if if_run.lower()=='yes':
        Menu()




def Add_Record():
    L =[]
    id=int(input("Enter the parking number : "))
    L.append(id)
    pname=input("Enter the Parking Name: ")
    L.append(pname)
    level=input("Enter level of parking : ")
    L.append(level)
    freespace=input("Is there any freespace or not(yes/no): ")
    L.append(freespace)
    vehicleno=input("Enter the Vehicle Number : ")
    L.append(vehicleno)
    nod=int(input("Enter total number of days for parking: "))
    L.append(nod)
    Payment = 20*nod
    L.append(Payment)
    sql='insert into parkmaster(pid,pnm,level,freespace,vehicleno,nod,payment) values(%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql,L)
    mydb.commit()
    del(L)
    if_record = input("If you want to add more parking details(yes/no):")
    if if_record.lower()=='yes':
        Add_Record()
    else :
        Menu()


def Rec_View():
    print("Select the search criteria : ")
    print("1. Parking ID")
    print("2. Parking Name")
    print("3. Level Number")
    ch=int(input("Enter the choice : "))

    if ch==1:
        s=int(input("Enter Parking ID : "))
        rl=[s]
        sql="select * from parkmaster where pid=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()

    elif ch==2:
        s=input("Enter Parking Name : ")
        rl=[s]
        sql="select * from parkmaster where pnm=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()

    elif ch==3:
        s=int(input("Enter Level of Parking : "))
        rl=[s]
        sql="select * from parkmaster where level=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        
    for x in res:
        print('Parking Id :',x[0])
        print('Parking Name :',x[1])
        print('Level :',x[2])
        print('Freespace(Y/N) :',x[3])
        print('Vehicle Number :',x[4])
        print('Number of days for parking :',x[5])
        print('Payment :',x[6])
    print('Task completed')
    rl.pop()
    if_view = input("If you want to view more parking details(yes/no):")
    if if_view.lower()=='yes':
        Rec_View()



def Vehicle_Detail():
    X=[]
    vid=int(input("Enter Vehicle No : "))
    X.append(vid)
    vnm=input("Enter Vehicle Name/Model Name : ")
    X.append(vnm)
    dateofpur=input("Enter Year-Month-date of purchase : ")
    X.append(dateofpur)
    sql="insert into vehicle_record(pid,vehiclename,dateofpur) values(%s,%s,%s)"
    mycursor.execute(sql,X)
    mydb.commit()
    X.pop()
    if_details = input("If you want to add more vehicle details(yes/no):")
    if if_details.lower()=='yes':
        Vehicle_Detail()

def remove():
    vid=int(input("Enter the vehicle number of the vehicle to be deleted : "))
    Y = [vid]
    sql="Delete from vehicle_record where pid=%s"
    mycursor.execute(sql,Y)
    mydb.commit()
    print('Removed as per the command')
    Y.pop()
    if_remove = input("If you want to delete more vehicle details(yes/no):")
    if if_remove.lower()=='yes':
        remove()


def Vehicle_View():   
    vid=int(input("Enter the vehicle number of the vehicle whose details is to be viewed : "))
    sql="select * from vehicle_record where pid=%s"
    T =[vid]
    print('The following are the detailes you wanted:')
    mycursor.execute(sql,T)
    res=mycursor.fetchall()
    for x in res:
        print('Parking Id :',x[0])
        print('Vehicle name :',x[1])
        print('Date of purchase :',x[2])
    print('Task compelted')
    T.pop()
    if_view = input("If you want to view more vehicle details(yes/no):")
    if if_view.lower()=='yes':
        Vehicle_View()

Menu()
