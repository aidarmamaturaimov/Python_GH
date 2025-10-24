x = float(input('What is the total bill amount? '))
y = float(input('What percentage tip would you like to give? '))

tip = x*(y/100)
total_amount = x + tip

print(f'The total tip is: ${tip:.2f}')
print(f'The total bill is: ${total_amount:.2f}')

if tip > 20:
    print("Thank you for your generosity!")

split_bil = int(input('How many people are splitting the bill? '))

names = []
for i in range(split_bil):
    names.append(input('What is your name? '))

share_amount = total_amount / split_bil
print('The amount each person must pay: ', share_amount)