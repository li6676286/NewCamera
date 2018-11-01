import json
import re
import socket
import struct


class ZSMix():
    def _zs_send(self, address):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((address, 8131))
            data={"cmd":"get_ems"}
            data = json.dumps(data)
            length = len(data)
            header = ['V', 'Z', 0, 0, 0, 0, 0, 0]
            header[4] += ((length >> 24) & 0xFF)
            header[5] += ((length >> 16) & 0xFF)
            header[6] += ((length >> 8) & 0xFF)
            header[7] += (length & 0xFF)
            f = '!ssBBBBBB%ds' % length
            _msg = struct.pack(
                f, "V".encode(), "Z".encode(), 0, 0, header[4],
                header[5], header[6], header[7], data.encode()
            )
            s.sendall(_msg)
            buffer = []
            while True:
                d = s.recv(1024)  # recv(max)方法。表示每次仅仅能读取max个字节
                if d:
                    buffer.append(d)
                else:
                    break
            date = b''.join(buffer)
        except Exception :
            return "ERROR_CONN"
        finally:
            try:
                s.close()
            except Exception:
                pass

        string = date.decode('GBK')
        root_pattern = '"active_id":([\s\S]*?),"cmd"'
        result = re.findall(root_pattern, string)

        return result
