

import sys
import os
import math


def closestPair(fileName):

    # Gets File

    with open(fileName) as f:
        content = f.readlines()
        points = []
    for (i, p) in enumerate(content):
        if p != '\n':
            p = p.replace(' ', ',').replace('\n', '')
            temp = p.split(',')
            p = [int(p) for p in temp]
            p = tuple(p)
            t = p
            points.append(t)

    # Sort points by both x and y coord

    Px = sorted(points, key=lambda x: x[0])
    Py = sorted(points, key=lambda y: y[1])

    def brute_force_remaining(P):

        closest_pair = (P[0], P[1])
        bestDistance = calc_distance(closest_pair)
        for i in range(len(P)):
            for j in range(i + 1, len(P)):

                # Calculate Distance

                dist = calc_distance((P[i], P[j]))

                # Check if better than bestDistance if so update

                if dist < bestDistance:
                    bestDistance = dist
                    
                    closest_pair = (P[i], P[j])

        return closest_pair

    def calc_distance(points):
        x = math.sqrt((points[0][0] - points[1][0]) ** 2
                      + (points[0][1] - points[1][1]) ** 2)
        return x

     # Closest Points Divide & Conquer Function

    def rec_closest_points(Px, Py):
        n = len(Px)

         # Base Case for Algorithm

        if len(Px) < 4:
            return brute_force_remaining(Px)

        # Split the Pairs in 2 parts

        Px1 = Px[:n / 2]
        Px2 = Px[n / 2:]
        Py1 = Py[:n / 2]
        Py2 = Py[n / 2:]

        # Recursivly Get Closest Points in the halves

        (tempPx1, tempPy1) = rec_closest_points(Px1, Py1)
        (tempPx2, tempPy2) = rec_closest_points(Px2, Py2)

        # Calculate Distance

        distance_left_half = calc_distance((tempPx1, tempPy1))
        distance_right_half = calc_distance((tempPx2, tempPy2))
        if distance_left_half > distance_right_half:
            closest_pair = (tempPx2, tempPy2)
            best_so_far = distance_right_half
        else:
            closest_pair = (tempPx1, tempPy1)
            best_so_far = distance_left_half

        # Check remaining points if not in same half


        mergePx = Px1 + Px2

        S = filter(lambda x: x[0] - Px1[-1][0] < best_so_far, mergePx)

        sorted_y = sorted(S, key=lambda y: y[1])
        if len(sorted_y) <= len(S) and len(sorted_y) > 1:
            splitPair = brute_force_remaining(sorted_y)
            if calc_distance(splitPair) < best_so_far:
                closest_pair = splitPair

        # Check if points have a distance less than best so far

        for i in range(len(sorted_y)):
            for j in range(i + 1, i):
                dist = calc_distance((sorted_y[i], sorted_y[j]))
                if dist < best_so_far:
                    best_so_far = dist
                    closest_pair = (sorted_y[i], sorted_y[j])

        return closest_pair

    #Starts the Recursive Algorithm
    def find_closest_pair(x_sorted, y_sorted):
        points = rec_closest_points(x_sorted, y_sorted)

        # I couldnt get the Distance to return so I had to call the distance function once more to calculate.
        # This is only for printing to the console

        best_so_far = calc_distance(points)
        return {'pair': points, 'distance': best_so_far}


    #returns a Dictionary with Pair of Points and Distance
    return find_closest_pair(Px, Py)


def main():

    
    if len(sys.argv) <= 1:

        fileName = '10points_test.txt'
    else:

        fileName = sys.argv[1]

    # calls the Closest Pair algorithm with file

    p = closestPair(fileName)
    print 'The minimum distance is: ' + str(p['distance']) + ': ' \
        + str(p['pair'][0]) + '<---->' + str(p['pair'][1])

    return 0


if __name__ == '__main__':
    main()


			
