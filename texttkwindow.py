import re
from tkinter import *

from testt.change_serverip import change_ip, restore_ip, get_address
from testt.httpsever import HttpServer
from testt.hxzxclient import HXZXclient
from testt.zsclient import ZSMix


class TKwindow:

    def _http_callback(self,message):
        root_pattern = 'car_plate=([\s\S]*?)&car_logo'
        result = re.findall(root_pattern, str(message))
        if '牌' in result[0]:
            self.t.delete('1.0', 'end')
            self.t.insert('insert', '此摄像机为华夏智信摄像机,已经适配,此次检测未检测到车辆')
            restore_ip(address=self.address)
        else:
            self.t.delete('1.0', 'end')
            self.t.insert('insert', '此摄像机为华夏智信摄像机,已经适配,此次检测捕捉到的车牌号为'+result[0])
            restore_ip(address=self.address)

    def rtnkey(self,event=None):
        var = self.e1.get()
        if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                    var):
            self.address = get_address()
            try:
                if self.address == None:
                    d = ZSMix()._zs_send(var)
                    if 'E' in d:
                        self.t.delete('1.0', 'end')
                        self.t.insert('insert', '你输入的ip没有匹配到任何摄像机')
                    elif int(d[0]) > 0:
                        self.t.delete('1.0', 'end')
                        self.t.insert('insert', '此摄像机已适配臻识科技并且已经加密')
                    else:
                        self.t.delete('1.0', 'end')
                        self.t.insert('insert', '此摄像机已适配臻识科技,但并没有加密')
                else:
                    change_ip()
                    hc = HXZXclient()
                    b = hc._hxzx_send(var)
                    if 'E' in b:
                        self.t.delete('1.0', 'end')
                        self.t.insert('insert', '你输入的ip没有匹配到任何摄像机')
            except Exception:
                pass
        else :
            self.t.delete('1.0', 'end')
            self.t.insert('insert', '你输入的不是ip地址,请重新输入')




    def main(self):
        hs = HttpServer()
        hs.run_daemon(self._http_callback)
        root = Tk()
        root.title('摄像头检测工具')
        root.geometry('600x400')
        lable = Label(root,text = '此工具为摄像头检测工具,输入ip后会自动识别摄像头是否已经适配和加密\n\n'
                              '请在下方输入所要检测的ip:'
                  ,height=6,width =100)
        lable.config(font=('times','12','bold'))
        self.e1 = StringVar()
        e = Entry( root,validate='key', textvariable=self.e1, width=50 )
        w = Button (root, text ="检测",padx=10,cursor='gumby',bd=8,relief=RAISED,command =self.rtnkey)
        w.config(font=('Helvetica','13','bold'),bg='#00E3E3',activebackground="blue")
        self.t=Text(root,height=5)     #这里设置文本框高，可以容纳两行
        lable.pack()
        e.pack()
        w.pack()
        self.t.pack()

        root = mainloop()


def run():
    tt = TKwindow()
    tt.main()
