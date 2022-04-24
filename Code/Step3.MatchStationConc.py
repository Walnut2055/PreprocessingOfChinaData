import os
import pandas as pd
from Module.Config import HOME_PATH, MIDDLE_AREA, YEAR
from Module.Utile import makefolder, deletefolder

# Path setting #
RAW_PATH = HOME_PATH + "Data/MeltData/"
STATION_PATH = os.path.join(HOME_PATH, "Data/Station/")
RESULT_PATH = os.path.join(HOME_PATH, "Data/MatchData/")
makefolder(RESULT_PATH)

# Station data load #
ST_df = pd.read_csv(STATION_PATH + "RemakeStation.txt", delimiter="\t")
ST_df = ST_df.drop(columns=['NATION', 'Area1', 'Area2'])

#
# Concentration data and station data are matched.
#
for Y in YEAR:

    for ma in MIDDLE_AREA:
        # Conc data load #
        conc_df = pd.read_csv(RAW_PATH + "{}_{}.txt".format(ma, Y), delimiter="\t", low_memory=False)

        # Match (Using merge method) #
        merge = pd.merge(conc_df, ST_df, on='STATION_ID')

        # Columns relocation #
        merge = merge[['Date', 'Year', 'Month', 'Day', 'Hour', 'YYYYMMDD', 'STATION_ID', '권역', '중권역', '소권역', '세부권역', 'LON', 'LAT', 'X', 'Y', 'NIER_group', 'value']]

        # Saved data #
        merge.to_csv(RESULT_PATH + "{}_{}.txt".format(ma, Y), sep="\t", index=False)

# Delete used data #
# deletefolder(RAW_PATH)