# 地理関連処理

import math

POLE_RADIUS = 6356752.314245                  # 極半径
EQUATOR_RADIUS = 6378137.0                    # 赤道半径


def cal_distance(latlon1:tuple,latlon2:tuple) -> float:
    # https://www.gis-py.com/entry/py-latlon2distance


    # 緯度経度をラジアンに変換
    lat_kamata = math.radians(latlon1[0])
    lon_kamata = math.radians(latlon1[1])
    lat_yokosukachuo = math.radians(latlon2[0])
    lon_yokosukachuo = math.radians(latlon2[1])

    lat_difference = lat_kamata - lat_yokosukachuo       # 緯度差
    lon_difference = lon_kamata - lon_yokosukachuo       # 経度差
    lat_average = (lat_kamata + lat_yokosukachuo) / 2    # 平均緯度

    e2 = (math.pow(EQUATOR_RADIUS, 2) - math.pow(POLE_RADIUS, 2)) \
            / math.pow(EQUATOR_RADIUS, 2)  # 第一離心率^2

    w = math.sqrt(1- e2 * math.pow(math.sin(lat_average), 2))

    m = EQUATOR_RADIUS * (1 - e2) / math.pow(w, 3) # 子午線曲率半径

    n = EQUATOR_RADIUS / w                         # 卯酉線曲半径

    distance = math.sqrt(math.pow(m * lat_difference, 2) \
                   + math.pow(n * lon_difference * math.cos(lat_average), 2)) # 距離計測

    return distance