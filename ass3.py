'''
3. Create a file and insert the records in the following format(Read the records from the user)
SNo Name   Game
1   ram  Cricket
2.  ramu  kabaddi
3.  rao   hockey
'''
file = open('SampleRecord.txt','w')
table = ['SNo\t','Name\t','Game']
file.writelines(table)
file.write('\n')
rows = int(input('Enter the rows to insert in a file:'))
for i in range(rows):
    file.writelines([input(),'\t',input(),'\t',input()])
    file.write('\n')
file.close()
file1 = open('SampleRecord.txt','r')
data = file1.read()
print('Contents after Inserting in a file is')
print(data)
file1.close()
'''
Input:
Enter the rows to insert in a file:3
1. 
ram
cricket
2.
ramu
kabaddi
3.
rao
hockey
Contents after Inserting in a file is
SNo	Name	Game
1. 	ram	  cricket
2.	ramu	kabaddi
3.	rao	  hockey
