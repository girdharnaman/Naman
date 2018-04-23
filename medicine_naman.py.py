from tkinter import *
win=Tk()
count=0
def add():
    f=open('dept_db.txt','a')            
    medicineid=s1.get()
    medicinename=s2.get()
    medicineprice=s3.get()
    medicinequantity=s4.get()
    expiryyear=s5.get()
    f.writelines(medicineid.ljust(5)+medicinename.ljust(20)+medicineprice.ljust(20)+medicinequantity.ljust(20)+expiryyear.ljust(10)+"\n")
    f.close()
def del_rec():
    prt_rcd=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()]
    f=open('dept_db.txt','r')           
    lines=f.readlines()
    print(lines)
    print(prt_rcd)
    f.close()
    f=open('dept_db.txt','w')           
    for i in lines:
        m=i.split()
        print(m)
        if(m!=prt_rcd):
             f.writelines(m[0].ljust(5)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(10)+"\n")
    f.close()
def update():
    a1=s1.get()
    a2=s2.get()
    a3=s3.get()
    a4=s4.get()
    a5=s5.get()
    f=open('dept_db.txt','r')          
    h=f.readlines()
    f.close()
    f=open('dept_db.txt','w')          
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=a1):
            f.writelines(j[0].ljust(5)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(10)+"\n")
    
        else:
            f.writelines(a1.ljust(5)+a2.ljust(20)+a3.ljust(20)+a4.ljust(10)+a5.ljust(10)+"\n")
            flag=1
    f.close()
def search():
    var=s1.get()
    f=open('dept_db.txt','r')         
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==var): 
            print(j)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()  
def next_rec():
    f=open('dept_db.txt','r')         
    i=0
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    info=l.split()
    s1.set(info[0])	
    s2.set(info[1])
    s3.set(info[2])
    s4.set(info[3])
    s5.set(info[4])
    count=count+1
    f.close()
def prev():
    global count
    i=0
    count=count-1
    print(count)
    f=open("dept_db.txt","r")        
    while(i<=count-1):
        l=f.readline()
        i=i+1
        print(l)
    rec=l.split()
    s1.set(rec[0])
    s2.set(rec[1])
    s3.set(rec[2])
    s4.set(rec[3])
    s5.set(rec[4])
def first():
    f=open("dept_db.txt",'r')       
    k=f.readlines()[0]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
def last():
    f=open("dept_db.txt",'r')       
    de=sum(1 for i in open("dept_db.txt"))-1
    print(de)
    k=f.readlines()[de]
    j=k.split()
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()

c1=Canvas(win,height=500,width=500)
c1.pack()

l1=Label(win,text="Medicine Id :")
l2=Label(win,text="Medicine Name :")
l3=Label(win,text="Medicine Price :")
l4=Label(win,text="Medicine Quantity :")
l5=Label(win,text="Expiry Year :")

l1.place(x=10,y=30)
l2.place(x=10,y=60)
l3.place(x=10,y=90)
l4.place(x=10,y=120)
l5.place(x=10,y=150)

t1=Entry(win,textvariable=s1)
t2=Entry(win,textvariable=s2)
t3=Entry(win,textvariable=s3)
t4=Entry(win,textvariable=s4)
t5=Entry(win,textvariable=s5)

t1.place(x=120,y=30)
t2.place(x=120,y=60)
t3.place(x=120,y=90)
t4.place(x=120,y=120)
t5.place(x=120,y=150)

b1=Button(win,text="ADD",command=add)
b2=Button(win,text="DELETE",command=del_rec)
b3=Button(win,text="UPDATE",command=update)
b4=Button(win,text="SEARCH",command=search)
b5=Button(win,text="NEXT",command=next_rec)
b6=Button(win,text="PREVIOUS",command=prev)
b7=Button(win,text="FIRST",command=first)
b8=Button(win,text="LAST",command=last)

b1.place(x=10,y=200)
b2.place(x=60,y=200)
b3.place(x=130,y=200)
b4.place(x=200,y=200)
b5.place(x=10,y=250)
b6.place(x=60,y=250)
b7.place(x=130,y=250)
b8.place(x=200,y=250)



win.mainloop()
