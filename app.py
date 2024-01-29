from pywebio.platform.flask import webio_view
from flask import Flask
import pywebio
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import mysql.connector as mysql

#con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')


app = Flask(__name__)
pywebio.config(title="مدرستي")

date=['2023/2024','2024/2025','2025/2026']
class_name= ['الاول','الثاني','الثالث','الرابع','الخامس','السادس','السابع','الثامن','التاسع','العاشر','الحادي عشر','الثاني عشر']
def ass0():
    put_html('<style> @keyframes ani{0% {color:blue; font-size:50px; } 20% {color:red;font-size:40;} 40%{color:green;font-size:30px;} 60%{color:red;font-size:40px;} 80%{color:blue; font-size:45px; } 100%{color:red; font-size:50px; }} .d1{height:70px; background:white;} .p1{animation:ani 8s linear infinite ;  text-shadow:5px 5px 5px white; border-radius:20px;}</style>')
    put_html('<div class=d1><center><b><p class=p1 float=center>MY SCHOOL</p></b></center><div>')
    put_html("</br></br></br></br><hr>")
 
def ass():
    put_html('<style> .d1{height:2%; background:white;} .p1{ text-shadow:5px 5px 5px blue; font-size:40px }</style>')
    put_html('<div class=d1><center><b><p class=p1 float=center>MY SCHOOL</p></b></center><div>')
    put_html("</br></br><hr>")
    
    put_link("مدير",url='/moder').style('font-size:20px;')
    put_text("")
    put_link("مدرس",url='/teacher').style('font-size:20px;')
       




#انشاء حساب المدرسة
def creat_account_school():
    ass()
    while True:
        data_school=input_group("ادخل البيانات التالية",[
            
            input("اسم المدرسة",type="text",name="a1",required=True),
            input("كلمة المرور",type="text",name="a2",required=True),
            
            
        ])
        a1=data_school['a1']
        a2=data_school['a2']
        
        
        
        
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s   ORDER BY schoolname ASC", (a1,))
        a1res = (cur.fetchall())
        con.commit()
        con .close()
        a1res1=[data[0] for data in a1res]
        
        if a1res1==[]:
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            query = 'INSERT INTO `account`(`schoolname`,`schoolpassword`) VALUES(%s,%s)'
            val = (a1,a2)
            cur.execute(query, val)   
            con.commit()
            con.close()
            popup("✔✔✔",content="تم انشاء الحساب بنجاح")
        else:
            popup("💥💥💥",content="تم انشاء حساب لهذه المدرسة من قبل اذا اردت انشاء حساب جديد قم بحذف الحساب القديم اولا")


#انشاء حساب المدير
def adminaccount():
    ass()
    while True:
        data_admin=input_group("ادخل البيانات التالية",[
            input("اسم المدرسة",type="text",name="b1",required=True),
            input("كلمة المرور",type="text",name="b2",required=True),
            input("اسم المدير",type="text",name="b3",required=True),
            input("كلمة المرور",type="text",name="b4",required=True)
            
            
        ])
        b1=data_admin['b1']
        b2=data_admin['b2']
        b3=data_admin['b3']
        b4=data_admin['b4']


        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s AND schoolpassword=%s  ORDER BY schoolname ASC", (b1,b2))
        b1res = (cur.fetchall())
        con.commit()
        con .close()
        b1res1=[data[0] for data in b1res]
        
        if b1res1==[]:
            popup("عذرا",content="هناك خطأ بكلمة المرور او اسم المدرسة")
            
        else:
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute('UPDATE `account` SET adminname=%s ,password=%s  WHERE schoolname=%s AND schoolpassword=%s   ', (b3,b4,b1,b2))
            con.commit()
            con.close()
            popup("✔✔✔✔",content="تم انشاء الحساب بنجاح")
            
            


