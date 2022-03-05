# RGB Yandex Controller #
### libs:
* json
* keyboard
* requests
* pyautogui
* tkinter
* time

### functions main.py
* choose_color - open the color picker, returns hex color code
* hexToInt - changes hex code to int
* rgbOn - turns on the lamp
* rgbOff - turns off the lamp
* rgbPicker - a color is sent to the input in the int format; the color of the lamp switches to sent

## For the script to work
* I. Enter the lamp id in "yandex_lamp_id" // go to https://oauth.yandex.ru and rigister & select your device; copy ID and paste here 
* II. Enter the OAuth-code in "yandex_oauth" // go to https://oauth.yandex.ru/authorize?response_type=token&client_id={yandex_lamp_id} (without {})
