import os
import platform
import mysql.connector
import pandas as pd
from pandas import DataFrame
def selection():
  db = mysql.connector.connect(user='root', password='useradmin@100', host='localhost',database='akul')
  cursor = db.cursor()
  print('-------------------------------------------------\nWELCOME TO MEDI-CAPS INTERNATIONAL SCHOOL,INDORE\n-------------------------------------------------')
  print('--------------------------\nSCHOOL MANAGEMENT SYSTEM\n--------------------------')
  print("1.STUDENT MANAGEMENT")
  print("2.EMPLOYEE MANAGEMENT")
  print("3.FEE MANAGEMENT")
  print("4.EXAM MANAGEMENT")
  ch=int(input("\nEnter ur choice (1-4) : "))
  if ch==1:
     print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
     print('a.NEW ADMISSION')
     print('b.UPDATE STUDENT DETAILS')
     print('c.ISSUE TC')
     c=input("Enter ur choice (a-c) : ")
     print('\nInitially the details are..\n')
     display1()
     if c=='a':
         insert1()
         print('\nModified details are..\n')
         display1()
     elif c=='b':
         update1()
         print('\nModified details are..\n')
         display1()
     elif c=='c':
         delete1()
         print('\nModified details are..\n')
         display1()
     else:
         print('Enter correct choice...!!')
  elif ch==2:
     print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
     print('a.NEW EMPLOYEE')
     print('b.UPDATE STAFF DETAILS')
     print('c.DELETE EMPLOYEE')
     c=input("Enter ur choice : ")
     print('\nInitially the details are..\n')
     display2()
     if c=='a':
          insert2()
          print('\nModified details are..\n')
          display2()
     elif c=='b':
          update2()
          print('\nModified details are..\n')
          display2()
     elif c=='c':
          delete2()
          print('\nModified details are..\n')
          display2()
     else:
          print('Enter correct choice...!!')
  elif ch==3:
     print('WELCOME TO FEE MANAGEMENT SYSTEM')
     print('a.NEW FEE')
     print('b.UPDATE FEE')
     print('c.EXEMPT FEE')
     c=input("Enter ur choice : ")
     print('\nInitially the details are..\n')
     display3()
     if c=='a':
          insert3()
          print('\nModified details are..\n')
          display3()
     elif c=='b':
          update3()
          print('\nModified details are..\n')
          display3()
     elif c=='c':
          delete3()
          print('\nModified details are..\n')
          display3()
     else:
          print('Enter correct choice...!!')
  elif ch==4:
     print('WELCOME TO EXAM MANAGEMENT SYSTEM')
     print('a.EXAM DETAILS')
     print('b.UPDATE DETAILS ')
     print('c.DELETE DETAILS')
     c=input("Enter ur choice : ")
     print('\nInitially the details are..\n')
     display4()
     if c=='a':
          insert4()
          print('\nModified details are..\n')
          display4()
     elif c=='b':
          update4()
          print('\nModified details are..\n')
          display4()
     elif c=='c':
          delete4()
          print('\nModified details are..\n')
          display4()
     else:
          print('Enter correct choice...!!')
  else:
     print('Enter correct choice..!!')



def insert1():
 sname=input("Enter Student Name : ")
 admno=int(input("Enter Admission No : "))
 dob=input("Enter Date of Birth(yyyy-mm-dd): ")
 cls=input("Enter class for admission: ")
 cty=input("Enter City : ")
 db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
 cursor = db.cursor()
 sql="INSERT INTO student(sname,admno,dob,cls,cty) VALUES ( '%s' ,'%d','%s','%s','%s')"%(sname,admno,dob,cls,cty)
 try:
   cursor.execute(sql)
   db.commit()
 except:
   db.rollback()
   db.close()
   #insert1()

def display1():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM student"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
     sname = c[0]
     admno= c[1]
     dob=c[2]
     cls=c[3]
     cty=c[4]
     print ("(sname=%s,admno=%d,dob=%s,cls=%s,cty=%s)" % (sname,admno,dob,cls,cty))
 except:
     print ("Error: unable to fetch data")
     db.close()

def update1():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM student"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
       sname = c[0]
       admno= c[1]
       dob=c[2]
       cls=c[3]
       cty=c[4]
 except:
   print ("Error: unable to fetch data")

 print()
 tempst=int(input("Enter Admission No : "))
 temp=input("Enter new class : ")
 try:
   sql = "Update student set cls='%s' where admno='%d'" % (temp,tempst)
   cursor.execute(sql)
   db.commit()
 except Exception as e:
   print (e)
   db.close()


def delete1():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM student"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
      sname = c[0]
      admno= c[1]
      dob=c[2]
      cls=c[3]
      cty=c[4]
 except:
   print ("Error: unable to fetch data")
   
 temp=int(input("\nEnter adm no to be deleted : "))
 try:
   sql = "delete from student where admno='%d'" % (temp)
   ans=input("Are you sure you want to delete the record(y/n) : ")
   if ans=='y' or ans=='Y':
         cursor.execute(sql)
         db.commit()
 except Exception as e:
   print (e)
   db.close()

   
def insert2():
 ename=input("Enter Employee Name : ")
 empno=int(input("Enter Employee No : "))
 job=input("Enter Designation: ")
 hiredate=input("Enter date of joining (yyyy-mm-dd): ")
 db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
 cursor = db.cursor()
 sql="INSERT INTO emp(ename,empno,job,hiredate) VALUES ( '%s' ,'%d','%s','%s')" %(ename,empno,job,hiredate)
 try:
   cursor.execute(sql)
   db.commit()
 except:
   db.rollback()
   db.close()


