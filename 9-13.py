with open('vocabulary.txt', 'r') as fh:
    for line in fh:
        word = line.strip().split(': ')
        quiz = input('%s: ' % (word[1]))
        if quiz == word[0]:
            print('맞았습니다!')
        else:
            print('아쉽습니다. 정답은 %s입니다.' % (word[0]))