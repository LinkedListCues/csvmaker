from roster import *
from grademaker import *

def Calculate(student):
	return 0

if __name__ == '__main__':
	rostermaker = RosterMaker('secret/roster.csv')
	calculator = Calculator(rostermaker, Calculate)
	calculator.CalculateAll()

	csv = CSVMaker('Discussion Week 4')
	csv.MakeCSV(rostermaker, calculator)