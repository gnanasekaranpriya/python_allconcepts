# File Objects 
#A file descriptor leak happens when your program opens files (or sockets, or pipes) but never closes them — 
# so the OS thinks they’re still “in use,” even though your program is done with them.

#f = open(r'C:\Users\vgpsa\Python Projects\Data Analyst\Data Collection\Read&Write Files\test.txt', 'r')

#print(f.mode)

#f.close()

# context manager - so with open automatically closes the file after exiting the block of code

with open('test.txt', 'r') as f: 
    for line in f:
        print(line, end='')


#f.seek(0) goes back to the first line 

#with open('test2.txt', 'w') as f: 
#    f.write("Text2")

# read from file and then write to it 
with open('test.txt', 'r') as rf: 
    with open('test_copy.txt', 'w') as wf: 
        for line in rf: 
            wf.write(line)

# read from file and then write to it - choosing chuck of the file 

with open('test.txt', 'r') as rf: 
    with open('test_copy.txt', 'w') as wf: 
        for line in rf: 
            wf.write(line)