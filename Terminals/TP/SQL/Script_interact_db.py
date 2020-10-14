import mysql.connector
import serial, time

ser = serial.Serial('/dev/ttyACM0', 9600)
valeur = ser.readline()
valeur = valeur.decode('utf-8')
ser.close()
valeur = valeur.split(",")
cnx = mysql.connector.connect(user='gr4', password='pg4',host='10.23.17.25',database='capteurs')
cursor = cnx.cursor()
query = ("INSERT INTO MESURESG4 (valeur_temp, valeur_humi) values ('" + valeur[1].rstrip()+ "' , '" + valeur[0].rstrip()+ "')")
query = (query)
cursor.execute(query)
cnx.commit()
for i in cursor :
    print(i[0])
    print("")
cnx.close()
