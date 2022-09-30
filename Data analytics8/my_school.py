import sys
import datetime
import sys 
class Course:
    """
    course class to hold course info 
    """
    def __init__(self, code, courseScore=-1,coursename="",  C="E", CreditPoint=6):
        self.courseCode= code
        self.Name  = coursename
        self.score = courseScore
        self.CreditPoint=CreditPoint
        if "C" in C:
            self.Compulsory="*"
        else:
            self.Compulsory="-"
    def setTotalEnrolledStudent(self, n_students):
        self.n_students=n_students
    def setAverageOfCourse(self, avg):
        self.average=avg
    def printStats(self):
        string=""
        string+=self.courseCode
        string+="\t"
        string+=self.Compulsory
        string+=" "
        string+=self.Name
        string+="\t"
        string+=str(self.CreditPoint)
        string+="\t"
        string+=str(self.n_students)
        string+="\t"
        string+=str(self.average)
        string+="\n"
        
        return string
    def __str__(self):
        
        return self.printStats()
    
class Student:
    """
    student class to hold student info with list of course objects 
    """
    def __init__(self, studentID ):
        self.StudentID=studentID 
        self.courselist=[]
    def addCourse(self,course):
        # function to add courses
        self.courselist.append(course)
    def setName(self, name):
        self.name=name
    def setStudyMode(self,mode):
        self.study_mode=mode 
    def calculateGPA(self):
        """
        Function to calculate GPA
        """
        count=0
        points=0
        totalPoints= self.countCreditPoints() # to calculate all credit points 
        IsResultAnnounced=False # will tell us result is announced or not. 
        for i in self.courselist:
            if i.score==-1 or i.score==888:  # if exception case, donot consider it 
                continue
            elif i.score>=80:
                points+=(4*i.CreditPoint)
            elif i.score>=70:
                points+=(3*i.CreditPoint)
            elif i.score>=60:
                points+=(2*i.CreditPoint)
            elif i.score>=50:
                points+=(1*i.CreditPoint)
            else:
                points+=0
            IsResultAnnounced=True
            count+=1
        if IsResultAnnounced:  # if result announced is set true, then give 
            return points/totalPoints
        else:
            return -1  # this will tell, that result is not announced yet
        
    def CheckRequirement(self):
        """
        function to check student is meeting minimum requirments or not, FT=fulltime, PT=part time
        """
        creditPoints=0
        count=0
        for i in self.courselist:
            if i.score!=-1 and i.score!=888 and i.Compulsory=="*":
                count+=1
            if i.score!=-1 and i.score!=888:
                creditPoints+=i.CreditPoint;
        if ("FT" in self.study_mode and count>=3 and creditPoints>=50) or ("PT" in self.study_mode and count>=2 and creditPoints>=30):
            return " "
        else:
            return "!"
    def countCreditPoints(self):
        countPoint=0
        for i in self.courselist:
            if i.score==-1 or i.score==888:
                continue 
            countPoint+=i.CreditPoint
        return countPoint
    def countEnrolledCourses(self):
        count=0
        for i in self.courselist:
            if i.score==-1 or i.score==888:
                continue
            else:
                count+=1
        return count
    def __str__(self):
         # for displaying the student with course info 
        string=""
        count=0
        for i in self.courselist:
            if count==len(self.courselist):
                break
            count+=1
#             print(i.score, i.score==-1)
            if i.score==-1 or i.score==888:
                string+="  "
            else:
                string+=str(i.score)
            if len(str(i.score))>2:
                string+="     |  "
            else:
                string+="      |  "
        
        return str(self.StudentID)+"   |  "+string
