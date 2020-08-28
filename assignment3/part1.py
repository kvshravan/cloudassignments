import math
def course_reg(args):
    file1 = open(args, 'r')
    Lines = file1.readlines()
    file1.close()
    roll_no = input('Enter Roll No: ')
    name = input('Enter Name: ')
    curr_sem = int(input('Enter Current Semester: '))
    year = math.ceil(curr_sem/2);
    year = str(year)
    eligibleDict = {}
    for line in Lines:
      if line[0] == roll_no[0] and line[2]==year:
        line_split = line.strip().split('\t')
        eligibleDict[line_split[0]] = line_split[1]
    course_count = int(input('Enter number of courses you wanna take (Min.3, Max.4): '))
    while course_count !=3 and course_count!=4:
      print('Error , choose min 3. and max 4.')
      course_count = int(input('Enter number of courses you wanna take (Min.3, Max.4): '))
    print('Choose any ' +str(course_count)+' courses from the following: ')
    for key in eligibleDict:
      print(key,'\t',eligibleDict[key])
    file2 = open('studentcourseinfo','w+')
    while course_count:
      x = input('Enter course code : ')
      if x in eligibleDict:
        file2.write(x+'\t'+eligibleDict[x]+'\t'+name+'\t'+roll_no+'\t'+str(curr_sem)+'\n')
        course_count = course_count -1
      else:
        print('Enter valid course code')
    file2.close()
    print('Successfully written')
