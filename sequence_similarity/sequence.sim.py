#!/usr/bin/env python3
import sys 

fields = "q_seqid s_sequid percid alen mism gaps q_start q_end s_start s_end evalue bits".split() #this defines the column names for BLAST tabular output. 
#split converts the string into a list of field names 

seq_hit_file = []

seq_hits_list = [] # initializes an empty list that will store parsed hits from all files 
# each elements will be a dictionary representing one BLAST hit 

for seq_hit_file in sys.argv[1]: #loops through all command-line arguments except the first sys.argv which is the script name! 
    #each argument should be a file path to the BLAST tabular file. 
    with open (seq_hit_file, "r") as fh: #open the current file in read mode. 
        for line in fh: #loops over each line in the file 
            line = line.strip()
            if line.startswith('#'):
                is_comment = True
            else:
                is_comment = False 
            if not is_comment:
                values = line.split('\t')


                seq_hit_data = {}
                for i in range(len(fields)):
                    seq_hit_data[fields[i]] = values[i]
                
                seq_hit_data['file'] = seq_hit_file

                seq_hits_list.append(hit_data)

                break

for seq_hit in seq_hits_list:
    print('\t'.join([hit["file"], hit["percid"], hit["alen"], hit["evalue"]]))





# for hit_filename in sys.argv[1:]:

# #     with open("hit_filename" , "r") as fh: #here I have the as to "fh" which is filen handle. 
# #         for line in fh: 
# #             for line in fh:
# #                 # remove trailing newline (handles Unix and Windows)
# #                 line = line.rstrip('\n') # continue processing with `line` (now without the newline)
# #                 print(line)
# #            # if line.rstrip('/n').startswith('#'):
             
                
# import sys

# hit_files = []

# field_str = "q_seqid s_seqid percid alen mism gaps q_start q_end s_start s_end evalue bits"
# fields=field_str.split(' ')

# hits_list = []

# for hit_file in sys.argv[1:]:

#     with open(hit_file,'r') as fin:
#         for line in fin:
#             if line[0]=='#':
#                 continue
#             hit_data = dict(zip(fields,line.strip('\n').split('\t')))
#             hit_data['file'] = hit_file
#             hits_list.append(hit_data)
#             break

# for hit in hits_list:
#     print('\t'.join([hit[x] for x in ('file','percid','alen','evalue')]))