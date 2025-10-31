import random , os
random_num = random.randint(1,100)

with open("random_numbers.txt" , 'w' , encoding='utf-8') as f:
    f.write(str(random_num))

print(f"Random Number: {random_num}")
print(f"Random number saved to: {os.path.abspath('random_numbers.txt')}")

