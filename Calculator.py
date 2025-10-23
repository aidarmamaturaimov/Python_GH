x = float(input('What is the total bill amount?'))
y = float(input('What percentage tip would you like to give?'))

tip = x*(y/100)
total = x + tip

print(f'The total tip is: ${tip:.2f}')
print(f'The total bill is: ${total:.2f}')