#بيانات المعلمين
def inf_teacher():
    ass()
    
    
    data_school=input_group("ادخل البيانات التالية",[
        
        input("اسم المدرسة",type="text",name="c1",required=True),
        input("كلمة المرور",type="text",name="c2",required=True)
        
        
        
    ])
    c1=data_school['c1']
    c2=data_school['c2']
    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s AND schoolpassword=%s   ORDER BY schoolname ASC", (c1,c2))
    c1res = (cur.fetchall())
    con.commit()
    con .close()
    c1res1=[data[0] for data in c1res]
    if c1res1 == []:
        popup("💥💥💥",content="تأكد من اسم المدرسة وكلمة المرور انهما صحيحتين")
    
    
    else:
        while True:
            
            data_teacher=input_group("ادخل المعلومات",[
                select("الصف",name="c3",options=class_name,required=True),
                input("المادة",type="text",name="c4",required=True),
                input(" اسم الاستاذ الثلاثي ",type="text",name="c5",required=True)
            
            ])
            c3=data_teacher["c3"]
            c4=data_teacher['c4']
            c5=data_teacher['c5']
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute("SELECT DISTINCT teacher FROM teacherinfo WHERE schoolname=%s AND class=%s AND subjectname=%s  ORDER BY teacher ASC", (c1,c3,c4))
            tu=cur.fetchall()
            con.commit()
            con.close()
            tu1=[data[0] for data in tu]
            
            if tu1==[]:
            
            
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                query = 'INSERT INTO `teacherinfo`(`schoolname`,`class`,`subjectname`,`teacher`) VALUES(%s,%s,%s,%s)'
                val = (c1,c3,c4,c5)
                cur.execute(query, val)   
                con.commit()
                con.close()
                popup("✔✔✔✔",content="تمت اضافة البيانات بنجاح")
            else:
                popup("عذرا",content="لقد قمت بإضافة الاستاذ سابقا")
        


#تعديل استاذ مادة
def update_teacher():
    ass()
    data_up_teacher=input_group("ادخل البيانات التالية",[
        
        input("اسم المدرسة",type="text",name="d1",required=True),
        input("كلمة المرور",type="text",name="d2",required=True)
        
        
        
    ])
    d1=data_up_teacher['d1']
    d2=data_up_teacher['d2']
    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT schoolpassword FROM account WHERE schoolname=%s AND schoolpassword=%s   ORDER BY schoolname ASC", (d1,d2))
    d1res = (cur.fetchall())
    con.commit()
    con .close()
    d1res1=[data[0] for data in d1res]
    if d1res1== []:
        popup("💥💥💥",content="تأكد من اسم المدرسة وكلمة المرور انهما صحيحتين")
    
    
    else:
        while True:
            
            data_teacher=input_group("ادخل المعلومات",[
                select("الصف",name="d3",options=class_name,required=True),
                input("المادة",type="text",name="d4",required=True),
                input(" اسم الاستاذ الجديد الثلاثي ",type="text",name="d5",required=True)
            
            ])
            d3=data_teacher["d3"]
            d4=data_teacher['d4']
            d5=data_teacher['d5']
            
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute('UPDATE `teacherinfo` SET teacher=%s WHERE schoolname=%s AND class=%s AND subject=%s    ', (d5,d1,d3,d4))
            con.commit()
            con.close()
            popup("✔✔✔✔",content="تم  التعديل بنجاح")
            
            
    


#اضافة طلاب   
def add_students():
    ass()
    data_school=input_group("ادخل البيانات التالية",[
        
        input("اسم المدرسة",type="text",name="e1",required=True),
        input("كلمة المرور",type="text",name="e2",required=True),
        select(" الصف",options=class_name,name="e5",required=True)
        
        
        
    ])
    e1=data_school['e1']
    e2=data_school['e2']
    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s AND schoolpassword=%s   ORDER BY schoolname ASC", (e1,e2))
    e1res = (cur.fetchall())
    con.commit()
    con .close()
    e1res1=[data[0] for data in e1res]
    if e1res1==[]:
        popup("💥💥💥",content="تأكد من اسم المدرسة وكلمة المرور انهما صحيحتين")
    
    else:
        while True:
            
            data_students=input_group("ادخل المعلومات",[
                input("اسم الطالب",type="text",name="e3",required=True),
                input("اسم الام",type="text",name="e4",required=True),
                
                
            ])
            e3=data_students["e3"]
            e4=data_students['e4']
            e5=data_school['e5']
            
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            query = 'INSERT INTO `students`(`schoolname`,`studentname`,`studentmother`,`class`) VALUES(%s,%s,%s,%s)'
            val = (e1,e3,e4,e5)
            cur.execute(query, val)   
            con.commit()
            con.close()
            popup("✔✔✔✔",content="تمت اضافة البيانات بنجاح")


