def sed(pattern,filename1,filename2):
    fin1=open(filename1)
    fin2=open(filename2,"w")
    for line in fin1:
        if pattern is line:
            line=line.replace(pattern,"blablabla")
        fin2.write(line)
    

sed("aas",'Chapter14_files/words.txt','Chapter14_files/result.txt')