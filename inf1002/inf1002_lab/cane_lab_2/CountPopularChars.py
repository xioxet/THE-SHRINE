import sys

def CountPopularChars():
    inp = sys.argv[1]
    z = {}
    for i in inp.lower():
        if i not in z:
            z[i] = 0
        z[i] += 1
    top_5 = sorted([(z[i], 256-ord(i)) for i in z], reverse=True)[:5]

    print(','.join([f'{i[0]}:{chr(256-i[1])}'[::-1] for i in top_5]))

if __name__ == "__main__":
    CountPopularChars()



