import mysql.connector
import os
from forex_python.converter import CurrencyRates

def passwordchecker(ND,pa):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="bms")

    cur_object = con.cursor()
    query = "SELECT * FROM `register` WHERE `NID` = '" + ND + "';"
    cur_object.execute(query)

    table = cur_object.fetchall()

    if pa == table[0][6]:
        return True
    else:
        return False

def searchsender(ND):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="bms")

    cur_object = con.cursor()

    query = "SELECT * FROM register WHERE NID = '" + ND + "';"
    cur_object.execute(query)

    table = cur_object.fetchall()

    if (doesuserexist(ND)):
        print("==========================================================")
        print("***********      Sender Account is found       ***********")
        print("==========================================================")
        print("First Name     ", table[0][0])
        print("Last Name      ", table[0][1])
        print("User Name      ", table[0][2])
        print("Gender         ", table[0][3])
        print("National id    ", table[0][4])
        print("Birth Date     ", table[0][5])
        print("Account Number ", table[0][7])
        print("Money          ", table[0][8])
        print("Type           ", table[0][9])
        print("==========================================================")
    else:
        print("==========================================================")
        print("***********         User is not found          ***********")
        print("==========================================================")
    cur_object.close()
    con.close()


def searchreceiver(ND):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="bms")

    cur_object = con.cursor()

    query = "SELECT * FROM register WHERE NID = '" + ND + "';"
    cur_object.execute(query)

    table = cur_object.fetchall()

    if (doesuserexist(ND)):
        print("==========================================================")
        print("***********     Receiver Account is found      ***********")
        print("==========================================================")
        print("First Name     ", table[0][0])
        print("Last Name      ", table[0][1])
        print("User Name      ", table[0][2])
        print("Gender         ", table[0][3])
        print("National id    ", table[0][4])
        print("Birth Date     ", table[0][5])
        print("Account Number ", table[0][7])
        print("Money          ", table[0][8])
        print("Type           ", table[0][9])
        print("==========================================================")
    else:
        print("==========================================================")
        print("***********         User is not found          ***********")
        print("==========================================================")
    cur_object.close()
    con.close()

def iban(n):
    con = mysql.connector.connect( host="localhost", user="root",password="", database="bms")

    cur_object=con.cursor()

    query= "SELECT * FROM `register` WHERE `NID` = '"+n+"';"
    cur_object.execute(query)

    table = cur_object.fetchall()

    cur_object.close()
    con.close()

    BAN = "EG3800190005"+str(table[0][7])

    print("==========================================================")
    print("***********            Iban Number             ***********")
    print("==========================================================")
    print("\n",BAN)

def currencyconverter():

    cr = CurrencyRates()

    from_currency = str(input("Enter in the currency you'd like to convert from: ")).upper()

    to_currency = str(input("Enter in the currency you'd like to convert to: ")).upper()


    amount = float(input("Please enter the amount you want to convert: "))

    if(from_currency == "EGP" and to_currency == "USD"):
        val = amount * 0.052411604
    elif from_currency == "USD" and to_currency == "EGP":
        val = amount * 19.084436  
    else:
        if(from_currency == "EGP"):
            amount*=0.052407335 
            from_currency = "USD"

        if(to_currency == "EGP"):
            to_currency = "USD"
            val = cr.convert(from_currency, to_currency, amount)

            val=float(val)* 19.084436  

        else:
            val = cr.convert(from_currency, to_currency, amount)

    print(val)


def doesuserexist(ND):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="bms")

    cur_object = con.cursor()
    query = "SELECT * FROM `register` WHERE `NID` = '" + ND + "';"
    cur_object.execute(query)

    table = cur_object.fetchall()

    if len(table) == 0:
        return False
    else:
        return True


def admincheck(ND):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="bms")

    cur_object = con.cursor()

    query = "SELECT * FROM register WHERE NID = '" + ND + "';"
    cur_object.execute(query)

    table = cur_object.fetchall()
    cur_object.close()
    con.close()

    if ((table[0][9]) == "admin"):
        return True
    else:
        return False


def serchUser(ND):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="bms")

    cur_object = con.cursor()

    query = "SELECT * FROM register WHERE NID = '" + ND + "';"
    cur_object.execute(query)

    table = cur_object.fetchall()

    if (doesuserexist(ND)):
        print("==========================================================")
        print("***********           User is found            ***********")
        print("==========================================================")
        print("First Name     ", table[0][0])
        print("Last Name      ", table[0][1])
        print("User Name      ", table[0][2])
        print("Gender         ", table[0][3])
        print("National id    ", table[0][4])
        print("Birth Date     ", table[0][5])
        print("Account Number ", table[0][7])
        print("Money          ", table[0][8])
        print("Type           ", table[0][9])
        print("==========================================================")
    else:
        print("==========================================================")
        print("***********         User is not found          ***********")
        print("==========================================================")
    cur_object.close()
    con.close()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bms"
)

