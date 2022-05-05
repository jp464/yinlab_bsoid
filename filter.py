# ===================================================================================
# SUMMARY OF CODE
# Filters for given next transition label 

# PROCEDURE
# Modify the FILE to be the path of the file you wish to analyze. The DEST 
# is where the result will be stored in. You can also change the name of the file. 
# In the terminal, change the directory to where the program is located and enter
# "python filter.py". 
# ===================================================================================

import pandas as pd 

FILE = "/Users/stan.park712/Library/CloudStorage/Box-Box/jp464/yinLab/yinlab_bsoid/test_data/frame_transitions.csv"
DEST = "/Users/stan.park712/Library/CloudStorage/Box-Box/jp464/yinLab/yinlab_bsoid/test_data"
DEST += "/filtered_frame_transitions.csv"
df = pd.read_csv(FILE)

label = input("Enter label to filter for").split(" ")
label = list(map(lambda x: int(x), label))

df = df[df["next_label"].isin(label)]
df.to_csv(DEST)
