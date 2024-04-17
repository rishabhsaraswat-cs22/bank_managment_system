import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='rishabh',database='bank')

def open_account():
                a=int(input("Enter account number: "))
                b=input("Enter Name: ")
                c=input("Enter DOB: ")
                d=int(input("Enter phone number: "))
                e=input("Enter address: ")
                f=int(input("Enter opening balance: "))
                g=int(input("Enter aadhaar number: "))
                data1=(a,b,c,d,e,f,g)
                data2=(a,b,f)
                sql1="insert into account values(%s,%s,%s,%s,%s,%s,%s)"
                sql2="insert into amount values(%s,%s,%s)"
                c=con.cursor()
                c.execute(sql1,data1)
                c.execute(sql2,data2)
                con.commit()
                print("Data Entered Successfully....!!")
                print(" "*130)
                ch=input("Want to Enter more records :")
                if ch.lower()=="yes":
                        open_account()
                else:
                        main()
        
        
def credit():
        try:
                am=int(input("Enter amount: "))
                acnm=int(input("Enter account number: "))
                x="select Balance from amount where Account_number = %s"
                data=(acnm,)
                c=con.cursor()
                c.execute(x,data)
                user=c.fetchone()
                final=user[0]+am
                sql="update amount set Balance= %s where Account_number= %s"
                d=(final,acnm)
                c.execute(sql,d)
                con.commit()
                print("Record updated successfully.....!!!!")
        except:
                print("Account doesn't exit......!!!!!")
        main()
        
def debit():
        try:
                am=int(input("Enter amount: "))
                acnm=int(input("Enter account number: "))
                x="select Balance from amount where Account_number = %s"
                data=(acnm,)
                c=con.cursor()
                c.execute(x,data)
                user=c.fetchone()
                final=user[0]-am
                sql="update amount set Balance= %s where Account_number= %s"
                d=(final,acnm)
                c.execute(sql,d)
                con.commit()
                print("Record updated successfully.....!!!!")
        except:
                print("Account doesn't exit......!!!!!")
        main()
        
def delete():
        try:
                ac=int(input("Enter account number:"))
                sql1="delete from account where Account_number= %s"
                sql2="delete from amount where Account_number= %s"
                data=(ac,)
                a=con.cursor()
                a.execute(sql1,data)
                a.execute(sql2,data)
                con.commit()
                print("Record deleted successfully....!!!")
        except:
                print("Record not found......!!!")
        main()
        
def search():
        try:
                ac=int(input("Enter Account No: "))
                a="Select*from account where Account_number= %s"
                data=(ac,)
                c=con.cursor()
                c.execute(a,data)
                user=c.fetchone()
                print(" "*260)
                print("\tAcc.no\t"," "*8,"Name"," ","\tDOB\t"," "*2,"Phone_no\t"," "*2,"Address\tOpen_Balnace\tAadhaar_no")
                print("="*130)
                for i in user:
                      print("%15s"%i,end="")
                print()
                print("="*130)
        except():
                print("Record not found......!!!!")
        main()
        
def dispsortacc():
        try:
                a="Select * from Account order by Account_number"
                c=con.cursor()
                c.execute(a)
                f="%s,%s,%s,%s,%s,%s,%s"
                print("\tAcc.no\t\tName"," ","\tDOB\t\tPhone_no\tAddress\tOpen_Balnace\tAadhaar_no")
                print("="*130)
                for i in c:
                        for j in i:
                                print("%13s"%j,end=" ")
                        print()
                print("Record sorted successfully........!!!!")
                print("="*130)
                con.commit()
        except:
                print("Table doesn't exit.....!!!")
        main()
        
def dispsortname():
        try:
                a="Select * from Account order by Name"
                c=con.cursor()
                c.execute(a)
                f="%s,%s,%s,%s,%s,%s,%s"
                print("\tAcc.no\t\tName\t\tDOB\t"," "*3,"Phn_number\t"," "*3,"Address\t"," "*3,"Open_Balnace"," "*3,"Aadhaar_no")
                print("="*130)
                for i in c:
                        for j in i:
                                print("%13s"%j,end="\t")
                        print()
                print("="*130)
                print("Record sorted successfully........!!!!")
                con.commit()
        except:
                print("Table doesn't exit.....!!!")
        main()
        
def dispsortbal():
        try:
                a="Select * from Amount order by Balance"
                c=con.cursor()
                c.execute(a)
                f="%s,%s,%s,%s,%s,%s,%s"
                print("\tAcc.no\t"," "*3,"Name\t"," "*3,"Balnace")
                print("="*130)
                for i in c:
                        for j in i:
                                print("%10s"%j,end="\t")
                        print()
                print("="*130)
                print("Record sorted successfully........!!!!")
                con.commit()
        except:
                print("Table doesn't exit.....!!!")
        main()
        
