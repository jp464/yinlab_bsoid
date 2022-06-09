# ===================================================================================
# SUMMARY OF CODE
# Identifies the initial and final frame of contiguous frames of the given
# label and the next transition label. The frequencies of the next transition
# label is also given.

# PROCEDURE
# Modify the FILE to be the path of the file you wish to analyze. The DEST 
# is where the result will be stored in. The frequencies of the next transition
# label will be printed. You can also change the name of the file. 
# In the terminal, change the directory to where the program is located and enter
# "python group_transition.py". 
# ===================================================================================

import pandas as pd 
import pathlib

# File and Destination path
PATH = pathlib.Path(__file__).parent.resolve()
fname = "/data/Ai14-03_68_RD200_RS35_Trainingday5_camP.csv"
FILE = str(PATH) + fname

DEST = str(PATH) + "/output" + fname[5:len(fname) - 5] + "_frame_transitions.csv"



# Read file and extract list of labels for all frames
df = pd.read_csv(FILE)
all_labels = df.iloc[2:, 1].to_list()


label = int(input("Enter label"))

initial = []
final = []
next = []

# Identify all transition frames 
check = False
for i in range(len(all_labels)):
    cur = all_labels[i]

    if (not check):
        if cur == label:
            initial.append(i)
            check = True
        
    else:
        if cur != label:
            final.append(i - 1)
            next.append(all_labels[i])
            check = False
        
        if i == len(all_labels) - 1:
            final.append(i)
            next.append(all_labels[i])


# Create data frame of initial and final frames of label, and next label
d = {'initial': initial, 'final': final, 'next_label' : next}
df = pd.DataFrame(data=d)

df_initial = df[["initial", "next_label"]]
df_intervals = df.loc[df["final"] - df["initial"] > 0]

df.to_csv(DEST)


# Calculate frequencies of next labels 
freq = df["next_label"].value_counts(normalize = True)
print(freq)



