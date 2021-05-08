# Student Name, Student Roll no, Subject Names, Subject Credits, Subject Marks Secure, sgpa
class StudentExam:
    subName=["FPP","FLAT","DAA","CN","COA","EEC"]
    subCredit=[3,4,4,3,3,3]
    def getData(self):
        self.snam=input("Enter the Name of the Student : ")
        self.srollno=input("Enter the Roll No : ")
        self.marks=[]
        for i in range(0,6,1):
            mark=int(input("Enter the Marks for {} :".format(self.subName[i])))
            self.marks.append(mark)
    def tableDesign(self):
        print("Subject Name\t",end="")
        print(*self.subName,sep='\t',end="\n")
        print("Credit \t\t",end="")
        print(*self.subCredit,sep='\t',end="\n")
    def display(self):
        self.SGPA()
        print(self.srollno,end="\t")
        print(*self.marks,sep='\t',end="\t")
        print(self.sgpa,end="\n")
    def SGPA(self):
        self.grade=[]
        self.gradem=[]
        sumCredit=0
        sumCreditAcc=0
        for i in range(0,6,1):
            mark=self.marks[i]
            if mark >=90:
                grade='O'
                gradem=10
            elif mark >= 80:
                grade='E'
                gradem=9
            elif mark >= 70:
                grade='A'
                gradem=8
            elif mark >= 60:
                grade='B'
                gradem=7
            elif mark >= 50:
                grade='C'
                gradem=6
            elif mark >= 40:
                grade='D'
                gradem=5
            else:
                grade='F'
                gradem=2
            self.grade.append(grade)
            self.gradem.append(gradem)
            sumCredit= sumCredit+self.subCredit[i]
            sumCreditAcc=sumCreditAcc+self.subCredit[i]*gradem
        self.sgpa=(float)(sumCreditAcc/sumCredit)
    def findTopper(lst):
        top=lst[0]
        for std in lst:
            if(std.self.sgpa>top.self.sgpa):
                top=std
        
        return top
    
students=[]
n=int(input("Enter the Number of Student"))
for i in range(0,n):
    s=StudentExam()
    s.getData()
    students.append(s)
students[0].tableDesign()
for student in students:
    student.display()
n=StudentExam()
n


    
