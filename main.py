class Mlops:
	def _init_(self,totalStudents):
		self.totalStudents=totalStudents
	
	def getTotalStudents(self):
		return self.totalStudents

	def addStudent(self):
		self.totalStudents=self.totalStudents + 1

	def removeStudent(self):
		self.totalStudents=self.totalStudents - 1

	def getClassName(self):
		return "Machine Leraning Opertaions CS-B Task"
	
    #vfvf