#انشاءحساب مدرس
def teacher_account():
    ass()
    data_f=input_group("ادخل البيانات التالية",[
        
        input("اسم المدرسة",type="text",name="f1",required=True),
        input("كلمة المرور",type="text",name="f2",required=True),
        select("الصف",name="f3",options=class_name,required=True),
  
        
    ])
    f1=data_f['f1']
    f2=data_f['f2']
    f3=data_f['f3']
    #التأكد ك\من المدرسة وجلب المواد
    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s AND schoolpassword=%s   ORDER BY schoolname ASC", (f1,f2))
    f1res = (cur.fetchall())
    con.commit()
    con .close()
    f1res1=[data[0] for data in f1res]
    if f1res1==[]:
        popup("💥💥💥",content="تأكد من اسم المدرسة وكلمة المرور انهما صحيحتين")
    else:
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT subjectname FROM teacherinfo WHERE schoolname=%s AND class=%s   ORDER BY subjectname ASC", (f1,f3))
        res = (cur.fetchall())
        con.commit()
        con .close()
        res1=[data[0] for data in res]
        
    
    
        data_f2=input_group("ادخل البيانات التالية",[
       
        
        select("المادة",options=res1,name="f4",required=True),
        input(" اسم الاستاذ الثلاثي ",type="text",name="f5",required=True),
        input("كلمة المرور الخاصة بك",type="text",name="f6",required=True)
     
        ])
        f4=data_f2['f4']
        f5=data_f2['f5']
        f6=data_f2['f6']

        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT teacher FROM teacherinfo WHERE schoolname=%s AND subjectname=%s AND class=%s   ORDER BY subjectname ASC", (f1,f4,f3))
        n = (cur.fetchall())
        con.commit()
        con .close()
        n1=[data[0] for data in n]
        if n1[0]==f5:
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute('UPDATE `teacherinfo` SET password=%s WHERE schoolname=%s AND class=%s AND subjectname=%s AND teacher=%s   ', (f6,f1,f3,f4,f5))
            con.commit()
            con.close()
            popup("✔✔✔✔",content="تم  انشاء الحساب  بنجاح")
            
        
        else:
            popup("عذرا",content="هناك خطأبالاسم المدخل .اذا استمرت المشكلة تأكد بأن المدير قد قام باضافتك")



#اضافة علامات الطلاب
def add_mark():
    ass()
    session=['الاول','الثاني']
    data_g=input_group("ادخل المعلومات",[
            input("اسم المدرسة",type="text",name="g1",required=True),
            input("كلمة المرور ",type="text",name="g2",required=True),
            select(" الصف",options=class_name,required=True,name="g3"),
            select("الفصل ",options=session,name="g4",required=True),
            select("العام الدراسي ",options=date,name="gd4",required=True)
            
        ])
    g1=data_g["g1"]
    g2=data_g["g2"]
    g3=data_g["g3"]
    g4=data_g['g4']
    gd4=data_g['gd4']
    
    #التأكد من اسم المدرسة
    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s AND schoolpassword=%s   ORDER BY schoolname ASC", (g1,g2))
    g1res = (cur.fetchall())
    con.commit()
    con .close()
    g1res1=[data[0] for data in g1res]
    if g1res1==[]:
        popup("💥💥💥",content="تأكد من اسم المدرسة وكلمة المرور انهما صحيحتين")
    else:
        #جلب المواد
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT  subjectname FROM teacherinfo WHERE schoolname=%s AND class=%s ORDER BY subjectname ASC", (g1,g3))
        subject = (cur.fetchall())
        con.commit()
        con .close()
        subject1=[data[0] for data in subject]
        #جلب الاسماء
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT  studentname,studentmother FROM students WHERE schoolname=%s AND class=%s ORDER BY studentname ASC", (g1,g3))
        c = (cur.fetchall())
        con.commit()
        con .close()
        c11=[data[0]+" :"+"اسم الام "+data[1] for data in c]
            
        #التأكد من كلمة مرور الاستاذ
        
        data_g2=input_group("ادخل المعلومات",[
            select("اسم المادة",options=subject1,name="g5",required=True),
            input("  العلامة الكلية للمادة ",type="text",name="mtot",required=True),
            input(" اسم المدرس ",type="text",name="g6",required=True),
            input("كلمة المرور ",type="text",name="g7",required=True)
            
        ])
        g5=data_g2["g5"]
        g6=data_g2["g6"]
        g7=data_g2["g7"]
        mtot=data_g2['mtot']
        #جلب اسم الاستاذ
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT teacher FROM teacherinfo WHERE schoolname=%s AND subjectname=%s AND class=%s  ORDER BY password ASC", (g1,g5,g3))
        tea = (cur.fetchall())
        con.commit()
        con .close()
        tea1=[data[0] for data in tea]

        #جلب كلمة المرور
        
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT password FROM teacherinfo WHERE schoolname=%s AND subjectname=%s AND class=%s  ORDER BY password ASC", (g1,g5,g3))
        pas = (cur.fetchall())
        con.commit()
        con .close()
        pas1=[data[0] for data in pas]
        
        if g7==pas1[0] and g6==tea1[0]:
            c11new=[]
            su=len(c11)
            for h in c11:
                
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                cur.execute("SELECT DISTINCT student FROM markers WHERE schoolname=%s AND class=%s AND session=%s AND subject=%s ORDER BY student ASC", (g1,g3,g4,g5))
                chst = (cur.fetchall())
                con.commit()
                con .close()
                chst1=[data[0] for data in chst]
                
                if h   not in chst1:
                    c11new.append(h)
                    
              
            su=len(c11new)
            if su==0:
                put_success("لقد تم الانتهاء من اضافة العلامات ",closable=True) 
            for k in c11new:
                
                   
                dm=input_group("ادخل المعلومات",[
                    
                    
                    input(" عدد الطلاب المتبقي",type="text",readonly=True,value=su,name="llll"),
                    input(" اسم الطالب",type="text",name="n1",required=True,value=k,readonly=True),
                    input(" درجة أعمل الطالب",type="number",name="l1",required=True),
                    input(" درجة الامتحان",type="number",name="l2",required=True)
                    
                ])
                n1=dm['n1']
                l1=dm['l1']
                l2=dm['l2']
                m=l1+l2
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                query = 'INSERT INTO `markers`(`schoolname`,`class`,`session`,`student`,`subject`,`workdegree`,`examdegree`,`mark`,`totalmark`,`date`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                val = (g1,g3,g4,n1,g5,l1,l2,m,mtot,gd4)
                cur.execute(query, val)   
                con.commit()
                con.close()
                su=su-1
                popup("✔✔✔✔",content="تمت اضافة العلامة بنجاح")
                if su==0:
                    put_success("لقد تم الانتهاء من اضافة العلامات ",closable=True) 
                
                
            
            
        
        else:
            popup("عذرا",content="هناك خطأباسم المدرس وكلمة المرور") 
        
    
   
        
  
