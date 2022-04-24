import os
import pandas as pd
from Module.Config import HOME_PATH, YEAR
from Module.Util import makefolder, makedate

# Path setting #
RAW_PATH = HOME_PATH + "Data/RawData/"
RESULT_PATH = os.path.join(HOME_PATH, "Data/MiddleAreaData/")
makefolder(RESULT_PATH)

#
# Data preprocessing.
#
for Y in YEAR:
    # Data load #
    CN_DATA = pd.read_csv(RAW_PATH + "CHINA_PM2P5_YEAR_DATA_{}.txt".format(Y), sep="\|", header=[0, 5], encoding='utf-8', engine='python')

    # Unnecessary index is deleted #
    CN_DATA.drop([0, 1, 2, 3], inplace=True)
    CN_DATA = CN_DATA.reset_index(drop=True)
    print(len(CN_DATA))

    # Date information is saved to list #
    DATE_LIST = []
    DATE = CN_DATA['대권역'].values
    for i in range(len(DATE)):
        d = int(str(int(DATE[i]))[0:10])
        DATE_LIST.append(d)

    # YYYYMMDDHH is reformatted from YYYYMMDDHH00 #
    RE_DATE = makedate(DATE_LIST[0]-1, DATE_LIST[-1]-1)

    # The list is composed of the date that does not exist #
    EXI_DATE = []
    for i in RE_DATE:
        if i in DATE_LIST: pass
        else: EXI_DATE.append(i)

    # Middle area data is split #
    MID_AREA = list(set(CN_DATA.columns.get_level_values(0)))
    for ma in MID_AREA:
        if ma == '대권역': pass
        else:
            area = CN_DATA[ma].copy()
            area['Date'] = DATE_LIST
            col_loc = ['Date'] + area.columns[:-1].tolist()
            area = area[col_loc]

            # Unnecessary station delete #
            drop_st = []
            for id in area.columns.tolist():
                null_num = area[id].isnull().sum()
                unique_val = area[id].nunique()
                if null_num != len(area):
                    if unique_val <= 2:
                        drop_st.append(id)
                    else:
                        pass
                    pass
                else:
                    drop_st.append(id)
            area = area.drop(columns=drop_st).copy()

            # Insert list of date that does not exist #
            ins_date = pd.DataFrame(columns=area.columns)
            ins_date['Date'] = EXI_DATE
            area = pd.concat([area, ins_date]).reset_index(drop=True).copy()
            area = area.sort_values(by=['Date'], axis=0, ascending=True)
            print("Drop station number :: Year={} / Area={} / DropNumber={} / Len={}".format(Y, ma, len(drop_st), len(area)))

            area.to_csv(RESULT_PATH + "{}_{}.txt".format(ma, Y), sep='\t', index=False)