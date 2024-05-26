"""
This Python file will call the code written in getInput, match, and outputMatches.
"""
import numpy as np
import pandas as pd

import getInput
import match
import outputMatches
import calculateEffectiveness as calcEf

codes = match.formatCSV('../../sampleCodes.csv')

matches = match.createMatches(codes)
print(matches)

stdev = calcEf.calcStDev(matches)
print()
print("Standard Deviation: ", stdev)