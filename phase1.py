import os

def main():
    file_names =['reviews.txt','scores.txt','pterms.txt','rterms.txt']
    idx_names =['rw.idx','sc.idx','pt.idx','rt.idx']
    structures =['hash','btree','btree','btree']
    for i in range(len(file_names)):
        structure = structures[i]
        if structure == 'btree':
            add = "-c duplicates=1"
        elif structure == 'hash':
            add = ""
        os.system("sort -u %s -o %s"%(file_names[i],file_names[i]))
        os.system("perl break.pl < %s | db_load -T -t %s %s %s"\
                  %(file_names[i],structure,add,idx_names[i]))

main()
