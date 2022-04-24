import os
import sys
import pandas as pd
from Module.Config import HOME_PATH, IMPACT_AREA

# Path setting #
DATA_PATH = HOME_PATH + "Data/Station/"
RESULT_PATH = HOME_PATH + "Data/Station/"

# Data load #
ST_DATA = pd.read_csv(DATA_PATH + "ChinaStation.txt", delimiter="\t")

# Make a list #
BA, MA = ST_DATA['권역'].tolist(), ST_DATA['중권역'].tolist()

#
# Impact areas are marked 'Y'. Useless areas are marked 'N'.
#
LABEL = []
for i in range(len(BA)):
    if BA[i] in IMPACT_AREA.keys():
        if MA[i] in IMPACT_AREA[BA[i]]: LABEL.append('Y')
        else: LABEL.append('N')
    else: LABEL.append('N')
ST_DATA['NIER_group'] = LABEL

#
# File of Remake station is saved.
#
ST_DATA.to_csv(RESULT_PATH + "RemakeStation.txt", sep="\t", index=False)
print("Station file is remake.")