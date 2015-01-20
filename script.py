#!/usr/bin/env python
import csv
import re

def bgdhypothesis(t0, t1):
    return lambda x: t0 + t1*x

def bgdcost(h, M):
    return 1.0/2.0*len(M)*sum([(h(x) - y)**2 for x,y in M])

def bgdnext(t0, t1, h, M, alpha):
    return (
        t0 - alpha*1.0/len(M)*sum([h(x) - y for x,y in M]),
        t1 - alpha*1.0/len(M)*sum([(h(x) - y)*x for x,y in M])
    )

def bgd(M, alpha, epsilon, iterations):

    t0, t1 = 0.0, 0.0
    h = bgdhypothesis(t0, t1)
    J = bgdcost(h, M)

    for n in range(iterations):

        t0, t1 = bgdnext(t0, t1, h, M, alpha)
        h = bgdhypothesis(t0, t1)
        e = bgdcost(h, M)

        if abs(J - e) <= epsilon:
            return h

        J = e

    raise Exception('Could not find hypothesis')

def gettrainingset():
    with open('rentals.csv') as f:
        
        reader = csv.reader(f)
        header = None
        M = []

        for row in reader:

            if not header:
                header = tuple(row)
                continue

            pcm, rooms = float(re.sub(r'[^\d\.]', '', row[0])), float(row[1])

            M.append((pcm, rooms))

    return M

def main():

    M = gettrainingset()
    roomstopcm = bgd([(rooms, pcm) for pcm, rooms in M], 0.1, 0.01, 1500)
    pcmtorooms = bgd(M, 0.000001, 0.01, 1500)

    rooms = 2
    pcm = roomstopcm(rooms)
    print('For {0} PCM you could get {1} rooms'.format(pcm, rooms))

    pcm = 1400
    rooms = pcmtorooms(pcm)
    print('For {0} PCM you could get {1} rooms'.format(pcm, rooms))

if __name__ == '__main__':
    main()
