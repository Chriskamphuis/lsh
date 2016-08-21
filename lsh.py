import numpy as np  # Numpy is used to have more control over the datatypes.


class lsh:

    def __init__(self):
        print("")

    '''
    Creates a shingle set of a text document.
    Uses read(1) to extract char from textdocuments, so it extracts bytes which
    means the shingles are actually created with the bytes. Which might be
    troublesome if you use special characters.
    '''
    def shingle(self, document, w=5, token='char'):
        shingle_list = np.array([])
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
                            shingle = ''
                            for t in buf:
                                shingle += t
                            shinglehash = hash(shingle) % (2**32)
                            shingle32 = np.uint32(shinglehash)
                            shingle_list = np.append(shingle_list, shingle32)
            elif token is 'word':
                word_buf = ''
                while True:
                    c = doc.read(1)
                    if not c:
                        break
                    elif c is not '\n' and c is not ' ' and c is not '\t':
                        word_buf += c
                    elif word_buf is not '':
                        for i in range(w-1):
                            buf[i] = buf[i+1]
                        buf[w-1] = word_buf
                        if buf[0] is not '':
                            shingle = ''
                            for t in buf:
                                shingle += t
                                shingle += ' '
                            shingle = shingle[0:-1]
                            shinglehash = hash(shingle) % (2**32)
                            shingle32 = np.uint32(shinglehash)
                            shingle_list = np.append(shingle_list, shingle32)
                        word_buf = ''

            else:
                print('invalid token')
                exit(0)
        return np.unique(shingle_list)

    '''
    Jaccard function for determining similarity between sets.
    '''
    def jaccard(self, set1, set2):
        intersect = np.intersect1d(set1, set2)
        union = np.union1d(set1, set2)
        return float(len(intersect))/float(len(union))

a = lsh()
b = a.shingle("test.txt")
c = a.shingle("test2.txt")
print(a.jaccard(b, c))
