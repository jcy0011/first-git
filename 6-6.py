import random
a = random.randint(1,20)
i = 4
while i >= 1:
    j = int(input('기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ' % (i)))
    if i == 1:
        if a != j:
            print('아쉽습니다. 정답은 %d였습니다.' % (a))
    if j > a:
        print('Down')
    elif j < a:
        print('Up')
    else:
        print('축하합니다. %d번만에 숫자를 맞추셨습니다.' % (5 - i))
        break
    i = i - 1
