# ---------------------------------------- #
# Code name : Config.py
# ---------------------------------------- #
# Developer : Jeong-Beom Lee
# Generate date : 2022-04-06
# Update date : 2022-04-24
# ---------------------------------------- #

#
# Import library.
#
import os

#
# Set path.
#
ABS_PATH = os.path.abspath(os.path.dirname("__main__"))
HOME_PATH = ABS_PATH + "../../"

#
# Variables related to the area.
#
MIDDLE_AREA = ['동북', '화북', '화동', '중남', '서북', '서남']
IMPACT_AREA = {'동북': ['랴오닝성', '지린성', '헤이룽장성'], '화북': ['베이징시', '텐진시', '허베이성', '산시성'],
               '화동': ['산둥성', '상하이시', '안후이성', '장쑤성', '저장성'], '중남': ['허난성']}

#
# Variables related to the date.
#
YEAR = [2016, 2017, 2018, 2019, 2020, 2021]
SEASON_YEAR = [2016, 2018, 2020]
UNSEASON_YEAR = [2016, 2017, 2018, 2019, 2020, 2021]