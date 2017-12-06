# A minimal Mysql shell for experiments
import pymysql
import time

sock ='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
h = 'localhost'
while True:
    try:
        dbname = input("Βάση δεδομένων: ")
        con = pymysql.connect(host = h,
             user='root', passwd='', db=dbname, charset='utf8')
    except pymysql.Error as e:
        print ('Σφάλμα', e)
    else:
        con.isolation_level = None
        cur = con.cursor()
        cur.execute('select version()')
        print('Εκδοση βάσης δεδομένων: {}'.format(cur.fetchone()))
        break
buffer = ""
#print("ΒΔ:", dbname, " Δώστε εντολές SQL (enter για έξοδο)")



cur.execute('DELETE  FROM `ΓΗΠΕΔΟ` ')
cur.execute('DELETE  FROM `ΜΠΑΣΚΕΤ`')
cur.execute('DELETE  FROM `ΒΟΛΕΥ` ')
cur.execute('DELETE  FROM `ΠΕΛΑΤΗΣ` ')
cur.execute('DELETE  FROM `ΠΟΔΟΣΦΑΙΡΟ` ')
cur.execute('DELETE  FROM `ΕΝΟΙΚΙΑΖΕΙ` ')

cur.execute('INSERT INTO `ΓΗΠΕΔΟ`( `ID`,`ΦΩΤΙΣΜΟΣ`,`ΜΠΑΛΕΣ`,`ΚΛΙΜΑΤΙΣΜΟΣ`) VALUES (0001,"ΟΧΙ",15,"NAI") ')
cur.execute('INSERT INTO `ΓΗΠΕΔΟ`( `ID`,`ΦΩΤΙΣΜΟΣ`,`ΜΠΑΛΕΣ`,`ΚΛΙΜΑΤΙΣΜΟΣ`) VALUES (0002,"ΟΧΙ",15,"NAI") ')
cur.execute('INSERT INTO `ΓΗΠΕΔΟ`( `ID`,`ΦΩΤΙΣΜΟΣ`,`ΜΠΑΛΕΣ`,`ΚΛΙΜΑΤΙΣΜΟΣ`) VALUES (0003,"NAI",15,"NAI") ')
cur.execute('INSERT INTO `ΓΗΠΕΔΟ`( `ID`,`ΦΩΤΙΣΜΟΣ`,`ΜΠΑΛΕΣ`,`ΚΛΙΜΑΤΙΣΜΟΣ`) VALUES (0004,"NAI",25,"NAI") ')
cur.execute('INSERT INTO `ΓΗΠΕΔΟ`( `ID`,`ΦΩΤΙΣΜΟΣ`,`ΜΠΑΛΕΣ`,`ΚΛΙΜΑΤΙΣΜΟΣ`) VALUES (0005,"NAI",25,"NAI") ')
cur.execute('INSERT INTO `ΓΗΠΕΔΟ`( `ID`,`ΦΩΤΙΣΜΟΣ`,`ΜΠΑΛΕΣ`,`ΚΛΙΜΑΤΙΣΜΟΣ`) VALUES (0006,"NAI",30,"NAI") ')


cur.execute('INSERT INTO `ΜΠΑΣΚΕΤ`( `ID`,`ΔΑΠΕΔΟ`)  VALUES (0001,"ΞΥΛΙΝΟ") ')
cur.execute('INSERT INTO `ΜΠΑΣΚΕΤ`( `ID`,`ΔΑΠΕΔΟ`)  VALUES (0002,"ΤΣΙΜΕΝΤΕΝΙΟ") ')
cur.execute('INSERT INTO `ΠΟΔΟΣΦΑΙΡΟ`( `ID`,`ΕΙΔΟΣ ΤΑΠΗΤΑ`, `ΔΙΑΣΤΑΣΕΙΣ`)  VALUES (0003,"ΧΛΩΡΟΤΑΠΗΤΑΣ","5x5") ')
cur.execute('INSERT INTO `ΠΟΔΟΣΦΑΙΡΟ`( `ID`,`ΕΙΔΟΣ ΤΑΠΗΤΑ`, `ΔΙΑΣΤΑΣΕΙΣ`)  VALUES (0004,"ΧΛΩΡΟΤΑΠΗΤΑΣ","7x7") ')
cur.execute('INSERT INTO `ΒΟΛΕΥ` (`ID`) VALUES (0005) ')
cur.execute('INSERT INTO `ΠΟΔΟΣΦΑΙΡΟ`( `ID`,`ΕΙΔΟΣ ΤΑΠΗΤΑ`, `ΔΙΑΣΤΑΣΕΙΣ`)  VALUES (0006,"ΧΛΩΡΟΤΑΠΗΤΑΣ","11x11") ')

