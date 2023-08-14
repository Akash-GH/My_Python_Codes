import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

if int(time.strftime('%H')) < 12:
  print('Good Morning!')
elif int(time.strftime('%H')) == 12:
  print('Good Afternoon!')
elif int(time.strftime('%H')) > 12:
  print('Good Evening!')
else:
  print('Good Night')

hour = time.strftime('%H')
if (int(hour) > 5 and int(hour) < 12):
  print('Good Morning!')
elif (int(hour) == 12 and int(hour) > 12):
  print('Good Afternoon!')
elif (int(hour) > 12 and int(hour) <= 17):
  print('Good Evening!')
else:
  print('Good Night')