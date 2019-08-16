x = input("x value: ")
y = input("y value: ")
function = input('Add or Subtract: ')
if function == 'Add':
    sum = int(x) + int(y)
    print(sum)
elif function == 'Subtract':
    sub = int(x) - int(y)
    print(sub)
input("Press enter to exit")