cur.execute('INSERT INTO `ΠΕΛΑΤΗΣ`(`ΚΩΔΙΚΟΣ`,`ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ΤΗΛΕΦΩΝΟ`) VALUES (5001,"ΣΤΕΛΙΟΣ","ΠΑΠΑΔΟΠΟΥΛΟΣ","6984367354") ' )


cur.execute('INSERT INTO `ΠΕΛΑΤΗΣ`(`ΚΩΔΙΚΟΣ`,`ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ΤΗΛΕΦΩΝΟ`) VALUES (5002,"ΚΩΝΣΤΑΝΤΙΝΟΣ","ΜΙΧΑΛΟΠΟΥΛΟΣ","6944742354") ' )

cur.execute('INSERT INTO `ΠΕΛΑΤΗΣ`(`ΚΩΔΙΚΟΣ`,`ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ΤΗΛΕΦΩΝΟ`) VALUES (5003,"ΣΩΤΗΡΗΣ","ΜΑΓΚΑΦΑΣ","6934222354") ' )

cur.execute('INSERT INTO `ΠΕΛΑΤΗΣ`(`ΚΩΔΙΚΟΣ`,`ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ΤΗΛΕΦΩΝΟ`) VALUES (5004,"ΙΩΑΝΝΗΣ","ΜΟΥΣΤΑΚΙΔΗΣ","6974982354") ' )

cur.execute('INSERT INTO `ΠΕΛΑΤΗΣ`(`ΚΩΔΙΚΟΣ`,`ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ΤΗΛΕΦΩΝΟ`) VALUES (5005,"ΠΕΤΡΟΣ","ΠΑΥΛΟΠΟΥΛΟΣ","6984442354") ' )


#cur.execute()

# egw evala to cur.execure s comment gia na treksei
#cur.execute('INSERT INTO `')
cur.execute('commit')


cur.execute('SELECT `ΚΩΔΙΚΟΣ` FROM `ΠΕΛΑΤΗΣ` ')
clients = cur.fetchall()

cur.execute('SELECT `ID` FROM `ΓΗΠΕΔΟ` ')
fields_id = cur.fetchall()


while True:
    ###my changes
    user_pick =  input("1)if you want to check a customer reservation enter check /n 2)for sql orders enter 'sql' 3)to inser a reservation enter insert")
    if(user_pick == 'check'):
        print("here are all the available clients to checks ")
        cur.execute('SELECT `ΕΠΩΝΥΜΟ` FROM `ΠΕΛΑΤΗΣ`')
        names = cur.fetchall()
        print(names)
    elif(user_pick == 'insert'):
        c_id = input('pleaze give the id of the client you want to insert')
        
        for x in range(0,len(clients)):
            
            if(int(c_id) == clients[x][0]):
                field = input('enter the id of the field he wants to reserve')
                for i in range(0,len(fields_id)):
                    if(int(field) == int(fields_id[i][0])):
                       start_time = input('enter start time in this form "00:00:00" ')
                       end_time = input('give the end time in this form "00:00:00" ')
                       date = input('enter the date for the reservation')
                       cur.execute('INSERT INTO `ΕΝΟΙΚΙΑΖΕΙ`(`ΚΩΔΙΚΟΣ`,`ID`,`ΩΡΑ ΑΡΧΗΣ`,`ΩΡΑ ΛΗΞΗΣ`) VALUES (' + str(c_id) + ' , ' \
                                   + str(field) + ' , "'+ str(start_time) +'" , "'+str(end_time) +'" ); ')
                       print('succes')
                       cur.execute('commit')
                       
                    else:
                        
                       continue
                        
                        
            else:
                continue

#### edw teleiwnoun oi allages m

    line = input('>>>')
    if line == "":
        print ("byeeeeeeeeeeeee")
        break
    buffer += line
    print (buffer)
    if True: 
        try:
            buffer = buffer.strip()
            if buffer.lstrip().upper().startswith("SELECT"):
                count=0
                cur.execute(buffer)
                desc = [x[0] for x in cur.description]
                print(*desc, sep='\t')
                for row in cur.fetchall():
                    for i in row :
                        print (i, end = '\t')
                    print()
                    count +=1
                    if count%30==0:
                        reply = input ( "....more ? (y/n)")
                        if reply != "y" :
                            break
                        else:
                            print ()
            else:
                cur.execute(buffer)
                cur.execute('commit')
            print ("σύνολο :", cur.rowcount )
        except pymysql.Error as e:
            print ("An error occurred:", e)
        buffer = ""
cur.execute('commit')        
con.close()
