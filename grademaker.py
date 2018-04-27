import csv, os
from roster import RosterMaker

class Calculator(object):
	"""Class for calculating grades.
	Takes in a roster and a method name for calculating the grade itself."""
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
		assert type(result) is int, 'Result was not an integer. Got: ' + str(result)
		return result


class CSVMaker(object):
	"""Given a list of students and their grades, makes an appropriate csv for upload."""

	HEADER_BASE = ['Student', 'ID', 'SIS User ID', 'SIS Login ID', 'Section']

	def __init__(self, assignment_name, output_file = 'secret/out.csv'):
		super(CSVMaker, self).__init__()

		assert not assignment_name is None
		assert type(assignment_name) is str, 'Assignment name invalid.'
		self._assignment_name = assignment_name
		
		self._output_file = output_file
		
		self._rows = []
		self._header = CSVMaker.HEADER_BASE + [self._assignment_name]
		
	
	def MakeCSV(self, roster, calculator):
		students = roster.students
		grades = calculator.grades

		for netid, student in students.items():
			if netid in grades:
				self._rows.append(self.MakeRow(student, grades[netid]))
			else:
				print('Student missing from grades: ' + student.name)

		self.WriteCSV()

	def MakeRow(self, student, grade):
		return {
		'Student': student.name,
		'ID': student.canvas_id,
		'SIS User ID': student.netid,
		'SIS Login ID': student.netid,
		'Section': student.section,
		self._assignment_name: str(grade)
		}

	def WriteCSV(self):
		print('Writing to output file: ' + self._output_file)

		with open(self._output_file, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=self._header)
			writer.writeheader()
			for row in self._rows: writer.writerow(row)
