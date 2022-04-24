import os
import pandas as pd
from Module.Config import HOME_PATH, MIDDLE_AREA, YEAR, SEASON_YEAR
from Module.Utile import makefolder, deletefolder

# Path setting #
RAW_PATH = HOME_PATH + "Data/MatchData/"
RESULT_PATH = os.path.join(HOME_PATH, "Result/")
makefolder(RESULT_PATH)

#
# Make Season data.
#
for Y in SEASON_YEAR:

    for ma in MIDDLE_AREA:
        # Data load #
        s_data = pd.read_csv(RAW_PATH + "{}_{}.txt".format(ma, Y), delimiter="\t", encoding='utf-8')
        dec = s_data.loc[(s_data['Month'] == 12)].reset_index(drop=True)

        # Load data of January, February, Merch #
        s_data1 = pd.read_csv(RAW_PATH + "{}_{}.txt".format(ma, Y + 1), delimiter="\t", encoding='utf-8')
        jfm = s_data1.loc[(s_data1['Month'] == 1) | (s_data1['Month'] == 2) | (s_data1['Month'] == 3)].reset_index(drop=True)

        # Merge DEC, JFM data #
        merge = pd.concat([dec, jfm]).reset_index(drop=True)
        merge = merge.rename(columns={'LON': 'LAT', 'LAT': 'LON'})
        merge = merge.fillna('NaN')
        merge.to_csv(RESULT_PATH + "Season_{}_{}.txt".format(ma, Y), sep=',', index=False)
        print("Split season data :: Year={} / Area={}".format(Y, ma))

#
# Make unseason data.
#
for Y in YEAR:

    for ma in MIDDLE_AREA:
        # Data load #
        us_data = pd.read_csv(RAW_PATH + "{}_{}.txt".format(ma, Y), delimiter="\t", encoding='utf-8')
        an_df = us_data.loc[(us_data['Month'] >= 4) & (us_data['Month'] <= 11)].reset_index(drop=True)
        an_df = an_df.rename(columns={'LON': 'LAT', 'LAT': 'LON'})
        an_df = an_df.fillna('NaN')
        an_df.to_csv(RESULT_PATH + "Unseason_{}_{}.txt".format(ma, Y), sep=',', index=False)
        print("Split unseason data :: Year={} / Area={}".format(Y, ma))

# Delete used data #
deletefolder(RAW_PATH)