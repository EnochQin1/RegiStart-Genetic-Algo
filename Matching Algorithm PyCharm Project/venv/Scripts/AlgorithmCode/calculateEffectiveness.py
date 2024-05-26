"""
This file contains all the methods to determine the performance of the algorithm.
"""
import csv
import numpy as np
import pandas as pd
import math
from statistics import stdev

"""
This method calculates how equitable matches are by determine the standard deviation of the number of relationship points
per person, given the matches made.
"""
def calcStDev(matches):
    orgTotals = []
    for index, row in matches.iterrows():
        org = row['organizer']
        found = False
        for r in orgTotals:
            if r[0] == org:
                r[1] += int(float(row['relationship']))
                found = True
        if not found:
            orgTotals.append([org, int(float(row['relationship']))])

    stdevList = []
    for row in orgTotals:
        stdevList.append(row[1])

    return stdev(stdevList)
