import time
print("\t\t\t", time.ctime())



import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', password='123456', database='old')
mycursor = conn.cursor()



def menu():
    print("######################################################################")
    print("###################  AA EMPLOYEE MANAGEMENT FORUM  ###################")
    print("######################################################################")
    c = 'yes'
    c = input("do you want to continue or not?----->(y/n):")

    while (c == 'y' or c=='Y'):
        print("1.EMPLOYEE REGISTRATION")
        print("2.EMPLOYEE DETAILS")
        print("3.UPDATE EMPLOYEE SALARY")
        print("4.NAME LIST OF ALL EMPLOYEES")
        print("5.TOTAL STRENGTH OF COMPANY")
        print("6.EMPLOYEE WORK EXPERIENCE")
        print("7.CHECK CURRENT SALARY OF EMPLOYEE")
        print("8.ABOUT US")
        choice = eval(input("ENTER THE CHOICE----->"))

        if choice == 1:
            register()
        elif choice == 2:
            details()
        elif choice == 3:
            em_salary()
        elif choice == 4:
            em_list()
        elif choice == 5:
            em_count()
        elif choice == 6:
            em_perform()
        elif choice == 7:
            salary()
        elif choice == 8:
            about()
        else:
            print("exit")
            break
    if c=='n' or c=='N':
        print("YOU CHOSE NOT TO CONTINUE")
        print("THANK YOU")
    if c!="y" and c!="n" and c!="Y" and c!="N":
        print("please choose from (y/n) only!!!")
        menu()



def register():
    import random
    v_em_no = random.randint(1,99999)
    print("employee id is----->", v_em_no)
    v_em_name = input("enter employee name----->")
    print("1.IT ENGG.")
    print("2.HR DEPT.")
    print("3.CLERK")
    print("4.SENIOR DEVELOPER")
    print("5.MARKETING MANAGER")
    v_em_dept = input("enter department of employee-----> ")

    if v_em_dept=="1":
        v_em_dept='IT ENGG.'
    elif v_em_dept=="2":
        v_em_dept='HR DEPT.'
    elif v_em_dept=="3":
        v_em_dept='clerk'
    elif v_em_dept=="4":
        v_em_dept='SENIOR DEVELOPER'
    elif v_em_dept=="5":
        v_em_dept="MARKETING MANAGER"
    else:
        print("please choose from the above options!!!")
        register()

    print("the chosen department was----->", v_em_dept)
    v_em_salary = input("enter employee salary:")
    v_em_age = eval(input("enter employee age:"))
    v_sql_insert = "insert into office values(" + str(v_em_no) + ",'" + v_em_name + "','" + v_em_dept + "'," + str(
        v_em_salary) + "," + str(v_em_age) + ")"
    mycursor.execute(v_sql_insert)
    conn.commit()
    print("congrats,employee has been registered successfully!!!")
    print("       registered successfully!!!          ")



def details():
    mycursor.execute("select * from OFFICE")
    results = mycursor.fetchall()
    conn.commit()
    for x in results:
        print("#########################################################")
        print(x)
    print("#########################################################")



def em_salary():
    print("what would you like to do??" )
    print("1.INCREASE EMPLOYEE SALARY")
    print("2.DEDUCT EMPLOYEE SALARY")
    sal=eval(input("----->"))

    if sal==1:
        ID = input("enter employee ID")
        print("1) 5% hike")
        print("2) 10% hike")
        print("3) 15% hike")
        print("4) 25% hike")
        hike = eval(input("select how much salary hike would you like to give??----->"))
        if hike==1:
            mycursor.execute("update office set em_salary=em_salary+em_salary*5/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was increased by 5%!!!")
        elif hike==2:
            mycursor.execute("update office set em_salary=em_salary+em_salary*10/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was increased by 10%!!!")
        elif hike==3:
            mycursor.execute("update office set em_salary=em_salary+em_salary*15/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was increased by 15%!!!")
        elif hike==4:
            mycursor.execute("update office set em_salary=em_salary+em_salary*25/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was increased by 25%!!!")
        else:
            print("kindly choose from the given options!!!")

    if sal==2:
        ID = input("enter employee name")
        print("1) 5% deduction")
        print("2) 10% deduction")
        print("3) 15% deduction")
        print("4) 25% deduction")
        deduct = eval(input("select how much salary hike would you like to deduct??----->"))
        if deduct == 1:
            mycursor.execute("update office set em_salary=em_salary-em_salary*5/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was deducted by 5%!!!")
        elif deduct == 2:
            mycursor.execute("update office set em_salary=em_salary-em_salary*10/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was deducted by 10%!!!")
        elif deduct == 3:
            mycursor.execute("update office set em_salary=em_salary-em_salary*15/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was deducted by 15%!!!")
        elif deduct == 4:
            mycursor.execute("update office set em_salary=em_salary-em_salary*25/100 where em_no='"+(ID)+"'; ")
            conn.commit()
            print("employee salary was deducted by 25%!!!")
        else:
            print("kindly choose from the given options!!!")



