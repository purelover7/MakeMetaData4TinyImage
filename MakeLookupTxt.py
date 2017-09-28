import os

def make_lookup(dirname, write_file):
    filenames = os.listdir(dirname)
    index = 0

    lookup = dict()

    with open(write_file, 'w') as wf:
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            print_line =  '{}\t{}\n'.format(filename, index)
            print(print_line)
            wf.write(print_line)
            lookup[filename] = index
            index = index + 1

    return lookup


## dir_search("E:/Project/TinyImageNet/Data/tiny-imagenet-200/train",
##           "E:/Project/TinyImageNet/Data/lookup.txt")
