class lsh:

    def __init__(self):
        print('')

    def shingle(self, document, w=3, token='char'):
        shingle_list = []
        buf = ['' for i in range(w)]
        with open(document, 'r') as doc:
            if token is 'char':
                while True:
                    c = doc.read(1)
                    if not c:
                        break
                    elif c is '\n' or c is ' ' or c is '\t':
                        continue
                    else:
                        for i in range(w-1):
                            buf[i] = buf[i+1]
                        buf[w-1] = c
                        if buf[0] is not '':
                            shingle = ""
                            for t in buf:
                                shingle += t
                            shingle_list.append(shingle)

            elif token is 'word':
                print(token)
            else:
                print('invalid token')
                exit(0)
        return set(shingle_list)
