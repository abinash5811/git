#Class and sections - [[1A,1B,1C],[2A,2B,2C],[3A,3B,3C],[4A,4B,4C]]
class_size = [[25, 30, 28],
              [20, 22, 25],
              [27, 24, 26],
              [18, 20, 22]]
# Help the adminstration find following information:

# Number of students in class- 1A
# Number of students in class- 3B
# Number of students in class- 4C
# Total number of students of all sections in each class- 1 and Class- 4: 1(A,B,C) +4 (A,B,C)
 
# Number of students in class- 1A 
s_in_1a=class_size[0][0]
print("the number of students in class-1A=",s_in_1a)

# Number of students in class- 3B
s_in_3b=class_size[2][1]
print("the number of students in class-1A=",s_in_3b)

# Number of students in class- 4C
s_in_4c=class_size[3][2]
print("the number of students in class-1A=",s_in_4c)

# Total number of students of all sections in each class- 1 and Class- 4: 1(A,B,C) +4 (A,B,C)
total_std_in_cls1_cls4=sum(class_size[0])+sum(class_size[3])
print("the total students in class 1&4 are=",total_std_in_cls1_cls4)

classs=[]
classs.append(s_in_1a)
classs.append(s_in_3b)
classs.append(s_in_4c)
print(classs)
# classs.sort()
# print(classs)
classs.sort()
print(classs)






             