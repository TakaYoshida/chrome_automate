from selenium.webdriver.chrome import service as fs
from selenium import webdriver
import csv
import screeninfo

MONITOR_WIDTH, MONITOR_HEIGHT = 0, 0
path_driver = r'C:\Users\takashi\PycharmProjects\chrome_automate\driver\chromedriver.exe'
path_addressCSV = r'C:\Users\takashi\PycharmProjects\chrome_automate\address.csv'

# ウインドウサイズを取得する
for m in screeninfo.get_monitors():
    MONITOR_WIDTH = m.width
    MONITOR_HEIGHT = m.height

address = []
with open(path_addressCSV, encoding='utf-8-sig', newline='') as f:  # utf-8-sigにしとかないと\ufeffが読み込まれる
    csvreader = csv.reader(f)
    # header = next(csvreader)
    for row in csvreader:
        # print(row)
        address = row

chrome_service = fs.Service(executable_path=path_driver)
browser = webdriver.Chrome(service=chrome_service)
browser.get(address[0])
# browser.execute_script('window.open()')
# browser.switch_to.window(browser.window_handles[1])
# browser.get(address[1])
browser.set_window_size(MONITOR_WIDTH // 2, MONITOR_HEIGHT)  # ウインドウサイズを画面半分にする
browser.set_window_position(MONITOR_WIDTH // 2, 0)  # 画面右半分にブラウザ表示
