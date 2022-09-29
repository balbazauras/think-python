from stringprep import in_table_c21_c22


def sed(pattern,filename1,filename2):
    fin1=open(filename1)
    fin2=open(filename2,"w")
    for line in fin1:
        if pattern in line:
            line=line.replace(pattern,"blablabla")

        fin2.write(line)
    

sed("aah",'Chapter14_files/words.txt','Chapter14_files/result.txt')