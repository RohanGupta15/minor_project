#For files other than texts or NON UTF-8 encoded files we open them in Binary Mode  #
#               Line by Line reading                                                #
#####################################################################################
with open('Rohan.jpg', 'rb') as original_pic:
    with open('Rohan_copy.jpg' , 'wb') as copy_pic:
       for line in original_pic:
            copy_pic.write(line)
             
#########################################################################
#                                                                       #
#               Reading and writing with speciic block size             #
#                                                                       #
#########################################################################

with open('Rohan.jpg' , 'rb') as orginal_picture:
    with open('Rohan_copy_block.jpg' , 'wb') as copy_picture:
        block_size = 4096
        read_block = orginal_picture.read(block_size)
        while len(read_block) > 0:
            copy_picture.write(read_block)
            read_block = orginal_picture.read(block_size)