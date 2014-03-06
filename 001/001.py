number = 1000 * [-1]

i = 0
while True:
    number[i] = int(raw_input(""))
    if number[i] == 42:
        break
    i += 1
    
for j in range(i):
    print(number[j])