#تعديل علامة طالب
def edit_mark():      
    ass()
    session=['الاول','الثاني']
    data_g=input_group("ادخل المعلومات",[
            input("اسم المدرسة",type="text",name="h1",required=True),
            input("كلمة المرور ",type="text",name="h2",required=True),
            select(" الصف",options=class_name,required=True,name="h4"),
            select("الفصل ",options=session,name="h3",required=True)
            
        ])
    h1=data_g["h1"]
    h2=data_g["h2"]
    h3=data_g["h3"]
    h4=data_g['h4']
    
    #التأكد من اسم المدرسة
    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s AND schoolpassword=%s   ORDER BY schoolname ASC", (h1,h2))
    h1res = (cur.fetchall())
    con.commit()
    con .close()
    h1res1=[data[0] for data in h1res]
    if h1res1==[]:
        popup("💥💥💥",content="تأكد من اسم المدرسة وكلمة المرور انهما صحيحتين")
    else:
        #جلب المواد
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT  subjectname FROM teacherinfo WHERE schoolname=%s AND class=%s ORDER BY subjectname ASC", (h1,h4))
        subject = (cur.fetchall())
        con.commit()
        con .close()
        subject1=[data[0] for data in subject]
        
        #التأكد من كلمة مرور الاستاذ
        
        data_g2=input_group("ادخل المعلومات",[
            select("اسم المادة",options=subject1,name="h5",required=True),
            input(" اسم المدرس ",type="text",name="h6",required=True),
            input("كلمة المرور ",type="text",name="h7",required=True)
            
        ])
        h5=data_g2["h5"]
        h6=data_g2["h6"]
        h7=data_g2["h7"]
        
        #جلب اسم الاستاذ
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT teacher FROM teacherinfo WHERE schoolname=%s AND subjectname=%s AND class=%s  ORDER BY password ASC", (h1,h5,h4))
        tea = (cur.fetchall())
        con.commit()
        con .close()
        tea1=[data[0] for data in tea]

        #جلب كلمة المرور
        
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT password FROM teacherinfo WHERE schoolname=%s AND subjectname=%s AND class=%s  ORDER BY password ASC", (h1,h5,h4))
        pas = (cur.fetchall())
        con.commit()
        con .close()
        pas1=[data[0] for data in pas]
        
        if h7==pas1[0] and h6==tea1[0]:
            
            
                
                
            dm=input_group("ادخل المعلومات",[
            
                    input(" اسم الطالب",type="text",name="h8",required=True),
                    input(" اسم لام",type="text",name="h9",required=True),
                    input("  درجة اعمال الطالب الجديدة",type="number",name="h10",required=True),
                    input(" درجة الامتحان الجديدة",type="number",name="h11",required=True)
                    
                ])
            h8=dm['h8']
            h9=dm['h9']
            h10=dm['h10']
            h11=dm['h11']
            h=h10+h11
            fg=h8+" :"+"اسم الام "+h9
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute('UPDATE `markers` SET workdegree=%s , examdegree=%s , mark=%s WHERE schoolname=%s AND class=%s AND subject=%s AND session=%s AND student=%s   ', (h10,h11,h,h1,h4,h5,h3,fg))
            con.commit()
            con.close()
            popup("✔✔✔✔",content="تم  التعديل بنجاح")
            
                
            
            
        
        else:
            popup("عذرا",content="هناك خطأباسم المدرس وكلمة المرور") 
        
    


