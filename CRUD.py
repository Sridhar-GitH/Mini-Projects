import mysql.connector
from tabulate import tabulate
import sys

try:
    DB = mysql.connector.connect(
            host="localhost",
            user="root",
            password='1234',
            auth_plugin='mysql_native_password',
            database="trailing_py"
        )

    if DB.is_connected():
        def Create(ID, Name, Gender, Age, Status, Interested_subjects, Fav_items,
                   Purchasing):
            cursor = DB.cursor()
            Q1 = 'insert into Management (ID, Name, Gender, Age, Status,' \
                 'Interested_subjects, Fav_items,Purchasing) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(Q1, (ID, Name, Gender, Age, Status, Interested_subjects, Fav_items,Purchasing))
            DB.commit()
            print('\n given data created successfully '.title())


        def Read():
            cursor = DB.cursor()
            Q1 = 'select * from Management'
            cursor.execute(Q1)
            fetching = cursor.fetchall()
            DB.commit()
            print("\n",
                  tabulate(fetching, headers=['ID', 'Name', 'Gender', 'Age', 'Status',
                                              'Interested_subjects', 'Fav_items',
                                              'Purchasing'],tablefmt="fancy"))


        def Update(User_update):
            if User_update == 1:
                old_id = int(input('enter the old id : '.title()))
                new_id = int(input('enter the new id : '.title()))
                cursor = DB.cursor()
                Query = 'update Management set ID = %s where ID = %s'
                cursor.execute(Query, (old_id, new_id))
                print('\nthe given id is update successfully '.title())

            if User_update == 2:
                id = int(input('enter the id to change name : '.title()))
                name = input('enter the new name : '.title())
                cursor = DB.cursor()
                Query = 'update Management set Name = %s where Id = %s'
                cursor.execute(Query, (name, id))
                print('\nthe given name is update successfully '.title())

            if User_update == 3:
                id = int(input('enter the id to change name : '.title()))
                gender = input('enter the gender : '.title())
                cursor = DB.cursor()
                Query = 'update Management set gender = %s where ID = %s'
                cursor.execute(Query, (gender, id))
                print('\nthe given gender is update successfully '.title())

            if User_update == 4:
                id = int(input('enter the id to change name : '.title()))
                age = input('enter the age : '.title())
                cursor = DB.cursor()
                Query = 'update Management set age = %s where ID = %s'
                cursor.execute(Query, (age, id))
                print('\nthe given age is update successfully '.title())

            if User_update == 5:
                id = int(input('enter the id to change name : '.title()))
                status = input('enter the status : '.title())
                cursor = DB.cursor()
                Query = 'update Management set status = %s where ID = %s'
                cursor.execute(Query, (status, id))
                print('\nthe given status is update successfully '.title())

            if User_update == 6:
                id = int(input('enter the id to change name : '.title()))
                Interested_subjects = input('enter the Interested_subjects : '.title())
                cursor = DB.cursor()
                Query = 'update Management set Interested_subjects = %s where ID = %s'
                cursor.execute(Query, (Interested_subjects, id))
                print('\nthe given Interested_subjects is update successfully '.title())

            if User_update == 7:
                id = int(input('enter the id to change name : '.title()))
                Fav_items = input('enter the Fav_items : '.title())
                cursor = DB.cursor()
                Query = 'update Management set Fav_items = %s where ID = %s'
                cursor.execute(Query, (Fav_items, id))
                print('\nthe given Fav_items is update successfully '.title())

            if User_update == 8:
                id = int(input('enter the id to change name : '.title()))
                Purchasing = input('enter the Purchasing : '.title())
                cursor = DB.cursor()
                Query = 'update Management set Purchasing = %s where ID = %s'
                cursor.execute(Query, (Purchasing, id))
                print('\nthe given Purchasing is update successfully '.title())


        def Delete(User_delete):
            cursor = DB.cursor()
            Query = 'delete from Management where ID = {}'.format(User_delete)
            cursor.execute(Query)
            DB.commit()
            print('\nthe given id is deleted successfully'.title())


        print(""" 
        
          ------------------------------------------------------
         |======================================================| 
         |=========== Welcome To Management System	============|
         |======================================================|
          ------------------------------------------------------\n
        """)

        while True:
            User = input('\nCreate a "Management" Data   --> Enter "C"'
                         '\nRead The "Management" Data   --> Enter "R"'
                         '\nUpdate The "Management" Data --> Enter "U"'
                         '\nDelete The "Management" Data --> Enter "D"'
                         '\n\n       TO EXIT ===> Enter "E"'
                         '\nENTER : ')

            if User.lower() == 'c':
                ID = int(input('enter the Unique Id as a (INT) : '.title()))
                Name = input('enter the name : '.title())
                Gender = input('enter the gender (male,female,others) : '.title())
                Age = int(input('enter the age as a (INT) : '.title()))
                Status = input('enter the Status (student,teacher,employee) : '.title())
                Interested_subjects = input('enter the Interested_subjects : '.title())
                Fav_items = input('enter the Fav_items : '.title())
                Purchasing = input('enter the Purchasing : '.title())

                Create(ID, Name, Gender, Age, Status, Interested_subjects, Fav_items,
                       Purchasing)

            elif User.lower() == 'r':
                Read()

            elif User.lower() == 'u':
                User_update = int(input('\nwhich data want to update'
                                        '\n(1) id'
                                        '\n(2) name'
                                        '\n(3) gender'
                                        '\n(4) age'
                                        '\n(5) status'
                                        '\n(6) interested_subjects'
                                        '\n(7) fav_items'
                                        '\n(8) purchasing'
                                        '\n enter : '.title()))
                Update(User_update)

            elif User.lower() == 'd':
                User_delete = int(input('enter the id want to delete from management : '.title()))
                Delete(User_delete)

            elif User.lower() == 'e':
                sys.exit('THANK YOU :)')

            else:
                print('\ninvalid character please enter given characters'.title())

except mysql.connector.Error as e:
    print('ERROR :( ,While connecting to MySQL... : ',e)

finally:
    if DB.is_connected():
        DB.cursor().close()
        DB.close()
        print('MySQL connection is closed'.title())
