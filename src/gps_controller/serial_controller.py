import serial
import micropyGPS
import threading
import time
import datetime
from . import gps_controller

TIMEZONE_JP=9
SERIAL_PATH = '/dev/serial0'

DATA_STOCK = 20

class SerialGPSController(gps_controller.GpsController):
    def __init__(self):
        self._gps = micropyGPS.MicropyGPS(TIMEZONE_JP, 'dd')

        self.gpsthread = threading.Thread(target=self._rungps, args=()) # 上の関数を実行するスレッドを生成
        self.gpsthread.daemon = True
        self.gpsthread.start() # スレッドを起動


    def _rungps(self): # GPSモジュールを読み、GPSオブジェクトを更新する
        s = serial.Serial(SERIAL_PATH, 9600, timeout=10)
        s.readline() # 最初の1行は中途半端なデーターが読めることがあるので、捨てる
        while True:
            sentence = s.readline().decode('utf-8') # GPSデーターを読み、文字列に変換する
            if sentence[0] != '$': # 先頭が'$'でなければ捨てる
                continue
            for x in sentence: # 読んだ文字列を解析してGPSオブジェクトにデーターを追加、更新する
                self.gps.update(x)

    def is_enable_gps(self):

        return self.gps.clean_sentences > DATA_STOCK
    
    def check_vaital(self):
        pass

    def get_gps_data(self):
        dt = datetime.datetime(
            int(f'20{self.gps.date[2]:02}'),
            self.gps.date[1],
            self.gps.date[0],
            self.gps.timestamp[0],
            self.gps.timestamp[1],
            self.gps.timestamp[2])
        return (
            self.gps.latitude, # 経度
            self.gps.longitude, # 緯度
            self.gps.altitude, # 高度
            self.gps.satellites_in_use, # 即位衛星数
            self.gps.fix_type, # 1:no 2:2D 3:3D
            self.gps.hdop, # 水平精度低下率
            self.gps.vdop, # 垂直精度低下率
            self.gps.pdop, # 位置精度低下率
            dt, # 時間
            )