#علامات الطلاب وترتيبهم
def avag():
    ass()
    session=['الاول','الثاني']
    datad_avag=input_group("ادخل البيانات التالية",[
        
        input("اسم المدرسة",type="text",name="i1",required=True),
        input("كلمة المرور",type="text",name="i2",required=True),
        input(" اسم المدير",type="text",name="i3",required=True),
        input("كلمة مرور المدير",type="text",name="i4",required=True),
        select(" الصف",options=class_name,name="i5",required=True),
        select(" الغصل",options=session,name="i6",required=True),
        select(" العام الدراسي",options=date,name="id6",required=True)
        
        
        
    ])
    i1=datad_avag['i1']
    i2=datad_avag['i2']
    i3=datad_avag['i3']
    i4=datad_avag['i4']
    i5=datad_avag['i5']
    i6=datad_avag['i6']
    id6=datad_avag['id6']
    
     #التحقق من المدرسة
    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT schoolname FROM account WHERE schoolname=%s AND schoolpassword=%s   ORDER BY schoolname ASC", (i1,i2))
    ires= (cur.fetchall())
    con.commit()
    con .close()
    ires1=[data[0] for data in ires]
    if ires1==[]:
        popup("💥💥💥",content="تأكد من اسم المدرسة وكلمة المرور انهما صحيحتين")
    
    else:
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT adminname FROM account WHERE schoolname=%s AND schoolpassword=%s AND adminname=%s AND password=%s   ORDER BY adminname ASC", (i1,i2,i3,i4))
        i3res= (cur.fetchall())
        con.commit()
        con .close()
        i3res1=[data[0] for data in i3res]
        if i3res1==[]:
            popup("💥💥💥",content="تأكد من اسم المدير وكلمة مرور المدير انهما صحيحتين")
        
        else:
            put_html('</br></br>')
            put_text("معدلات وترتيب طلاب الصف ").style('float:right;')
            put_text(i5).style('float:right;color:red;')
            put_text("الفصل").style('float:right;')
            put_text(i6).style('float:right;color:red;')
            put_text("العام الدراسي").style('float:right;')
            put_text(id6).style('float:right;color:red;')
            put_html('</br></br></br>')
            
            #اسماء الطلاب في الصف
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute("SELECT DISTINCT student FROM markers WHERE schoolname=%s AND class=%s AND session=%s AND date=%s  ORDER BY student ASC", (i1,i5,i6,id6))
            rstu= (cur.fetchall())
            con.commit()
            con .close()
            rstu1=[data[0] for data in rstu]
        
            #جلب المواد
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute("SELECT DISTINCT subject FROM markers WHERE schoolname=%s AND class=%s AND session=%s   ORDER BY student ASC", (i1,i5,i6))
            resses= (cur.fetchall())
            con.commit()
            con .close()
            resses1=[data[0] for data in resses]
            
            
            for x in rstu1:
                average=0
                summark=[]
                for y in resses1:
                #جلب علامات المواد لكل طالب 
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    cur.execute("SELECT DISTINCT  mark FROM markers WHERE schoolname=%s AND class=%s  AND student=%s AND subject=%s AND session=%s AND date=%s ORDER BY mark ASC", (i1,i5,x,y,i6,id6))
                    mar= (cur.fetchall())
                    con.commit()
                    con .close()
                    mar1=[data[0] for data in mar]
                    
                    summark.append(mar1[0])
                
                average=sum(summark)/len(summark)
                
                
                #اضافة المعدلات من اجل الترتيب
            
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                cur.execute("SELECT DISTINCT avg FROM orders WHERE schoolname=%s AND class=%s AND student=%s  AND session=%s AND date=%s  ORDER BY avg ASC", (i1,i5,x,i6,id6))
                hj= (cur.fetchall())
                con.commit()
                con .close()
                hj1=[data[0] for data in hj]
                
                if hj1==[]:
                
            
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    query = 'INSERT INTO `orders`(`schoolname`,`class`,`session`,`student`,`avg`,`date`) VALUES(%s,%s,%s,%s,%s,%s)'
                    val = (i1,i5,i6,x,average,id6)
                    cur.execute(query, val)   
                    con.commit()
                    con.close()
                    
                elif hj1[0]!=average:
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    cur.execute('UPDATE `orders` SET avg=%s WHERE schoolname=%s AND student=%s AND class=%s AND session=%s AND date=%s ', (average,i1,x,i5,i6,id6))
                    con.commit()
                    con.close()


            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute("SELECT  student FROM orders WHERE schoolname=%s AND class=%s AND session=%s AND date=%s ORDER BY avg DESC", (i1,i5,i6,id6))
            ord = (cur.fetchall())
            con.commit()
            con .close()
            ord1=[data[0] for data in ord]
            
            
            for n in ord1:
                put_text(n+"  ").style('text-align:center;')
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                cur.execute("SELECT DISTINCT avg FROM orders WHERE schoolname=%s AND class=%s AND student=%s AND session=%s AND date=%s ORDER BY avg DESC", (i1,i5,n,i6,id6))
                fin = (cur.fetchall())
                con.commit()
                con .close()
                fin1=[data[0] for data in fin]
                #المعدل الكلي
                fin2=[]
                for p in resses1:
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    cur.execute("SELECT DISTINCT mark FROM markers WHERE schoolname=%s AND class=%s  AND student=%s AND subject=%s AND session=%s AND date=%s ORDER BY mark ASC", (i1,i5,n,p,i6,id6))
                    j1= (cur.fetchall())
                    con.commit()
                    con .close()
                    j11=[data[0] for data in j1]
                    
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    cur.execute("SELECT DISTINCT workdegree FROM markers WHERE schoolname=%s AND class=%s  AND student=%s AND subject=%s AND session=%s AND date=%s ORDER BY mark ASC", (i1,i5,n,p,i6,id6))
                    j2= (cur.fetchall())
                    con.commit()
                    con .close()
                    j21=[data[0] for data in j2]
                    
                    
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    cur.execute("SELECT DISTINCT examdegree FROM markers WHERE schoolname=%s AND class=%s  AND student=%s AND subject=%s AND session=%s AND date=%s ORDER BY mark ASC", (i1,i5,n,p,i6,id6))
                    j3= (cur.fetchall())
                    con.commit()
                    con .close()
                    j31=[data[0] for data in j3]
                    
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    cur.execute("SELECT DISTINCT totalmark FROM markers WHERE schoolname=%s AND class=%s  AND student=%s AND subject=%s AND session=%s AND date=%s ORDER BY mark ASC", (i1,i5,n,p,i6,id6))
                    j4= (cur.fetchall())
                    con.commit()
                    con .close()
                    j41=[data[0] for data in j4]
                    
                    
                    
                    fin2.append(j41[0])
                    
                    
                    put_text(p).style('text-align:center;color:red;')
                    put_text("درجة الاعمال:"+str(j21)+"  "+"درجة الامتحان:"+str(j31)+" "+"المجموع"+str(j11)+"/"+str(j41)).style('text-align:center;')
                    
                sumfin2=sum(fin2)/len(fin2)
                put_text("المعدل"+"  "+str(fin1)+"  "+"/"+"  "+str(sumfin2)).style('text-align:center;color:red;')  
                put_html('<hr>')
 
 
 
 

