from re import A
import string

file_name="Chapter13_case/test.txt"
def strip_file(file_name):
    stripped_text=list()
    fin=open(file_name)
    for line in fin:
        word=line.strip()
        new_string = word.translate(str.maketrans('', '', string.punctuation)) #remove all charakters found in string.punctuation
        new_string=new_string.replace(" ","") #remove whitespaces inbetween text
        stripped_text.append(new_string) # add text to list
    return stripped_text


print(str(strip_file(file_name)))