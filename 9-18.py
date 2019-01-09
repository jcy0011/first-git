import random
with open('vocabulary.txt') as fh:
    totallines = 0
    adic = {}
    index = 1
    for line in fh:
        word = line.strip().split(': ')
        adic[index] = (word[0], word[1])
        index = index + 1
    while True:
        quiz = adic[random.randint(1, index-1)]
        answer = quiz[0]
        ask = input('%s: ' % (quiz[1]))
        if ask == 'q':
            break
        elif ask == answer:
            print('맞았습니다!')
        else:
            print('틀렸습니다. 정답은 %s입니다.' % (answer))
