def collatz(num):
    if num == 1:
        return
    if not num % 2:
        num = num // 2;
    else:
        num = 3*num + 1
    print(num)
    return collatz(num)

while True:
    try:
        num = int(input())
        collatz(num)
        break
    except ValueError:
        print('You shuold type an integrate number.')