#نقل الطلاب
def trans_students():
    ass()
    while True:
        data_trans=input_group("ادخل المعلومات",[
            input("اسم المدرسة",type="text",name="k1",required=True),
            input("كلمة المرور ",type="text",name="k2",required=True),
            input("اسم المدير",type="text",name="k3",required=True),
            input("كلمة مرور المدير ",type="text",name="k4",required=True),
            select("الصف الحالي",options=class_name,required=True,name="k5"),
            select("الصف الجديد",options=class_name,required=True,name="k6")
            
            
        ])
        k1=data_trans['k1']
        k2=data_trans['k2']
        k3=data_trans['k3']
        k4=data_trans['k4']
        k5=data_trans['k5']
        k6=data_trans['k6']
        
        #التحقق من المدرسة
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT schoolpassword FROM account WHERE schoolname=%s  ORDER BY schoolname ASC", (k1,))
        aab= (cur.fetchall())
        con.commit()
        con .close()
        aab1=[data[0] for data in aab]
        if aab1!=[]:
            
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute("SELECT DISTINCT password FROM account WHERE schoolname=%s AND adminname=%s  ORDER BY password ASC", (k1,k3))
            kaab= (cur.fetchall())
            con.commit()
            con .close()
            kaab1=[data[0] for data in kaab]
            
            if kaab1[0]==k4:
                
            
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                cur.execute("SELECT  studentname FROM students WHERE schoolname=%s AND class=%s  ", (k1,k5))
                tran=cur.fetchall()
                con.commit()
                con.close()
                tran1=[data[0] for data in tran]
                for xn in tran1:
                    con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                    cur = con.cursor()
                    cur.execute('UPDATE `students` SET class=%s WHERE schoolname=%s AND studentname=%s AND class=%s  ', (k6,k1,xn,k5))
                    con.commit()
                    con.close()
                    popup("✔✔✔✔",content="تم النقل بنجاح")
                
            else:
                popup("عذرا",content="هناك خطأباسم المدير او كلمة مروره")        
                    
        else:
            popup("💥💥💥","يوجد خطأباسم المدرسة او كلمة المرور")
    
        
      
      


