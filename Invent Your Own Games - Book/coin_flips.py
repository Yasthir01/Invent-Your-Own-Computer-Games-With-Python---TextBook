import random
print('I will flip a coin 1000 times! Guess how many times it will come up as Heads.'
      '(press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads += 1
    flips += 1

    if flips == 900:
        print(f'900 flips and there have been {heads} Head\'s')

    if flips == 100:
        print(f'100 tosses down and heads has come up {heads} times')

    if flips == 500:
        print(f'Halfway there and Heads has come up {heads} times so far')

print()
print(f'Out of 1000 tosses, Head\'s has come up {heads} times!')
print('Were you close?')
