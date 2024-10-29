#Create class Student
class Student:
  #Constructor
  def __intit__ (self, studentName, studentID, studentScore):
    self.studentName = name
    self.studentID = studentID
    self.studentScore = studentScore
  #Function for new students
  def add(self, studentName, studentID, studentScore):

    ob = Student(name, studentID, studentScore)
    ls.append(ob)

  def search(self, rn):
    for i in range(ls.__len__()):
      if(ls[i].rollno == rn):
        return i
