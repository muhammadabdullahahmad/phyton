new_file =open('new _file.txt',"x") 
new_file.close()
import os
print("checking if my file exist or not")
if os.path.exists("my_file.txt"):
  os.remove("my_fil.txt")
else:
 print("the file does not exists")
 my_file = open("my_file.txt","w")
 my_file.write("hi iam abd")
 my_file.close