from roster import RosterMaker
from types import *

class Calculator(object):
	"""Class for calculating grades. Takes in a roster and a method name for calculating the grade itself. Make sure to define said method in your script."""
	def __init__(self, rostermaker, method):
		super(Calculator, self).__init__()
		self._roster = rostermaker
		assert not method is None, 'No method defined.'
		self._method = method

		self.grades = {}

	def CalculateAll(self):
		for netid, student in self._roster.students.items():
			self.grades[netid] = self.Calculate(student)
	
	def Calculate(self, student):
		name = student.name
		result = self._method(student)
		assert not result is None, 'Calculation was none. Student: ' + name
		assert type(result) is IntType, 'Result was not an integer. Got: ' + str(result)
		return result