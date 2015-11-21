"""This module provides an implementation of the Sorting Abstract Data Type along with File Reading.

Title: Lab 4, Sorting Records

CSCI 241, March 3, 2015

Author: Nadia Aly (naaly)

This lab implements a "Student File Reader ADT" as described in our textbook along with sorting algorithms adt. Python

provides a 'sort()' method to sort a list, but it cannot be used with other data structures. This lab uses the bubble

sort algorithm to sort student records. The program takes an input file which contains a userID and a numerical grade

(one on each line) and is asked to sort each file by UserID and grade. The userID is taken as the sorting key and each

student record is the list is sorted in alphabetical order and output to a text file. The grade is taken as the sorting

key in the second sort and a letter grade is assigned, and the grades are sorted in descending order using bubble sort

algorithm, the sorted list is then written to the same text file as the student record's sorted by UserID.

"""

import numpy as np

File_Name= "rawgrade.txt"
#The input-file with student ID and number grade is rawgrade.txt

def main():
    """ The main function that calls the functions; recordRead, studentIDSort, and gradeSort. Record Read, named

    'recordRead' has its own global function returning unsorted record sequence. studentIDSort  has its own global

    function taking the (unsorted) records as input. gradeSort, has its own global function taking the sorted

    records as input.
    """
    rawGrade=open("rawgrade.txt",'r')
    #Open a connection to input file, read only
    studentList=recordRead(rawGrade)
    #Extract all student records and read to list
    rawGrade.close()
    #Close connection to input file
    procGrade = open("procGrade.txt",'w')
    #Open a connection to output file,ability to write
    studentIDSort(studentList)
    #Calls function to sort student record by userID
    writeIDSort(studentList,procGrade)
    #Write student record sorted by userID and the student record sorted by grade
    gradeSort(studentList)
    #Calls function to sort student record by grade
    writeGradeSort(studentList, procGrade)
    #Calls function to write the sorted lists to output file
    procGrade.close()
    #close connection to output file



class StudentRecord:
    """Define storage class such that each student record will be an object of this class (used for an individual

    student record.
    """
    def __init__(self, studentID, grade):
        """Create instance for storage class, each individual student record has userID, grade, letter (letter of

        numerical grade), and calls assign to take the grade and return letter.
        """
        self.userID= studentID
        self.grade=grade
        self.letter=None
        self.letter = assign(grade)

    def __str__(self):
        """Format output
        """
        self.spacesName = 8 - int(len(str(self.userID)))
        self.spacesGrade = 8 - int(len(str(self.grade)))
        return "" + self.userID + " "*self.spacesName + str(self.grade) + " "*self.spacesGrade + str(self.letter)


def assign(grade):
    """
    Assign could be used strictly for the grade portion of the record, or as in this case implemented indirectly as part

    of the record. As such, assign(grade) is not part of the StudentRecord Class so could theoretically be called just

    for the sort/writeGrade portion, rather than be an integral attribute of each processed line of a StudentRecord.

    Each student record is assigned a grade, and that grade is part of its printing (whether sorted or not). Assigns

    letter of: A,B, C, D or F to each grade interval, returns that letter.

    Argument:

        grade--Number grade from StudentRecord, returns letter Grade as char
     """
    if grade >= 90:
        letter = 'A'
    elif 80 <= grade and grade < 90:
        letter = 'B'
    elif 70 <= grade and grade < 80:
        letter = 'C'
    elif 60 <= grade and grade < 70:
        letter = 'D'
    else :
        letter = 'F'

    return letter



def recordRead(file):
    """Reads each line in file, index such that a list is created such that for each line, student ID will be referenced

    with the student's grade and they will not get mixed up. The first item is the student ID and second item is the

    grade. Take type integer for the grade. Read through each line in the file and append this to recordList for each

    ID/grade.
    """
    recordList = list()
    for line in file:
        line=line.split()
        if len(line)>1:
            rec = StudentRecord(line[0], int(line[1]))
            StudentRecord.userID = line[0]
            StudentRecord.grade = int(line[1])
            recordList.append(rec)
    return recordList



def studentIDSort(studentList):
    """
    Sorts the StudentRecord list by the StudentID (alphabetical order), via 'bubble sort' sorting algorithm. The bubble

    sort sorting algorithm makes multiple passes through a list and compares adjacent items and swaps those that are

    out of order.  Each pass through the list "bubbles" the next largest value in its proper place until all items are

    in the correct order.

    Argument:

        studentList-- unsorted StudentRecord list
    """
    sort = False
    n=len(studentList)
    while not sort:
        sort = True
        for i in range(0,n-1):
            if studentList[i].userID >studentList[i+1].userID:
                sort = False
                temp = studentList[i]
                studentList[i] = studentList[i+1]
                studentList[i+1]=temp


def gradeSort(studentList):
    """
    Sorts the StudentRecord list by the grade (number, not letter) via bubble sort. The bubble sort sorting algorithm

    methodology explained in previous function.

    Argument:

        studentList-- Unsorted StudentRecord list
    """
    sort = False
    n=len(studentList)
    while not sort:
        sort = True
        for i in range(0,n-1):
            if studentList[i].grade <studentList[i+1].grade:
                sort = False
                temp = studentList[i]
                studentList[i] = studentList[i+1]
                studentList[i+1]=temp



def writeIDSort(studentList,procGrade):
    """
    Writes each record as sorted by the studentID (formats with *** boarder).

    Argument:

        studentList-- sorted StudentRecords

        procGrade--output file
    """
    output = procGrade
    output.write("*********************************" + '\n' + "Sorted by StudentID" + '\n' "********************************" + '\n')
    for i in range (0, len(studentList)):
        output.write(str(studentList[i]) + '\n')

def writeGradeSort(studentList,procGrade):
    """
    writeGradeSort is only differentiated from WriteIDSort by the "sorted by" line in the header.  (formats with

    *** boarder)

    Arguments:

    studentList--sorted studentRecords

    procGrade--output text File we send formatted/sorted record to

    """
    output = procGrade
    output.write("**********************************" + '\n' + "Sorted by Grade" +'\n' + "**********************************" + '\n')
    for i in range (0, len(studentList)):
        output.write(str(studentList[i]) + '\n')






main()



