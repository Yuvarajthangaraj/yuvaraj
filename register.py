#!C:\Python311\python.exe
import cgi
import mysql.connector
print("content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1>Welcome</h1>")
form=cgi.FieldStorage()
ffirstname=form.getvalue("firstname")
flastname=form.getvalue("lastname")
femail=form.getvalue("email")
fcontact=form.getvalue("contact")
print("<h1>",ffirstname,"<h1>")
print("<h1>",flastname,"<h1>")
print("<h1>",femail,"<h1>")
print("<h1>",fcontact,"<h1>")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myschool")
mycursor=mydb.cursor()
sql="INSERT INTO myclass(firstname,lastname,email,contact) VALUES(%s,%s,%s,%s)";
val=(ffirstname,flastname,femail,fcontact)
mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")