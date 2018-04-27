import csv, os, Levenshtein

class ClassConfig(object):
	"""Makes a class configuration given a .json file containing the relevant information.
	See ClassConfig.MakeConfig"""
	def __init__(self, configfile):
		super(ClassConfig, self).__init__()
		self.configfile = configfile

class RosterMaker(object):
	"""Given a .csv file from Canvas, makes a roster container class object."""
	def __init__(self, file):
		super(RosterMaker, self).__init__()
		
		assert not file is None and os.path.isfile(file), 'File does not exist: ' + str(file)
		self._file = file
		
		self.students = {} # students dictionary, keyed on netid
		self.InitializeRoster()

	def InitializeRoster(self):
		with open(self._file, 'rU') as csvfile:
			self._reader = csv.reader(csvfile)
			rows = [row for row in self._reader]
			# skip the header; skip the "Points Possible" row
			studentlist = [Student(row) for row in rows[2:]]
			for student in studentlist:
				self.students[student.netid] = student

	def FuzzyMatch(self, netid):
		if netid in self.students: return netid
		for key in self.students.keys():
			# use the magic constant of 2 for now?
			if Levenshtein.distance(netid, key) < 2: return key
		return None
			


def Validate(value, name):
	result = str(value)
	assert not result is None, name + ' is None.'
	assert len(result) > 0, name + ' is the empty string.'
	return result

class Student(object):
	"""Container class for Student information. No, I'm not very good at Python."""
	def __init__(self, row):
		super(Student, self).__init__()
		self.row = row
		self.name = Validate(row[0], 'Name')
		self.canvas_id = Validate(row[1], 'Canvas ID')
		self.netid = Validate(row[2], 'NETID')
		self.section = Validate(row[4], 'Section')