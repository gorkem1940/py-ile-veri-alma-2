import schedule
import time
import threading
import requests
import xml.etree.ElementTree as ET

def fetch_and_save_xml():

    url = 'http://192.168.2.162/status.xml' // bu siteden veriyi al 

    headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        xml_data = response.text
        

        with open('status.xml', 'w') as f: 
            //status.xml yerine istediğimiz dosya uzantısını yazalım
            f.write(xml_data)
    else:
        print('Hata:', response.status_code)

def run_schedule():
    schedule.every(1).seconds.do(fetch_and_save_xml)
    while True:
        schedule.run_pending()
        time.sleep(1) // bir saniyede bir veriyi yenileyecektir

thread = threading.Thread(target=run_schedule)
thread.start()
