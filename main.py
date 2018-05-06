import csv, Levenshtein, re
from roster import *
from grademaker import *

GRADES = {}

def Calculate(student):
    if student not in GRADES: return 0
        return GRADES[student]

def GetNetid(row, roster):
    netid = row[2].lower()
        return roster.FuzzyMatch(netid)

regex = re.compile('[^a-zA-Z]')
def GetFruit(row, fruits):
    fruit = row[3]
        fruit = fruit.lower()
        fruit = regex.sub('', fruit)
        if fruit in fruits: return fruit
        for f in fruits:
            if Levenshtein.distance(f, fruit) < 3: return f

def SetGrade(student, fruit):
    if student is None: return
        grade = 1 if fruit else 0
        # assert student not in GRADES, 'Duplicate student ' + str(student)
        GRADES[student] = grade

if __name__ == '__main__':
    rostermaker = RosterMaker('secret/roster.csv')

        resultsfile = 'secret/week4.csv'
        with open(resultsfile, 'r') as csvfile:
            reader = csv.reader(csvfile)
                rows = [row for row in reader][1:]
                fruits = ['dragonfruit', 'lemon', 'persimmon', 'kumquat']
                for row in rows:
                    netid = GetNetid(row, rostermaker)
                        fruit = GetFruit(row, fruits)
                        SetGrade(netid, fruit)

        calculator = Calculator(rostermaker, Calculate)
        calculator.CalculateAll()

        csv = CSVMaker('Discussion Week 4')
        csv.MakeCSV(rostermaker, calculator)
