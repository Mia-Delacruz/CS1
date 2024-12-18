import time                                                     #import start time 
import datetime                                                 #import date 
                                                                #insert all different colored text options 
def colored_text(text, color_name):
    color_codes = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[37m'
    }

    print(color_codes.get(color_name) + text + color_codes.get('reset'))   #print colored text gets color code

current_time = datetime.datetime(2024, 10, 23, 6, 30, 0)        #sets current time to 6:30AM      
print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
colored_text("Alarm!", "red")                                   #set alarm color to red 

while True:                                                     #insert while true 
    snooze = input("snooze? yes/no: ").lower()                  #import snooze 

    if snooze == "yes":                                         #if snooze is yes sleep for another 8 minutes 
        colored_text("sleep for another 8 minutes!", "green")
        time.sleep(2)                                           #waits 2 seconds
        current_time += datetime.timedelta(minutes=5)           #adds 5 minutes to current time
    elif snooze == "no":
        time.sleep(1)                                           #waits 1 second
        current_time += datetime.timedelta(minutes=1)           #adds 1 minute to current time
        break                                                   #break from text 
    else:
        colored_text("Invalid response", "red")
print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
print("\nGood job!")                                            #print good job 
print("walk to the bathroom")                                   #brush teeth 
print("brush my teeth")                                         #do skin care and wash face 
print("do skincare and wash face\n")
current_time += datetime.timedelta(minutes=10)                  #adds 10 minutes to current time
print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
print()

while True:                                                     #insert while true for culred hair option 
    curl = input("curl hair? yes/no: ").lower()                 #if curl is yes 
    if curl == "yes":                                           #print curl hair with wand
        print("curl hair with wand!")                       
        time.sleep(3)                                             #time.curl
        current_time += datetime.timedelta(minutes=10)           #adds 10 minutes to current time
        break                                                    #break
    elif curl == "no":                                           #else if curl is no 
        break                                                    #break 
    else:                                                        #if anything else
        print("Invalid response")                                #print an invalid response 

print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
print("\nGood job!")                                            #print good job 
print("walk out of bathroom and into room")                     #walk out of bathroom and into room 
print("open closet to pick outfit\n")                           #open closet and pick out an outfit

while True:                                                     #have a while true
    jeans_and_polo = input("Do you want to wear jeans and a polo? yes/no: ").lower()                               #option for jeans and polo 
    if jeans_and_polo =="no":                                   #if jeans and polo is no 
        print("look for another outfit")                            #print look for another outfit 
        print("wear skirt and a polo")           #choose skirt and polo 
        time.sleep(1)                                              #add current time 
        current_time += datetime.timedelta(minutes=5)               #adds 5 minutes to current time
        break
    elif jeans_and_polo =="yes":                                  #skirt and polo is yes 
        print("put on jeans and a polo!")                            #put on skirt and polo instead of jeans and polo 
        time.sleep(1)                                              #add current time 
        current_time += datetime.timedelta(minutes=5)               #adds 5 minutes to current time
        break
    else:                                                           #if anything else 
        print ("invaling respose")                                  #invalid response 

print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
print("Good job!")                                              #print good job 
print("do makeup")                                              #do makeup 
current_time += datetime.timedelta(minutes=10)
print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 

while True:                                                     #insert while true
    mascara = input("mascara? yes/no: ").lower()                      #mascara option yes or no 
    if mascara == "yes":                                            #if yes
        print("curl and put mascara on eyelashes")                  #curl and put mascara on 
        time.sleep(1)                                             #insert time 
        current_time += datetime.timedelta(minutes=3)           #adds 3 minutes to current time
    elif mascara =="no":                                            #if mascara is no 
        break                                                       #break 
    else:                                                           #if anything else 
        print ("invalid response")                                  #print invalid response 

print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
print("Good job!")                                              #good job 
print("walk to the kitchen")                                    #walk to kitchen 
current_time += datetime.timedelta(minutes=1)
while True:                                                     #insert while true 
    eat_breakfast = input("eat breakfast? yes/no: ").lower()    #option to eat breakfast yes or no 
                                                                #if no 
    if eat_breakfast == "no":                                   #good job 
        print("good job!")                                      #break 
        break                                                   #if yes eat an apple 
    elif eat_breakfast == "yes":                                #insert current time 
        print("Eat an apple")                                   #break
        current_time += datetime.timedelta(minutes=5)           #if anything else invalid response 
        break
    else:
        print("invalid response")
print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
print("get backpack")                                           #walk to door 
print("walk to the door")                                       #pick shoes 
current_time += datetime.timedelta(minutes=1)                   #get backpack 
print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 

while True:  
    grey_sneakers = input("Do you want grey sneakers? yes/no: ").lower()    #insert while true 
    if grey_sneakers == "yes":                                              #option for grey sneakers 
        print("Put them on")                                                #if yes put them on 
        current_time += datetime.timedelta(minutes=1)                       #insert current time again 
        break                                                               #break 
    elif grey_sneakers =="no":                                              #if no pick another color 
        print("Pick another color")                                         #display current time  
        current_time += datetime.timedelta(minutes=5)                       #break 
        break                                                               #anything else invlaid resonse 
    else:
        print("Invalid")
print(current_time.strftime("%H:%M:%S"))                        #displays current time as hours, minutes, seconds 
print("walk outside and leave for school")                      #walk outside leave for school 
