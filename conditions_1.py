cur_speed = int(input('Current speed: '))

if cur_speed > 80:
    fin_value = (cur_speed - 80)*7
    print ("You should pay: "+ str(fin_value) +" dollars")
else:
    print("you are good to go!")


