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
import pathlib

# File and Destination path
PATH = pathlib.Path(__file__).parent.resolve()
fname = "/output/Ai14-03_68_RD200_RS35_Trainingday5_cam_frame_transitions.csv"
FILE = str(PATH) + fname
DEST = str(PATH) + "/output/" + "filtered_frame_transitions.csv"

df = pd.read_csv(FILE)

label = input("Enter label to filter for").split(" ")
label = list(map(lambda x: int(x), label))

df = df[df["next_label"].isin(label)]
df.to_csv(DEST)
