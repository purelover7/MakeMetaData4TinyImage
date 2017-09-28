import os
import MakeLookupTxt

def make_val(annotation_path, write_file, lookup):
    ## 해당 OS에 맞게 정규화를 한다.
    annotation_path = os.path.normcase(annotation_path);

    if( not os.path.exists(annotation_path) ):
        return;

    save_str = ''

    with open(annotation_path, 'r') as rf:
        while True:
            line = rf.readline()
            if not line: break
            split_str = line.split("\t")

            filename = os.path.join("val/images/", split_str[0])
            filename = os.path.normcase(filename);

            ctype =  split_str[1]
            itype = lookup[ctype]

            save_str += '{}\t{}\n'.format(filename, itype)
            print(line)

    with open(write_file, 'a') as wf:
        wf.write(save_str)

lookup = MakeLookupTxt.make_lookup(
    "E:/Project/TinyImageNet/Data/tiny-imagenet-200/train",
    "E:/Project/TinyImageNet/Data/lookup.txt"
)

make_val(
    "E:/Project/TinyImageNet/Data/tiny-imagenet-200/val/val_annotations.txt",
    "E:/Project/TinyImageNet/Data/val.txt",
    lookup
)
