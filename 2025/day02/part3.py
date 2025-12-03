#!/usr/bin/env python3
# https://www.reddit.com/r/adventofcode/comments/1pc9mrg/comment/nrxm7kk/

def process():
    sum = 0
    numbers = {}
    for total_len in range(1, 11):
        for chunk_len in range(1, 6):
            strformat = "{:0" + str(chunk_len) + "d}"
            if total_len % chunk_len != 0: continue
            nr_chunks = total_len//chunk_len
            if nr_chunks < 2: continue

            min = pow(10, chunk_len-1)
            max = pow(10, chunk_len)
            for i in range(min, max):
                chunk = strformat.format(i)
                number = ''
                for j in range(0, nr_chunks):
                    number += chunk
                if int(number) >= 1 and int(number) <= 4294967296:
                    if not number in numbers:
                        numbers[number] = 1
                        sum += int(number)
    print(sum)
    return sum

assert(process() == 88304989965662)