if (mydb):
    print("Connection Successful")

else:
    print("Connection unsuccessful")

mycursor = mydb.cursor()

while (True):

    os.system('cls')

    print("==========================================================")
    print("*********** WELCOME TO TECHNICO BANKING SYSTEM ***********")
    print("==========================================================")
    print("***********   (a)  Login as an Admin Account   ***********")
    print("***********   (b)  Login as a Client Account   ***********")
    print("***********   (e)  Quit                        ***********")
    print("==========================================================")

    EnterLetter = input("Select a Letter from the Above Box menu : ")

    os.system('cls')


    if EnterLetter == "a":
        natid = str(input("Enter Your National ID : "))
        userCheck =  doesuserexist(natid)
        
        
        ch = False
        if userCheck:
            ch = admincheck(natid)
            con = mysql.connector.connect(host="localhost", user="root", password="", database="bms")

            cur_object = con.cursor()
            query = "SELECT * FROM register WHERE `NID` = '" + natid + "'"
            cur_object.execute(query)

        else :
            print("User doesn't exist")
            mainMenu = input(" Press Enter Key to go back to Last Menu or press (z) to Quit  ")
            if (mainMenu == 'z'):
                EnterLetter = 'e'
                break
            else:
                continue

        password = str(input("Enter Your Password : "))
        pasflag = True
        if (ch == True):

            while(True):
                if(passwordchecker(natid,password)):
                    break
                else:
                    password = str(input("Password is wrong re-enter it again or press q to quite "))
                    if password == 'q':
                        EnterLetter = 'e'
                        pasflag = False
                        break

            while (pasflag):
                print("==========================================================")
                print("*********** WELCOME TO TECHNICO BANKING SYSTEM ***********")
                print("==========================================================")
                print("***********   (a)  Open new Account            ***********")
                print("***********   (b)  Search for a Client         ***********")
                print("***********   (c)  Deposit Money               ***********")
                print("***********   (d)  Withdraw Money              ***********")
                print("***********   (e)  Send Money                  ***********")
                print("***********   (f)  Currency Calculator         ***********")
                print("***********   (g)  Show IBAN                   ***********")
                print("***********   (z)  Return to main menu         ***********")
                print("==========================================================")

                EnterLetter1 = input("Select a Letter from the Above Box menu : ")

                os.system('cls')

                if EnterLetter1 == "a":
                    print("==========================================================")
                    print("***********             (a)  Admin             ***********")
                    print("***********             (b)  user              ***********")
                    print("==========================================================")

                    flag = True
                    while flag:
                        personType= input(str("Choose user type: "))

                        if(personType == "a" or personType == "b"):
                            flag = False

                    if personType == "a":
                        typ = "Admin"
                    else :
                        typ = "User"

                    if(typ == "Admin"):
                        fname = str(input("Write user Firstname : "))
                        lname = str(input("Write user Lastname : "))
                        uname = str(input("Write user Username : "))

                        print("==========================================================")
                        print("***********         Choose user Gender         ***********")
                        print("==========================================================")
                        print("==========================================================")
                        print("***********             (a)  Male              ***********")
                        print("***********             (b)  Female            ***********")
                        print("==========================================================")

                        flag = True
                        while flag:
                            genderType= input(str("Choose user type: "))

                            if(personType == "a" or personType == "b"):
                                flag = False

                        if genderType == "a":
                            gender = "Male"
                        else :
                            gender = "Female"

                        nat_id = str(input("Write user National ID : "))
                        Bdate = str(input("Write user Birth Date (yyyy/mm/dd) : "))
                        Pass = str(input("Write user Password : "))
                        Money = "NULL"
                    else:
                        fname = str(input("Write user Firstname : "))
                        lname = str(input("Write user Lastname : "))
                        uname = str(input("Write user Username : "))
                        gender = str(input("Write user Gender : "))
                        nat_id = str(input("Write user National ID : "))
                        Bdate = str(input("Write user Birth Date (yyyy/mm/dd) : "))
                        Pass = str(input("Write user Password : "))
                        Money = str(input("Write user amount of Money : "))

                    if (not(doesuserexist(nat_id))):
                        sql = "INSERT INTO `register`(`FName`, `LName`, `UName`, `Gender`, `NID`, `BDate`, `Pass`, `Money`, `Type`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                        val = (fname, lname, uname, gender, nat_id, Bdate, Pass,Money, typ)
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="bms"
                        )
                        mycursor = mydb.cursor()
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print("=================================================================")
                        print("***********   New User account created successfully  ***********")
                        print("=================================================================")
                        if(typ != "admin"):
                            sql = "SELECT `BANumber` FROM `register` WHERE `NID` = %s;"
                            val = (str(nat_id),)
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="",
                                database="bms"
                            )
                            mycursor = mydb.cursor()
                            mycursor.execute(sql , val)
                            # mydb.commit()
                            table = mycursor.fetchall()

                            print("Account Number ", str(table[0][0]))
                            print("=================================================================")
                    else:
                        print("=================================================================")
                        print("***********            User already exists           ***********")
                        print("=================================================================")

                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")

                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue

                elif EnterLetter1 == "b":
                    nat_id = str(input("Enter the national ID of user : "))
                    serchUser(nat_id)

                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")

                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue

                elif EnterLetter1 == "c":
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()

                    cnt = str(input("Enter the national ID of user : "))
                    serchUser(cnt)
                    wdrw = float(input("Enter the money to deposit : "))
                    sql = "SELECT * FROM register WHERE `NID` = '" + cnt + "'"
                    mycursor.execute(sql)
                    table = mycursor.fetchall()
                    nm = float(table[0][8]) + wdrw
                    nms = str(nm)
                    print("Your new balance is = ",nms)
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()
                    sql = "UPDATE register SET Money = '" + nms + "' WHERE NID = '" + cnt + "'"

                    mycursor.execute(sql)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")

                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue

                elif EnterLetter1 == "d":
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()

                    cnt = str(input("Enter the national ID of user : "))
                    serchUser(cnt)
                    wdrw = float(input("Enter the money to withdraw : "))
                    sql = "SELECT * FROM register WHERE `NID` = '" + cnt + "'"
                    mycursor.execute(sql)
                    table = mycursor.fetchall()
                    nm = float(table[0][8]) - wdrw
                    nms = str(nm)
                    print("Your new balance is = ",nms)
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()
                    sql = "UPDATE register SET Money = '" + nms + "' WHERE NID = '" + cnt + "'"

                    mycursor.execute(sql)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")

                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue
                
                elif EnterLetter1 == "e":
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()
                    
                    snd = str(input("Enter the national ID of the sender : "))
                    rvr = str(input("Enter the national ID of the receiver : "))

                    senderCheck =  doesuserexist(snd)
                    reciverCheck =  doesuserexist(rvr)
                    adminrecheck = admincheck(rvr)
                    flag = True
                    while(True):
                        if(senderCheck and reciverCheck and (not adminrecheck)):
                            break
                        elif reciverCheck and (not adminrecheck):
                            snd = str(input("Sender national id is wrong re-enter it again or press q to quite "))
                            if snd == 'q':
                                EnterLetter = 'e'
                                flag = False
                                break
                        elif senderCheck and not adminrecheck:
                            rvr = str(input("Reciver national id is wrong re-enter it again or press q to quite "))
                            if rvr == 'q':
                                EnterLetter = 'e'
                                flag = False
                                break
                                
                        else:
                            flag = False
                        os.system('cls')
                    if(flag):
                        searchsender(snd)
                        searchreceiver(rvr)
                        mon = float(input("Enter the money to send : "))

                        sql = "SELECT * FROM register WHERE `NID` = '" + snd + "'"
                        mycursor.execute(sql)
                        table = mycursor.fetchall()
                        sm = float(table[0][8]) - mon
                        sms = str(sm)
                        print("Sender new balance is = ", sms)
                        sql = "UPDATE register SET Money = '" + sms + "' WHERE NID = '" + snd + "'"

                        mycursor.execute(sql)

                        mydb.commit()
                        sql = "SELECT * FROM register WHERE `NID` = '" + rvr + "'"
                        mycursor.execute(sql)
                        table = mycursor.fetchall()
                        rm = float(table[0][8]) + mon
                        rms = str(rm)
                        print("Receiver new balance is = ", rms)
                        sql = "UPDATE register SET Money = '" + rms + "' WHERE NID = '" + rvr + "'"

                        mycursor.execute(sql)

                        mydb.commit()

                        mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")

                        if (mainMenu == 'z'):
                            EnterLetter = 'e'
                            break
                        else:
                            continue

                elif EnterLetter1 == "f":
                    currencyconverter()
                    
                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")
                    
                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue
                
                elif EnterLetter1 == 'g':
                    nat_id = str(input("Enter the national ID of user : "))
                    iban(nat_id)
                    print("\n\n")
                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")
                    
                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue

                elif EnterLetter1 == "z":
                    break
                os.system('cls')
        else:
            print("User is not an Admin")

        os.system('cls')


    if EnterLetter == "b":
        natid = str(input("Enter Your National ID : "))
        sql1 = "SELECT * FROM register WHERE `NID` = '" + natid + "'"
        mycursor.execute(sql1)
        ch = admincheck(natid)
        password = str(input("Enter Your Password : "))
        pasflag = True
        userCheck =  doesuserexist(natid)
        ch = True
        if userCheck:
            ch = admincheck(natid)
        else :
            print("User doesn't exist")
            mainMenu = input(" Press Enter Key to go back to Last Menu or press (z) to Quit  ")
            if (mainMenu == 'z'):
                EnterLetter = 'e'
                break
            else:
                continue
        if (ch == False):
            while(True):
                if(passwordchecker(natid,password)):
                    break
                else:
                    password = str(input("Password is wrong re-enter it again or press q to quite "))
                    if password == 'q':
                        EnterLetter = 'e'
                        pasflag = False
                        break
            while (pasflag):
                print("==========================================================")
                print("*********** WELCOME TO TECHNICO BANKING SYSTEM ***********")
                print("==========================================================")
                print("***********   (a)  Withdraw Money              ***********")
                print("***********   (b)  Send Money                  ***********")
                print("***********   (c)  Currency Calculator         ***********")
                print("***********   (d)  Show IBAN                   ***********")
                print("***********   (z)  Return to main menu         ***********")
                print("==========================================================")

                EnterLetter1 = input("Select a Letter from the Above Box menu : ")
                
                if EnterLetter1 == "a":
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()

                    cnt = str(natid)
                    serchUser(cnt)
                    wdrw = float(input("Enter the money to deposit : "))
                    sql = "SELECT * FROM register WHERE `NID` = '" + cnt + "'"
                    mycursor.execute(sql)
                    table = mycursor.fetchall()
                    nm = float(table[0][8]) + wdrw
                    nms = str(nm)
                    print("Your new balance is = ",nms)
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()
                    sql = "UPDATE register SET Money = '" + nms + "' WHERE NID = '" + cnt + "'"

                    mycursor.execute(sql)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")

                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue
                
                elif EnterLetter1 == "b":
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bms"
                    )

                    mycursor = mydb.cursor()
                    
                    snd = str(natid)
                    rvr = str(input("Enter the national ID of the receiver : "))

                    senderCheck =  doesuserexist(snd)
                    reciverCheck =  doesuserexist(rvr)
                    flag = True
                    while(True):
                        if(senderCheck and reciverCheck):
                            break
                        elif reciverCheck:
                            snd = str(input("Sender national id is wrong re-enter it again or press q to quite: "))
                            if snd == 'q':
                                EnterLetter = 'e'
                                flag = False
                                break
                        elif reciverCheck:
                            rvr = str(input("Reciver national id is wrong re-enter it again or press q to quite: "))
                            if rvr == 'q':
                                EnterLetter = 'e'
                                flag = False
                                break
                                
                        else:
                            flag = False
                        os.system('cls')
                    if(flag):
                        searchsender(snd)
                        searchreceiver(rvr)
                        mon = float(input("Enter the money to send : "))

                        sql = "SELECT * FROM register WHERE `NID` = '" + snd + "'"
                        mycursor.execute(sql)
                        table = mycursor.fetchall()
                        sm = float(table[0][8]) - mon
                        sms = str(sm)
                        print("Sender new balance is = ", sms)
                        sql = "UPDATE register SET Money = '" + sms + "' WHERE NID = '" + snd + "'"

                        mycursor.execute(sql)

                        mydb.commit()
                        sql = "SELECT * FROM register WHERE `NID` = '" + rvr + "'"
                        mycursor.execute(sql)
                        table = mycursor.fetchall()
                        rm = float(table[0][8]) + mon
                        rms = str(rm)
                        print("Receiver new balance is = ", rms)
                        sql = "UPDATE register SET Money = '" + rms + "' WHERE NID = '" + rvr + "'"

                        mycursor.execute(sql)

                        mydb.commit()

                        mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")

                        if (mainMenu == 'z'):
                            EnterLetter = 'e'
                            break
                        else:
                            continue

                elif EnterLetter1 == "c":
                    currencyconverter()
                    
                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")
                    
                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue
                
                elif EnterLetter1 == 'd':
                    iban(natid)

                    mainMenu = input(" Press Enter Key to go Back to Last Menu or press (z) to Quit  ")
                    
                    if (mainMenu == 'z'):
                        EnterLetter = 'e'
                        break
                    else:
                        continue
                
                elif EnterLetter1 == "z":
                    break
                os.system('cls')
        else:
            print("User is not a client")
        
        os.system('cls')

    elif EnterLetter == "e":
        break
    os.system('cls')

os.system('cls')