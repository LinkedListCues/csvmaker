import csv, Levenshtein, re
import argparse
from roster import *
from grademaker import *

GRADES = {}

def Calculate(netid):
    if netid not in GRADES: return 0
    return GRADES[netid]

def GetNetid(row, roster):
    netid = row[2].lower()
    return roster.FuzzyMatch(netid)

regex = re.compile('[^a-zA-Z]')
def GetWord(row, word):
    word = row[3]
    word = word.lower()
    word = regex.sub('', word)
    if word in words: return word
    for w in words:
        if Levenshtein.distance(w, word) < 3: return w

def SetGrade(netid, word):
    if netid is None: return
    grade = 1 if word else 0
    # assert student not in GRADES, 'Duplicate student ' + str(student)
    GRADES[netid] = grade

if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description='Process and make a Canvas csv.')
#    parser.add_argument('roster', metavar='f', type=str, nargs=1,
#            help='The csv rotserfile to use.')

    rostermaker = RosterMaker('secret/roster.csv')

    resultsfile = 'secret/week5.csv'
    with open(resultsfile, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader][1:]

    words = ['giraffe', 'snake', 'caterpillar', 'camel']
    for row in rows:
        netid = GetNetid(row, rostermaker)
        word = GetWord(row, words)
        SetGrade(netid, word)

    calculator = Calculator(rostermaker, Calculate)
    calculator.CalculateAll()

    csv = CSVMaker('Discussion Week 5')
    csv.MakeCSV(rostermaker, calculator)
