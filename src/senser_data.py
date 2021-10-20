import dataclasses
import datetime
from time import time

@dataclasses.dataclass
class SenserData(object):
    time_stamp: datetime = datetime.datetime.now()
    lon: float = 0.0 # 経度
    lat: float = 0.0# 緯度
    altitude: float = 0.0 # 高度（海抜)
    gps_count: int = 0 # GPSの数
    fix_type:int = 0 # 1:no 2:2D 3:3D
    hdop: float = 0.0 # 水平精度低下率
    vdop: float = 0.0 # 垂直精度低下率
    pdop: float = 0.0 # 位置精度低下率

    rotate_x: float = 0.0 # x軸角度
    rotate_y: float = 0.0 # y軸角度 
    rotate_z: float = 0.0 # z軸角度
    accel_x: float = 0.0 # x方向加速度
    accel_y: float = 0.0 # y方向加速度
    accel_z: float = 0.0 # z方向加速度
    
    photo_path: str =''

    def set_gps_data(self,lat,lon,altitude,gps_count,fix_type,hdop,vdop,pdop,timestamp):
        self.lat = lat
        self.lon = lon
        self.altitude = altitude
        self.gps_count = gps_count
        self.fix_type = fix_type
        self.hdop = hdop
        self.vdop = vdop
        self.pdop = pdop
        self.time_stamp = timestamp

    def set_accele_data(self,rotate_x,rotate_y,rotate_z,accel_x,accle_y,accle_z):
        self.rotate_x = rotate_x
        self.rotate_y = rotate_y
        self.rotate_z = rotate_z
        self.accel_x = accel_x
        self.accel_y = accle_y
        self.accel_z = accle_z

    def get_dict(self):
        data = dataclasses.asdict(self)
        data['time_stamp'] = data['time_stamp'].strftime('%Y-%m-%d %H:%M:%S')
        return data




    
