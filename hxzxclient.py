import socket
import struct

class HXZXclient():
    def _hxzx_send(self,address):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 第二步：建立连接
            s.connect((address, 8117))  # 80port是Web服务的标准port
            # 第三步：发送数据
            data = """
            20 00 00 00 05 10 00 00 00 00 00 00 01 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            """
            data = data.replace('\n', '').replace(' ', '')
            result = b''
            data_temp = ''
            while data:
                data_temp = data[0:2]
                r = int(data_temp, 16)
                result += struct.pack('B', r)
                data = data[2:]
            s.sendall(result)
            # 第四步：关闭连接
        except Exception:
            return "ERROR_CONN"
        finally:
            try:
                s.close()
            except Exception:
                pass