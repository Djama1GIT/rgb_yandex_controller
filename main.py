import json
import keyboard
import requests
import pyautogui
from tkinter import colorchooser
from time import sleep

yandex_oauth = oauth_id
yandex_lamp_id = lamp_id
head = json.loads('{"Authorization": "Bearer ' + yandex_oauth +
                  '", "Content-Type": "application/json"}')

commonly_first = "FFFFFF"  # Commonly used color (Num9)
commonly_second = "FF0000"  # Commonly used color (Num6)


def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    if color_code == (None, None):
        pyautogui.alert(text="Вы не выбрали цвет, поэтому будет установлено белое освещение", title='WARNING!', button='OK')
        return "FFFFFF"
    else:
        return color_code


def hexToInt(hex_code):
    if not hex_code:
        return "0"
    if len(hex_code) == 6 and type(hex_code) == str:
        hex_code = hex_code.upper()
        for i in hex_code:
            if not (i in "0123456789ABCDEF"):
                return "0"
        return str(int("0x" + hex_code, 0))
    else:
        return "0"


def rgbOn():
    try:
        data_json = json.loads('{"devices": [{"id": "'+yandex_lamp_id+'","actions": [{"type": '
                               '"devices.capabilities.on_off","state": {"instance": "on","value": true}}]}]}')
        requests.post("https://api.iot.yandex.net/v1.0/devices/actions", headers=head, json=data_json)
    except Exception as err:
        pyautogui.alert(text=err, title='WARNING!', button='OK')


def rgbOff():
    try:
        data_json = json.loads('{"devices": [{"id": "'+yandex_lamp_id+'","actions": [{"type": '
               '"devices.capabilities.on_off","state": {"instance": "on","value": false}}]}]}')
        requests.post("https://api.iot.yandex.net/v1.0/devices/actions", headers=head, json=data_json)
    except Exception as err:
        pyautogui.alert(text=err, title='WARNING!', button='OK')


def rgbPicker(color):
    try:
        data_json = json.loads('{"devices": [{"id": "'+yandex_lamp_id+'","actions": [{"type": '
                          '"devices.capabilities.color_setting","state": {"instance": "rgb","value": ' + color + '}}]}]}')
        requests.post("https://api.iot.yandex.net/v1.0/devices/actions", headers=head, json=data_json)
    except Exception as err:
        pyautogui.alert(text=err, title='WARNING!', button='OK')


keyboard.add_hotkey("Ctrl+7", lambda: rgbOff())
keyboard.add_hotkey("Ctrl+8", lambda: rgbOn())
keyboard.add_hotkey("Ctrl+9", lambda: rgbPicker(hexToInt(commonly_first)))
keyboard.add_hotkey("Ctrl+6", lambda: rgbPicker(hexToInt(commonly_second)))
keyboard.add_hotkey("Ctrl+5", lambda: rgbPicker(hexToInt(choose_color()[1][1:])))

while True:
    sleep(0.3)