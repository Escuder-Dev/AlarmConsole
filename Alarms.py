import datetime
import time

invalid = True

while(invalid):
    #Get a valid user input for the alarm time
    print("Set a valid time for the alarm with the folliwing format (12:00) or (05.45)")
    userInput = input (">> ")

    #Conver input into an array such as [12, 00] or [5, 30]
    alarmTime = [int(n) for n in userInput.split(":")]
    
    #Set up limit parameters for hours (0 to 24) and minutes (0 to 59)
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] <0:
        invalid = True
    else:
        invalid = False
    #If time is not between this parameters will keep asking to set up a different time


#Number of second in an Hour, minute and second
seconds_hms = [3600, 60 , 1]

#Conver alarm time into seconds
alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)],alarmTime)])

#Use of dateTime function to determine the system current time and conver it into seconds
now = datetime.datetime.now()
currentTimeSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

#Time until alarm goes off in seconds
secondsAlarmOff = alarmSeconds - currentTimeSeconds

#Add daily second in case alarm is for next day (negative value)
if secondsAlarmOff < 0:
    secondsAlarmOff += 86400

#Display Alarm message
print("Alarm is set!")
print("The alarm will ring at %s" % datetime.timedelta(seconds=secondsAlarmOff))

#Use of time.sleep to wait for the seconds required to ring the alarm
time.sleep(secondsAlarmOff)

#Message when alarm goes off
print("Is time to check Email and Stock Market")