def balance():
        try:
                ac=int(input("Enter Account number: "))
                a="Select Balance from amount where Account_number= %s"
                data=(ac,)
                c=con.cursor()
                c.execute(a,data)
                user=c.fetchone()
                print("Balance for Account:",ac,"is ",user[0])
        except:
                print("Record not found.....!!!!!")
        main()
       

def update():
        try:
              c=con.cursor()
              print("\nl. Name")
              print("\n2. D-O-B")
              print('\n3. Phone no.')
              print('\n4. Opening Balance')
              choice = input('\nEnter your choice: ')
              field = ' '
              if choice == '1':
                  field = 'name'
              if choice == '2':
                  field = 'DOB'
              if choice == '3':
                  field = 'Phone_number'
              if choice == '4':
                  field = 'Opening_Balance'
              ID = input('Enter Account no: ')
              value = input('\nEnter the new value: ')
              if field =='Phone No.' or field == 'Opening Balance':
                  sql = "update account set "+ field +"= '{}' where Account_number= '{}'".format(value,ID) 
              else:
                  sql = 'update account set ' + field + ' = "'+value+'" where Account_number = '+ID+';'
              c.execute(sql)
              
              print("\n\nUser's details Updated.....")
              con.commit()
              choice1=input("Enter 1 to update another record \nEnter 2 to go to main menu\n===> ")
              if choice1=='1':
                  update()
              else:
                  main() 
        except:
              print("Record not found....!!!!")
        main()

def menu_transaction():
        print("1. Debit/withdraw from account".center(140))
        print("2. Credit/deposit account".center(140))        
        print("3. Back".center(140))
def menu_display():
        print("1. Sorted as per Account number".center(140))
        print("2. Sorted as per Customer Name".center(140))
        print("3. Sorted as per Balance".center(140))
        print("4. Balance Enquiry".center(140))
        print("5. Back".center(140))

def all_record():
       try:
             a="select * from account"
             c=con.cursor()
             c.execute(a)
             user=c.fetchall()
             print("="*130)
             print("Acno. Name"," ","DOB"," "*10,"phn_no"," "*6,"Address","  ","open_bal  Aadhaar_no.")
             for i in user:
                   print(i, end=" \n")
             print("="*130)
             print()
       except:
             print("Table is empty.....!!!")
       main()

             
       

def main():
        print("*"*266)
        print("  -----------------------------")
        print("BANKING MANAGEMENT SYSTEM".center(33))
        print("  -----------------------------")
        print("   ------------------------")
        print(" WELCOME TO MAIN MENU".center(30))
        print("   ------------------------")
        print(" "*130)
        print("1. Open new account")
        print("2. Transactions")
        print("      1. Debit/withdraw from account")
        print("      2. Credit/deposit account")
        print("3. Update record")
        print("4. Delete/close an Account")
        print("5. Search for a record")
        print("6. Display")
        print("      1. Sorted as per Account number")
        print("      2. Sorted as per Customer Name")
        print("      3. Sorted as per Balance")
        print("      4. Balance Enquiry")
        print("7. Display all present records")
        print("8. Exit")
        print("*"*266)
        ch=int(input("Enter your choice: "))
        while True:
                if ch==1:
                        open_account()
                elif ch==2:
                        menu_transaction()
                        x=int(input("Task to be performed: "))
                        if x==1:
                                debit()
                        elif x==2:
                                credit()
                        elif x==3:
                                main()
                        else:
                                print("Invalid choice....!!!!")
                elif ch==3:
                        update()
                elif ch==4:
                        delete()
                elif ch==5:
                        search()
                elif ch==6:
                        menu_display()
                        k=int(input("Enter your choice: "))
                        if k==1:
                                dispsortacc()
                        elif k==2:
                                dispsortname()
                        elif k==3:
                                dispsortbal()
                        elif k==4:
                                balance()
                        elif k==5:
                                main()
                        else:
                                print("Invalid choice....!!!!!")
                elif ch==7:
                        all_record()
                elif ch==8:
                        print("Exiting.....!!!!")
                        break
                else:
                        print("Invalid choice... Please choose the valid option....!!!!!")
                        break

def password():
      ps=input("Enter password : ")
      if ps.lower()=="rishabh":
            main()
      else:
            print("Wrong password....!!!")
            password()
password()
      
            
            
      

        
