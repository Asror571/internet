import socket
import my_databases
import mysql.connector

# MySQL bazasiga ulanish
baza = mysql.connector.connect(    
    host=my_databases.host,
    user=my_databases.user,        
    password=my_databases.password, 
    database=my_databases.database
)

cursor = baza.cursor()

with open("domains.txt") as input_file:
    domains = input_file.read().split()

    for domain in domains:
            try:
                ip = socket.gethostbyname(domain)
                cursor.execute("INSERT INTO Domain (domain, ip) VALUES (%s, %s)", (domain, ip))
            except :
                 print(" {domain} ning Ip manzil topilmadi ")

baza.commit()
cursor.close()
baza.close()
