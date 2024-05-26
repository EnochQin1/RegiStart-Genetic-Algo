"""
This file is used to match targets and organizers based on the input provided in getInput.
This includes creating relationship codes.
"""
import csv
import numpy as np
import pandas as pd


def formatCSV(filepath):
    with open(filepath) as codesCSV:
        codesList = []
        codesReader = csv.reader(codesCSV)
        for row in codesReader:
            numTargOrg = row[0].split("_")
            codesList.append([numTargOrg[2], numTargOrg[1], numTargOrg[0]])
        codesDf = pd.DataFrame(codesList, columns=["organizer", "target", "relationship"])
    return codesDf


def dropItem(targetName, codesDf, columnName):
    for index, row in codesDf.iterrows():
        if row[columnName] == targetName:
            codesDf = codesDf.drop([index], axis=0)
    return codesDf


def createMatches(codesDf):
    columns = ['organizer', 'target', 'relationship']
    matches = pd.DataFrame(columns=columns)

    targetsNotRemaining = []
    organizersNotRemaining = []
    # Calculates average number of targets per organizer
    avg = codesDf['target'].nunique() / codesDf['organizer'].nunique()

    # Give every organizer their top target, if it is not already taken
    # If their top target is taken, give them the next highest target
    for index, row in codesDf.iterrows():
        if row['organizer'] not in matches['organizer'].unique() and row['target'] not in targetsNotRemaining:
            matches = matches.append({'organizer':row['organizer'],'target':row['target'],
                                      'relationship':row['relationship']}, ignore_index=True)
            targetsNotRemaining.append(row['target'])

    # Work down the DataFrame and assign each match, as long as the organizer has less than the maximum
    # number of targets
    for index, row in codesDf.iterrows():
        if matches['organizer'].value_counts()[row['organizer']] + 1 < avg and row['target'] not in targetsNotRemaining:
            matches = matches.append({'organizer':row['organizer'],'target':row['target'],
                                     'relationship':row['relationship']}, ignore_index=True)
            targetsNotRemaining.append(row['target'])
        # Max organizers out of targets at 1.25x the average number of targets per person
        elif matches['organizer'].value_counts()[row['organizer']] + 1 > (1.25 * avg):
            print("hi")
            organizersNotRemaining.append(row['organizer'])

    # For any target who only has relationships with maxed out individuals, just match
    # them with their best relationship, even if said person is maxed out
    for index, row in codesDf.iterrows():
        if row['target'] not in targetsNotRemaining:
            matches = matches.append({'organizer':row['organizer'],'target':row['target'],
                                     'relationship':row['relationship']}, ignore_index=True)
            targetsNotRemaining.append(row['target'])

    return matches
