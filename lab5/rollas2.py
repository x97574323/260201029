students=int(input("Pls input the number of students:"))
avg=list()
while students>0:
  grade1=float(input("Pls input grade 1:"))
  grade2=float(input("Pls input grade 2:"))
  grade3=float(input("Pls input grade 3:"))
  avg_note=(grade1*30+grade2*30+grade3*40)/100
  avg.append(avg_note)
  students=students-1
for  i in avg:
  print("avg grade of {}. student is {} ".format(avg.index(i)+1,i))


#seconde example for aa students

aa_students=list()
for k in avg:
  if k>=90:
    aa_students.append(k)