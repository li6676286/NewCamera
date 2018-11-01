import socket
import requests

def get_address():
    try:
        r = requests.get('http://192.168.6.174:8000/cgi-bin/get.cgi', params={'random': '0.8330624071278193','key':'network_httppost'},timeout=1)
        j = r.json()
        return j['network_httppost']['httppost_serverinfo']
    except Exception:
        return None

def change_ip():
    ip=socket.gethostbyname(socket.gethostname())
    address = ip+':8000/hxzx'
    requests.post('http://192.168.6.174:8000/cgi-bin/set.cgi', data={'key': 'network_httppost',
    'httppost_enable':'1','httppost_parkid':'0','httppost_serverinfo':address,
     'httppost_maxsend':'3','httppost_workmode':'1','httppost_autoalarmouten':'0','httppost_snap_full':'0',
      'httppost_snap_closeup': '0','httppost_backenable':'0','httppost_backip':'0.0.0.0',
       'httppost_ncsend':'0','httppost_heartinterval': '10' },timeout=1)

def restore_ip(address):
    requests.post('http://192.168.6.174:8000/cgi-bin/set.cgi', data={'key': 'network_httppost',
                                                                     'httppost_enable': '1', 'httppost_parkid': '0',
                                                                     'httppost_serverinfo': address,
                                                                     'httppost_maxsend': '3', 'httppost_workmode': '1',
                                                                     'httppost_autoalarmouten': '0',
                                                                     'httppost_snap_full': '0',
                                                                     'httppost_snap_closeup': '0',
                                                                     'httppost_backenable': '0',
                                                                     'httppost_backip': '0.0.0.0',
                                                                     'httppost_ncsend': '0',
                                                                     'httppost_heartinterval': '10'},timeout=1)

