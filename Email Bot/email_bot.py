import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

login_n = input("Login_Email: ")

login_p = input("Login_Password: ")

mssg = input("Message: ")

recipents = []
recipent = int(input("Number_Of_Recipent: "))

for number in range(recipent):
    recipent_name = input("Recipent Email: ")
    recipents.append(recipent_name)

server.login(login_n,login_p)
server.sendmail(login_n,
                recipents,
                mssg
                )