def display2():
 try:
   db = mysql.connector.connect(user='root',password='mann',host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM emp"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
     empno = c[0]
     ename= c[1]
     job=c[2]
     hiredate=c[3]
     print ("(empno=%d,ename=%s,job=%s,hiredate=%s)"%(empno,ename,job,hiredate))
 except:
     print ("Error: unable to fetch data")
     db.close()


def update2():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM emp"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
         empno = c[0]
         ename = c[1]
         job=c[2]
         hiredate=c[3]
 except:
   print ("Error: unable to fetch data")

 print()
 tempst=int(input("Enter Employee No : "))
 temp=input("Enter new designation : ")
 try:
   sql = "Update emp set job='%s' where empno='%d'" % (temp,tempst)
   cursor.execute(sql)
   db.commit()
 except Exception as e:
   print (e)
   db.close()


def delete2():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM emp"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
       empno = c[0]
       ename = c[1]
       job=c[2]
       hiredate=c[3]
 except:
   print ("Error: unable to fetch data")

   
 temp=int(input("\nEnter emp no to be deleted : "))
 try:
   sql = "delete from emp where empno='%d'" % (temp)
   ans=input("Are you sure you want to delete the record(y/n) : ")
   if ans=='y' or ans=='Y':
     cursor.execute(sql)
     db.commit()
 except Exception as e:
   print (e)
   db.close()


   
def insert3():
 admno=int(input("Enter adm no: "))
 fee=float(input("Enter fee amount : "))
 month=input("Enter Month: ")
 db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
 cursor = db.cursor()
 sql="INSERT INTO fee(admno,fee,month) VALUES ( '%d','%d','%s')"%(admno,fee,month)
 try:
   cursor.execute(sql)
   db.commit()
 except:
   db.rollback()
   db.close()



def display3():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM fee"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
         admno= c[0]
         fee=c[1]
         month=c[2]
         print ("(admno=%d,fee=%s,month=%s)" % (admno,fee,month))
 except:
         print ("Error: unable to fetch data")
         db.close()




def update3():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM fee"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
         admno= c[0]
         fee=c[1]
         month=c[2]
 except:
   print ("Error: unable to fetch data")

 print()
 tempst=int(input("Enter Admission No : "))
 temp=input("Enter new month : ")
 try:
   sql = "Update fee set month='%s' where admno='%d'" % (temp,tempst)
   cursor.execute(sql)
   db.commit()
 except Exception as e:
   print (e)
   db.close()



def delete3():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM fee"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
         admno= c[0]
         fee=c[1]
         month=c[2]
 except:
   print ("Error: unable to fetch data")


 temp=int(input("\nEnter admno to be deleted : "))
 try:
   sql = "delete from fee where admno='%d'" % (temp)
   ans=input("Are you sure you want to delete the record(y/n) : ")
   if ans=='y' or ans=='Y':
     cursor.execute(sql)
     db.commit()
 except Exception as e:
   print (e)
   db.close()



def insert4():
 sname=input("Enter Student Name : ")
 admno=int(input("Enter Admission No : "))
 per=float(input("Enter percentage : "))
 res=input("Enter result: ")
 db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
 cursor = db.cursor()
 sql="INSERT INTO exam(sname,admno,per,res) VALUES ('%s','%d','%f','%s')"%(sname,admno,per,res)
 try:
   cursor.execute(sql)
   db.commit()
 except:
   db.rollback()
   db.close()



def display4():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM exam"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
         sname = c[0]
         admno = c[1]
         per=c[2]
         res=c[3]
         print ("(sname=%s,admno=%d,per=%f,res=%s)"%(sname,admno,per,res))
 except:
         print ("Error: unable to fetch data")
         db.close()



def update4():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM exam"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
         sname = c[0]
         admno = c[1]
         per=c[2]
         res=c[3]
         
 except:
         print ("Error: unable to fetch data")

 print()
 tempst=int(input("Enter Admission No : "))
 temp=input("Enter new result : ")
 try:
   sql = "Update exam set res='%s' where admno='%d'" % (temp,tempst)
   cursor.execute(sql)
   db.commit()
 except Exception as e:
   print (e)
   db.close()



def delete4():
 try:
   db = mysql.connector.connect(user='root', password='mann', host='localhost',database='akul')
   cursor = db.cursor()
   sql = "SELECT * FROM exam"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
         sname = c[0]
         admno= c[1]
         per=c[2]
         res=c[3]
 except:
   print ("Error: unable to fetch data")

 temp=int(input("\nEnter adm no to be deleted : "))
 try:
   sql = "delete from exam where admno='%d'" % (temp)

   ans=input("Are you sure you want to delete the record(y/n) : ")
   if ans=='y' or ans=='Y':
     cursor.execute(sql)
     db.commit()
 except Exception as e:
   print (e)
   db.close()
   
selection()
def runAgain():
 runAgn = input("\nwant To Run Again Y/n: ")
 while(runAgn.lower() == 'y'):
     if(platform.system() == "Windows"):
         print(os.system('cls'))
     else:
         print(os.system('clear'))
     selection()
     runAgn = input("\nwant To run again Y/n:")
runAgain()
  
