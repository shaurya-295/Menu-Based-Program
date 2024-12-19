import mysql.connector as m
co=m.connect(host="localhost",user="root",password="cshp",database="niksps")
cur=co.cursor()
while True:
    
    print("# For Retailers")
    print("1 Add Items")
    print("2 Remove Items")
    print("3 Add Quantity")
    print("# For Buyers")
    print("4 To Buy Items")
    print("5 To EXIT")
    key=input("key to login retailers menu")
    if key=="password":
        print("      WELCOME TO OUR COSMETICS SHOP                           ")
        s="select * from cosmetics"
        cur.execute(s)
        f=cur.fetchall()
        print("","-"*39,"")
        print("|%16s|%5s|%5s|%10s|"%("ITEMS","C_P","S_P","QUANTITY"))
        print("","-"*39,"")
        for i in f:
            print("|%16s|%5d|%5d|%10d|"%(i[0],i[1],i[2],i[3]))
        print("","-"*39,"")
        e=input("Enter your choice")
        if e=='1':
            name=input("enter the name of item")
            C_P=int(input("enter cost price"))
            S_P=int(input("enter selling price"))
            quan=int(input("enter quantity of item"))
            i="insert into cosmetics values('{}',{},{},{})".format(name,C_P,S_P,quan)
            cur.execute(i)
            co.commit()
        elif e=='2':
                name=input("enter name of the item to delete")
                d="delete from cosmetics where items='{}'".format(name)
                cur.execute(d)
                co.commit()
        elif e=='3':
            n=input("name of the item")
            q=int(input("enter quantity to add"))
            i="select quantity from cosmetics where items='{}'".format(n)
            cur.execute(i)
            quantity=cur.fetchone()
            x=quantity[0]
            q=x+q
            u="update cosmetics set quantity={} where items='{}'".format(q,n)
            cur.execute(u)
            co.commit()
    else:
        e=input("Enter your choice")
        s="select ITEMS,S_P from cosmetics"
        cur.execute(s)
        f=cur.fetchall()
        print("","-"*39,"")
        print("|%16s|%5s|"%("ITEMS","S_P"))
        print("","-"*39,"")
        for i in f:
            print("|%16s|%5d|"%(i[0],i[1]))
        print("","-"*39,"")
        
        if e=="4":
            Bill=[]
            cur.execute("select items from cosmetics")
            l1=cur.fetchall()
            cur.execute("select quantity from cosmetics")
            l2=cur.fetchall()
            m="y"
            while m=="y":
                i=input("enter item name")
                q=int(input("items quantity required"))
                for j in range(len(l1)):
                    if l1[j][0]==i and l2[j][0]>=q:
                        cur.execute("select (S_P*{}) from cosmetics where items='{}'".format(q,i))
                        c=cur.fetchall()[0][0]
                        cur.execute("update cosmetics set quantity=(quantity-{}) where items='{}'".format(q,i))
                        co.commit()
                        Bill.append([i,q,c])
                        break
                else:
                    if l1[j][0]!=i:
                     print("item not found")
                    if l2[j][0]<q:
                        print("out of stock")
                m=input("Buy More?(y/n)")
            print(f"{'*** BILL ***':^35s}")
            print("","-"*33,"")
            print("|%16s|%10s|%5s|"%("ITEMS","QUANTITY","S_P"))
            print("","-"*33,"")
            T=0
            for x in Bill:
                T+=x[2]
                print("|%16s|%10d|%5d|"%(x[0],x[1],x[2]))
            print("","-"*33,"")
            print("|%27s|%5d|"%("Total Cost",T))
            print("","-"*33,"")
        else:
            print("Thank You")
            break
