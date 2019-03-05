#Simple file handling by Copying one file to another
with open('sample.txt', 'r') as rf:
    with open('sample_copy.txt', 'w') as wf:
        for line in rf:   #Can be used to itterate over one line at a time
            wf.write(line) # .wrtie to write a new file. if exits it overwrite the current file is not then creates one

