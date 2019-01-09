import random
ans1 = random.randrange(10)
ans2 = random.randrange(10)
ans3 = random.randrange(10)
print('0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.')
num = 0
while True:
    print('세 수를 하나씩 차례대로 입력하세요.')
    guess1 = int(input("1번째 수를 입력하세요: "))
    while True:
        guess2 = int(input("2번째 수를 입력하세요: "))
        if guess1 == guess2:
            print('중복되는 수 입니다. 다시 입력해주세요.')
            continue
        while True:
            guess3 = int(input("3번째 수를 입력하세요: "))
            if guess3 == guess2 or guess3 == guess1:
                print('중복되는 수 입니다. 다시 입력해주세요.')
                continue
            else:
                break
        break

    ans = [ans1, ans2, ans3]
    guess = [guess1, guess2, guess3]
    s, b = 0, 0
    for i in range(3):
        if ans[i] == guess [i]:
            s = s + 1
    for i in range(3):
        if guess[i] in ans:
            b = b + 1
    b = b - s
    print("%dS %dB" % (s, b))
    num = num + 1
    if s == 3:
        print('축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.' % (num))
        break
    else:
        continue
