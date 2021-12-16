import requests, json, tkinter as tk
choice = input(
    "If you would like to login in, type l. If you would like to create an account, type c: ")
#validates username and password
def validation(user: str, passw: str, lines: list): 
    access = False
    for l in lines:
        aut = l.split(' ')
        if user == aut[0] and passw == aut[1]:
            access = True
            break
        elif user != aut[0] and passw != aut[1]:
            access = False
    return access
if(choice == 'l'):
    user = input("Enter your username: ")
    passw = input("Enter your password: ")
    # code for reading file
    file = open("userpassStore.txt")
    lines = file.readlines()
    validate = validation(user, passw, lines)    
    while validate == False:
        print("Username or Password was wrong, please try again. ")
        user = input("Enter your username: ")
        passw = input("Enter your password: ")
        validate = validation(user, passw, lines)
    print("Access Granted. ")
    file.close()
else:
    newUser = input("Enter the username you would like to use: ")
    newPass = input("Enter the password you would like to use: ")
    newEmail = input("Enter your email address: ")
    
    #code to write to the file
    file = open("userpassStore.txt", "a")
    toAppend = ["\n", newUser, " ", newPass, " ", newEmail]
    file.writelines(toAppend)
    print("Account Created. ")
    file.close()
city = input("What city would you like the weather for: ")
unit = input("Would you like the temperature in F or C: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=bf9ef23ce300c409b28c62a04c410427&units={}"
if unit == 'F': 
    url = base_url.format(city, "imperial")
elif unit == 'C':
    url = base_url.format(city, "metric")
else:
    url = base_url.format(city, "imperial")
    unit = 'F'
req = requests.get(url)
while req == False: 
    print("City not found")
    city = input("What city would you like the weather for: ")
    url = base_url.format(city)
    req = requests.get(url)
data = req.json()
print("Today's Weather: \n")
print("Outside: ", data.get("weather")[0].get("main"))
print("Temperature: ", data["main"].get("temp"))
print("Minimum Temperature: ", data["main"].get("temp_min"))
print("Maximum Temperature: ", data["main"].get("temp_max"))
print("Feels like: ", data["main"].get("feels_like"))

out = data.get("weather")[0].get("main")
temp = data["main"].get("temp")
minTemp = data["main"].get("temp_min")
maxTemp = data["main"].get("temp_max")
feels_like = data["main"].get("feels_like")

window = tk.Tk()
intro = tk.Label(text = "Today's Weather: ")
outside = tk.Label(text = "Outside: " + out)
tempe = tk.Label(text = "Temperature: " + str(int(temp)) + " degrees " + unit)
mTemp = tk.Label(text = "Minimum Temperature: " + str(int(minTemp)) + " degrees " + unit)
maTemp = tk.Label(text = "Maximum Temperature: " + str(int(maxTemp)) + " degrees " + unit)
fL = tk.Label(text = "Feels Like: " + str(int(feels_like)) + " degrees " + unit)
intro.pack()
outside.pack()
tempe.pack()
mTemp.pack()
maTemp.pack()
fL.pack()
window.mainloop()
