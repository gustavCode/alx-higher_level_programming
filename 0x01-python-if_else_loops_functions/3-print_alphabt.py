#!/usr/bin/python3
for x in range(97, 123):
    if x == 101 or x == 'q':
        continue
    print('{:c}'.format(x), end='')