class School:
    """
    Getting students and course info and initializing the objects 
    """
    def __init__(self):
        
        self.TotalStudents=0
        self.TotalCourses=0
        self.students=[]
        self.courseCodelist=[]
        self.AvailableCourses=[]
    def read_scores(self, file_name):
        self.data=None
        self.data=open(file_name).readlines() # read file and store data
        self.TotalStudents = int(self.data[0].split()[0])//10 # get most significant digit
        self.TotalCourses = int(self.data[0].split()[0])%10 # get least significant digit 
        self.courseCodelist= self.data[0].split()[1:] # get all course names 
        for i in range(1,len(self.data)):  # loop of remainig data 
            studentID = self.data[i].split()[0] # get studetn id 
            studentObject= Student(studentID) # initialize studtns object 
            # adding course of specific course  
            for j in range(1,len(self.data[i].split())):
                score=-1
                try:
                    score = int(float(self.data[i].split()[j])) # get score in each subject  
                except:
                    if 'x' in self.data[i].split()[j]:
                        score=-1
                    elif "TBA" in self.data[i].split()[j]:
                        score=888
                courseObject = Course(self.courseCodelist[j-1], score) # intializing course object 
                studentObject.addCourse(courseObject) # adding course info in student object 
            self.students.append(studentObject)
    def getTopStudent(self):
        """
        function to get top average with student id of top average 
        """
        sid=""
        max_avg=-1  
        for i in self.students: 
            average=0
            count=0
            for course in i.courselist:
                if course.score!=-1 and course.score!=888: # donot count if score is -1 or 8888
                    average+=course.score
                    count+=1
            average = average//count
            if max_avg<average:  # if max average is found, then store it with student id 
                max_avg = average
                sid=i.StudentID
        return sid, max_avg
        
    def __str__(self):
        string="\t|   "
        count=0
        lne="--------"
        lne+="|"
        for i in self.courseCodelist:
            string+=i
            lne+=   "----------|"
            if count==len(self.courseCodelist)-1:
                break
            string+="   |   "
            count+=1
        print(string)
        print(lne)
        for i in self.students:
            print(i)
        print(lne)
        topStudent, average = self.getTopStudent()
        print(self.TotalStudents," students  ",self.TotalCourses, " courses "," the top student is ", end="")
        print(topStudent," average ", average)
        return ""
    def GenerateCoursesReport(self, filename):
        """This function initialize the variables required course statistics """
        course_code_to_scores={} # this dictionary to store name of course as key and scores as values
        for course_cde in self.courseCodelist:
            course_code_to_scores[course_cde]=[]
        for stdnt in self.students: 
            for course in stdnt.courselist:
                if course.score!=-1 and course.score!=888:
                    course_code_to_scores[course.courseCode].append(course.score)
        data = open(filename).readlines()
        min_avg=999
        course_cid=""
        for i in data:
            splitLine = i.split()
            code= splitLine[0]
            courseName = splitLine[1]
            isCompulsary = splitLine[2]
            CreditPoints = int(splitLine[3])
            courseObject = Course(code, courseScore=-1,coursename=courseName,  C=isCompulsary, CreditPoint=CreditPoints)
            if len(course_code_to_scores[code])>0:
                avg = sum(course_code_to_scores[code])// len(course_code_to_scores[code])
                if min_avg>avg:
                    min_avg=avg
                    course_cid = code
            else:
                avg="--"  # if no student enrolled 
            n_students = len(course_code_to_scores[code])
            courseObject.setTotalEnrolledStudent(n_students)
            courseObject.setAverageOfCourse(avg)
            
            self.AvailableCourses.append(courseObject)
        # update student course 
        for cr in self.AvailableCourses:
            for st in self.students:
                for cr_st in st.courselist:
                    if cr.courseCode==cr_st.courseCode:
                        cr_st.Name=cr.Name
                        cr_st.CreditPoint=cr.CreditPoint
                        cr_st.Compulsory=cr.Compulsory
                        cr_st.n_students=cr.n_students
                        cr_st.average=cr.average
                        
        string = self.printCourseStatistic()
        string+="The worse performing course is "
        string+=str(course_cid)
        string+=" with an average "
        string+=str(min_avg)
        string+="\n\n"
        currentDateTime= datetime.datetime.utcnow().strftime("%d %m %Y %H:%M:")
        string = currentDateTime +" \n " +string 
        print(string)
        data=None
        try:
            data= open("courses_report.txt","r").readlines()
            fl = open("courses_report.txt","w")
            fl.write(string+"\n")
            for i in data:
                fl.write(i)
            fl.close()
        except:
            fl = open("courses_report.txt","w")
            fl.write(string+"\n")
            fl.close()
            
        print("courses_report.txt generated! ")
    def GenerateStudentReport(self, filename):
        data= open(filename).readlines()
        string=""
        string+="SID       Name          Mode       Enl.      GPA\n"
        for lin in data:
            lst = lin.split()
            for i in self.students:
                if (i.StudentID==lst[0]):
                    i.setName(lst[1])
                    i.setStudyMode(lst[2])
        string+="-"*len(string)
        string+="\n"
        for i in self.students:
            gpa=i.calculateGPA()
            if gpa==-1: # result not announced
                gpa="--"
            else:
                gpa=round(gpa,2)
            while(len(i.name)!=len("    Name    ")):
                i.name+=" "
            i.study_mode = "    "+i.study_mode;
            while(len(i.study_mode)!=len("    Mode   ")):
                i.study_mode+=" "
            enrol= str(i.countEnrolledCourses())
            enrol = "   "+enrol
            string+=str(i.StudentID)+"  "+str(i.name)+"  "+ i.study_mode+"  "
            string+=enrol+ str(i.CheckRequirement())+"     "+str(gpa)+"\n"
        fl = open("student_report.txt","w")
        fl.write(string)
        fl.close()
        print("student_report.txt generated!")
        return
    def GenerateStudentReportAtHDLevel(self, filename):
        data= open(filename).readlines()
        string=""
        string+="SID       Name          Mode       CrPt      GPA\n"
        for lin in data:
            lst = lin.split()
            for i in self.students:
                if (i.StudentID==lst[0]):
                    i.setName(lst[1])
                    i.setStudyMode(lst[2])
        string+="-"*len(string)
        string+="\n"
        sort_stud=[]
        for i in self.students:
            gpa=i.calculateGPA()            
            gpa=round(gpa,2)
            sort_stud.append([i,gpa])
        
        
        sort_stud.sort(key=lambda x:x[1],reverse=True)
        
        
        for i in [j[0] for j in sort_stud]:
            gpa=i.calculateGPA()
            if gpa==-1: # result not announced
                gpa="--"
            else:
                gpa=round(gpa,2)
            while(len(i.name)!=len("    Name    ")):
                i.name+=" "
            i.study_mode = "    "+i.study_mode;
            while(len(i.study_mode)!=len("    Mode   ")):
                i.study_mode+=" "
            enrol= str(i.countCreditPoints())
            enrol = "   "+enrol
            string+=str(i.StudentID)+"  "+str(i.name)+"  "+ i.study_mode+"  "
            string+=enrol+ str(i.CheckRequirement())+"     "+str(gpa)+"\n"
        

        currentDateTime= datetime.datetime.utcnow().strftime("%d %m %Y %H:%M:")
        string = currentDateTime +" \n " +string 
        print(string)
        data=None
        try:
            data= open("student_report.txt","r").readlines()
            fl = open("student_report.txt","w")
            fl.write(string+"\n")
            for i in data:
                fl.write(i)
            fl.close()
        except:
            fl = open("student_report.txt","w")
            fl.write(string+"\n")
            fl.close()
            
        print("student_report.txt generated!")
        
        return
    
    def printCourseStatistic(self):
        string=""
        string+="CID\tName\t\tPt.\tEnl.\tAvg."
        dot_line = "-"*2*len(string)
        string+="\n"
        string+=dot_line
        string+="\n"
        for i in self.AvailableCourses:
            string+=i.printStats()
        string+=dot_line
        string+="\n"
        
        return string
if __name__=="__main__":
    if len(sys.argv)<2:
        print("[Usage:] Python my_school.py <scores file> ")
    else:
        filename=sys.argv[1]
        school = School()
        school.read_scores(filename)
        print(school)
        filename=sys.argv[2]
        school.GenerateCoursesReport(filename)
        filename=sys.argv[3]
        school.GenerateStudentReportAtHDLevel(filename)
