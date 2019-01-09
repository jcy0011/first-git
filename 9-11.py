while True:
    line = input('영어 단어를 입력하세요: ')
    if line == 'q':
        break
    else:
        meaning = input('한국어 뜻을 입력하세요: ')
        with open('vocabulary.txt', 'a') as fh:
            fh.write("%s: %s\n" % (line, meaning))
