import os
import MakeLookupTxt

def make_train(root_dir, write_file, lookup):
    ## 해당 OS에 맞게 정규화를 한다.
    root_dir = os.path.normcase(root_dir);

    dirnames = os.scandir(root_dir)

    save_str = ''

    for dirname in dirnames:
        if os.path.isdir(dirname) :
            # case dir:
            make_train(dirname.path, write_file, lookup)
        else :
            ## case file:
            if( dirname.name.find(".JPEG") == -1) :
                continue
            else :
                # file save
                found = dirname.path.find("train")
                filename = dirname.path[found:]
                filename = os.path.normcase(filename);

                found = dirname.name.find("_")
                ctype = dirname.name[:found]

                itype = lookup[ctype]

                save_str +=  '{}\t{}\n'.format(filename, itype)
                ## print_line = '{} {}\n'.format(dirname.name, root_path)
    with open(write_file, 'a') as wf:
        wf.write(save_str)

lookup = MakeLookupTxt.make_lookup(
    "E:/Project/TinyImageNet/Data/tiny-imagenet-200/train",
    "E:/Project/TinyImageNet/Data/lookup.txt"
)

make_train(
    "E:/Project/TinyImageNet/Data/tiny-imagenet-200/train",
    "E:/Project/TinyImageNet/Data/train.txt",
    lookup
)
