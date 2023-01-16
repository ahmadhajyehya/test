# for loop
for x in range(5):
    print(x)


for x in range(3,5):
    print(x)

for x in range(3,8,2):
    print(x)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1


# break statement
count = 0
while 1 > 0:
    print(count)
    count += 1
    if count >= 5:
        break

# continue statement
for x in range(5):
    if x == 3:
        continue
    print(x)