#حذف طلاب
def delt_students():
    ass()
    while True:
        data_delt=input_group("ادخل المعلومات",[
            input("اسم المدرسة",type="text",name="o1",required=True),
            input("كلمة المرور ",type="text",name="o2",required=True),
            input(" اسم المدير ",type="text",name="o3",required=True),
            input("كلمة مرور المدير ",type="text",name="o4",required=True),
            input("اسم الطالب",type="text",name="o5",required=True),
            input("اسم الام",type="text",name="o6",required=True),
            select(" الصف",options=class_name,name="o7",required=True)
            
        ])
        o1=data_delt['o1']
        o2=data_delt['o2']
        o3=data_delt['o3']
        o4=data_delt['o4']
        o5=data_delt['o5']
        o6=data_delt['o6']
        o7=data_delt['o7']
    
        #التحقق من المدرسة
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT schoolpassword FROM account WHERE schoolname=%s  ORDER BY schoolname ASC", (o1,))
        ab= (cur.fetchall())
        con.commit()
        con .close()
        ab1=[data[0] for data in ab]
        if ab1[0]!=[]:
            
            
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute("SELECT DISTINCT password FROM account WHERE schoolname=%s AND adminname  ORDER BY schoolname ASC", (o1,o3))
            abo= (cur.fetchall())
            con.commit()
            con .close()
            abo1=[data[0] for data in abo]
            if abo1[0]==o4:
                
            
            
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                cur.execute("DELETE  FROM students WHERE schoolname=%s studentname=%s  AND  studentmother=%s AND class=%s ", (o1,o5,o6,o7))
                con.commit()
                con.close()
                popup("✔✔",content="تم الحذف بنجاح")
            else:
                popup("عذرا",content="هناك خطأباسم المدير او كلمة المرور")
            
        else:
            popup("💥💥💥","يوجد خطأباسم المدرسة او كلمة المرور")
    
    



