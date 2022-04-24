import os
import pandas as pd
from Module.Config import HOME_PATH, MIDDLE_AREA, YEAR
from Module.Utile import makefolder, deletefolder

# Path setting #
RAW_PATH = HOME_PATH + "Data/MiddleAreaData/"
RESULT_PATH = os.path.join(HOME_PATH, "Data/MeltData/")
makefolder(RESULT_PATH)

#
# Data melt.
#
for Y in YEAR:

    for ma in MIDDLE_AREA:
        # Data load #
        ma_data = pd.read_csv(RAW_PATH + '{}_{}.txt'.format(ma, Y), delimiter="\t")

        # Extract station id information #
        stid_list = ma_data.columns[1:]

        # Add columns :: year, month, day, hour, yyyymmdd #
        y_list, m_list, d_list, h_list, date_list = [], [], [], [], []
        for d in ma_data['Date'].tolist():
            new_date = '{:10d}'.format(int(d))
            y_list.append(new_date[0:4])
            m_list.append(new_date[4:6])
            d_list.append(new_date[6:8])
            h_list.append(int(new_date[8:10]))
            date_list.append('{}'.format(new_date[0:8]))
        ma_data['Year'], ma_data['Month'], ma_data['Day'], ma_data['Hour'], ma_data['YYYYMMDD'] = y_list, m_list, d_list, h_list, date_list

        # Data melt #
        melt_df = pd.DataFrame([])
        for col in stid_list:
            melt = ma_data.melt(id_vars=['Date', 'Year', 'Month', 'Day', 'Hour', 'YYYYMMDD'], value_vars=col, var_name='STATION_ID')
            melt_df = pd.concat([melt_df, melt])
        melt_df = melt_df.reset_index(drop=True)
        melt_df.to_csv(RESULT_PATH + '{}_{}.txt'.format(ma, Y), sep="\t", index=False)
        print("China data melt :: Year={} / Area={}".format(Y, ma))

# Delete used data #
# deletefolder(RAW_PATH)