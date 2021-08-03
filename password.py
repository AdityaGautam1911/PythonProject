import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='123456',database='old')
cur = conn.cursor()



print("#####################################################################################################################")
print('##################################  WELCOME TO AA EMPLOYEE MANAGEMENT SYSTEM  #######################################')
print("#####################################################################################################################")



import datetime as dt
print("DATE       TIME")
print(dt.datetime.now())
print('')
print('')
print('1.CREATE AN ACCOUNT')
print('')
print('2.SIGN IN')
print('')

while True:
     n=input('enter your choice=')
     if n=='1':
          name=input('CHOOSE A USERNAME----->')
          print()
          while True:
               passwd=input('CHOOSE A 4 DIGIT PASSWORD----->')
               if len(passwd)!=4:
                    print(">>>INVALID!!")
                    continue
               if passwd.isalpha():
                    print(">>>INVALID!!")
                    continue
               else:
                    break
          V_SQLInsert="INSERT  INTO log_id (user_id,password) values (" +  str (passwd) + ",' " + name + " ') "
          cur.execute(V_SQLInsert)
          conn.commit()
          print()
          print('USER ID CREATED SUCCESSFULLY!!!')
          import mainp
          break


     if n=='2' :
          name=input('ENTER YOUR USERNAME----->')
          passwd=int(input('ENTER YOUR PASSWORD----->'))
          V_Sql_Sel="select * from log_id where password='"+str (passwd)+"' and user_id=  ' " +name+ " ' "
          cur.execute(V_Sql_Sel)
          if cur.fetchall() is  None:
               print('INVALID ID OR PASSWORD!!!')
          else:
               print()
               import mainp