#حذف حساب المدرسة
def delt_update_school():
    ass()
    while True:
        
    
        data_delt_update_school=input_group("ادخل البيانات التالية",[
            
            input("اسم المدرسة",type="text",name="q1",required=True),
            input(" كلمة المرور",type="text",name="q2",required=True),
            input("اسم المدير",type="text",name="q3",required=True),
            input("كلمة مرور المدير ",type="text",name="q4",required=True)
            
            
            
            
        ])
        q1=data_delt_update_school['q1']
        q2=data_delt_update_school['q2']
        q3=data_delt_update_school['q3']
        q4=data_delt_update_school['q4']
        
        
            
        #التحقق من المدرسة
        con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT schoolpassword FROM account WHERE schoolname=%s  ORDER BY schoolname ASC", (q1,))
        v= (cur.fetchall())
        con.commit()
        con .close()
        v1=[data[0] for data in v]
        if v1!=[]:
            
            
            con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
            cur = con.cursor()
            cur.execute("SELECT DISTINCT password FROM account WHERE schoolname=%s AND adminname=%s  ORDER BY schoolname ASC", (q1,q3))
            v2= (cur.fetchall())
            con.commit()
            con .close()
            v21=[data[0] for data in v2]
            if v21[0]==q4:
                con=mysql.connect(host='buduioid4mevhus3yhtg-mysql.services.clever-cloud.com',user='uqxeimuqg50oixeq',password='DwdctjNldbPo7t9PGkLe',database='buduioid4mevhus3yhtg')
                cur = con.cursor()
                cur.execute("DELETE FROM `account`WHERE schoolname=%s AND schoolpassword=%s", (q1,q2))
                con.commit()
                con .close()
                popup("تم حذف الحساب")
            
            else:
                popup("عذرا",content="هناك خطأباسم المدير او كلمة المرور")
            
        else:
            popup("💥💥💥","يوجد خطأباسم المدرسة او كلمة المرور")
    
    

#المدير
def moder():
    ass()
    put_html('<style>.dm1{border:solid; border-radius:10px; text-align:center; width:30%; box-shadow:3px 3px 2px 2px blue;}  .dh1 a{font-size:20px; }</style>')
    put_html('<center><div class=dm1> <a href=/school> انشاء حساب المدرسة</a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/adminaccount> انشاء حساب المدير</a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/delt_update_school> حذف حساب المدرسة</a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/inf_teacher> اضافة بيانات المعلمين</a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/update_teacher>تعديل استاذ  مادة</a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/add_students>اضافة طلاب </a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/delt_students> حذف طلاب</a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/trans_students> نقل الطلاب  </a></div></center></br></br>')
    put_html('<center><div class=dm1> <a href=/avag>علامات الطلاب وترتيبهم</a></div></center></br></br>')
    
    


#مدرس
def teacher():
    ass()
    put_html('<style>.dh1{border:solid; border-radius:10px; text-align:center; width:20%; box-shadow:5px 5px 2px 5px blue ;}  .dh1 a{font-size:20px; }</style>')
    put_html('<center><div class=dh1> <a href=/teacher_account> انشاء حساب   </a></div></center></br></br>')
    put_html('<center><div class=dh1> <a href=/add_mark> اضافة علامات طلاب</a></div></center></br></br>')
    put_html('<center><div class=dh1> <a href=/edit_mark> تعديل علامة طالب</a></div></center>')
    


#الصفحة الرئيسية
def home():
    ass0()
    put_html('<style>.dh1{border:solid; border-radius:10px; text-align:center; width:20%; box-shadow:5px 5px 5px 5px blue inset;}  .dh1 a{font-size:20px; }</style>')
    put_html('<center><div class=dh1 > <a href=/moder > مدير</a></div></center></br></br>')
    put_html('<style>.dh2{border:solid; border-radius:10px; text-align:center; width:20%; box-shadow:5px 5px 5px 5px blue inset;}  .dh2 a{font-size:20px; }</style>')
    put_html('<center><div class=dh2 > <a href=/teacher> مدرس</a></div></center>')
    



app.add_url_rule('/moder','moder',webio_view(moder),
                  methods=['GET','POST','OPTIONS'])


#قسم الروابط
app.add_url_rule('/','home',webio_view(home),
                  methods=['GET','POST','OPTIONS'])


app.add_url_rule('/school','school',webio_view(creat_account_school),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/adminaccount','adminaccount',webio_view(adminaccount),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/inf_teacher','inf_teacher',webio_view(inf_teacher),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/update_teacher','update_teacher',webio_view(update_teacher),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/add_students','add_students',webio_view(add_students),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/teacher','teacher',webio_view(teacher),
                  methods=['GET','POST','OPTIONS'])


app.add_url_rule('/teacher_account','teacher_account',webio_view(teacher_account),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/add_mark','add_mark',webio_view(add_mark),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/edit_mark','edit_mark',webio_view(edit_mark),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/avag','avag',webio_view(avag),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/trans_students','trans_students',webio_view(trans_students),
                  methods=['GET','POST','OPTIONS'])


app.add_url_rule('/delt_students','delt_students',webio_view(delt_students),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/delt_update_school','delt_update_school',webio_view(delt_update_school),
                  methods=['GET','POST','OPTIONS'])


if __name__ == "__main__":
    
    app.run()
