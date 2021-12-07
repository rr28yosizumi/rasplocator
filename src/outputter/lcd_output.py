from . import outputter

import smbus
import time

# I2C通信の設定
I2C_ADDR  = 0x27 # I2Cアドレス
LCD_WIDTH = 16   # 表示文字数の上限
LCD_CHR = 1 # 文字列送信モードの識別子
LCD_CMD = 0 # コマンド送信モードの識別子
LCD_LINE_1 = 0x80 # 一行目に表示する文字列の書き込み先
LCD_LINE_2 = 0xC0 # 二行目に表示する文字列の書き込み先
LCD_BACKLIGHT  = 0x08  # バックライトをOFFにするコマンド

bus = smbus.SMBus(1) # 接続されているバスの番号を指定

def init_display():
  send_byte_to_data_pin(0x33,LCD_CMD)
  send_byte_to_data_pin(0x32,LCD_CMD)
  send_byte_to_data_pin(0x06,LCD_CMD)
  send_byte_to_data_pin(0x0C,LCD_CMD)
  send_byte_to_data_pin(0x28,LCD_CMD)
  send_byte_to_data_pin(0x01,LCD_CMD)
  time.sleep(0.0005)
  
def send_byte_to_data_pin(bits, mode):
  upper_bits = mode | (bits & 0xF0) | LCD_BACKLIGHT
  lower_bits = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT
  bus.write_byte(I2C_ADDR, upper_bits)
  enable_toggle_button(upper_bits)
  bus.write_byte(I2C_ADDR, lower_bits)
  enable_toggle_button(lower_bits)

def enable_toggle_button(bits):
  time.sleep(0.0005)
  bus.write_byte(I2C_ADDR, (bits | 0b00000100))
  time.sleep(0.0005)
  bus.write_byte(I2C_ADDR,(bits & ~0b00000100))
  time.sleep(0.0005)

def send_string_to_display(message,line):
  message = message.ljust(LCD_WIDTH," ")
  send_byte_to_data_pin(line, LCD_CMD)
  for i in range(LCD_WIDTH):
    send_byte_to_data_pin(ord(message[i]),LCD_CHR)

class CsvOutputter(outputter.OutPut):
    def __init__(self):
        # LCDのメモリ初期化
        init_display()

    def put_data(self,data):
        init_display()
        send_string_to_display(f'lat:{data["lat"]},lon{data["lat"]}' , LCD_LINE_1) # 一行目
        send_string_to_display(f"co2:", LCD_LINE_2) # 二行目

    def finish(self):
        pass
