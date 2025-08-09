with open('condingal.txt','w') as file:
    file.write("hi my name is abd")
    file.close()
with open('condingal.txt','r') as file:
    data = file.readlines()
    print ("words in this file are...")
    for line in data:
        word = line.split()
        print (word)
        file.close()