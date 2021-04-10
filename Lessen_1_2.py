time = int(input ("Введите врямя в секундах"))
hour = time // 3600
minutes = (time - (hour * 3600)) // 60
seconds = ((time - (hour * 3600)) - (minutes * 60))
#print(f"{hour}:{minutes}:{seconds}")
print("{:02d}:{:02d}:{:02d}".format(hour, minutes, seconds))