def em_list():
    try:
        mycursor.execute("select em_name from office order by em_name asc")
        list_ = mycursor.fetchall()
        for x in list_:
            print(x)
        a = mycursor.rowcount()
        print("total employees are----->", a)
    except:
        print("")



def em_count():
    mycursor.execute("select count(distinct em_name) from office")
    count = mycursor.fetchall()
    for x in count:
        print("number of employees in the company are----->", x)
    conn.commit()



def salary():
    nam = input("enter employee name :")
    a = mycursor.execute("select em_salary from office where em_name='"+(nam)+"';")
    mycursor.execute(a)
    salary = mycursor.fetchall()
    for x in salary:
        print("current salary of",nam,"is----->",x)
    conn.commit()



def em_perform():
    print("please choose from the following")
    print("1)update employee work experience/performance")
    print("2)view employee work experience/performance")
    choice=input("(1/2)----->")

    if choice=="1":
        v_em_no = input("enter employee ID----->")
        print("ENTERED EMPLOYEE NUMBER IS----->",v_em_no)
        v_em_performance = input("enter employee performance( 1-100 )----->")
        v_em_work = input("enter  experience( IN YEARS )----->")
        mycursor.execute("insert into em_performance1 values('" + (v_em_no) + "','" + v_em_performance + "','" + str(v_em_work) + "')")
        conn.commit()
        print("WORK EXPERIENCE UPDATED SUCCESSFULLY!!!")
    if choice=="2":
        v_em_no = input("enter employee ID----->")
        a=mycursor.execute("select em_name from office where em_no='"+(v_em_no)+"';")
        b=mycursor.fetchall()
        v_em_name = b
        c=mycursor.execute("select em_dept from office where em_no='"+(v_em_no)+"';")
        d=mycursor.fetchall()
        v_em_dept = d
        print("EMPLOYEE NAME CORRESPONDING TO EMPLOYEE ID IS----->", b)
        print("EMPLOYEE DEPARTMENT CORRESPONDING TO EMPLOYEE ID IS----->", d)
        e=mycursor.execute("select em_performance from em_performance1 where em_no='"+(v_em_no)+"'; ")
        f=mycursor.fetchall()
        print("PERFORMANCE(1-100) OF EMPLOYE NO.",v_em_no,"is----->",f)
        g=mycursor.execute("select em_work from em_performance1 where em_no='"+(v_em_no)+"'; ")
        h=mycursor.fetchall()
        print("EXPERIENCE(IN YEARS) OF EMPLOYEE NO.",v_em_no,"is----->",h)


def about():
    print("AA companiy was  started in 1972 as a team of two colleagues with a desire to do something new.")
    print("Together, we changed enterprise software and reinvented how business was done.")
    print(" Today, as a market leader in enterprise application software, we remain true to our roots.")
    print(" That’s why we engineer solutions to fuel innovation, foster equality and spread opportunity for our employees and customers")
    print("AA values the entrepreneurial spirit, fostering creativity and building lasting relationships with our employees.")
    print("We know that a diverse and inclusive workforce keeps us competitive and provides opportunities for all.")
    print("We believe that together we can transform industries, grow economics, lift up societies and sustain our environment")
    print("Because it’s the best-run businesses that make the world run better and improve people’s lives.")
    print("(courtesy-SAP)")


menu()