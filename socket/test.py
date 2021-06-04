import socket
import json
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",4400));

endstr="#*#DataEnd#*#"

data={"method":"/stopDetect"};

cmd=json.dumps(data)
s.sendall(cmd.encode("utf-8")+endstr.encode("utf-8"))

recv_data_part=s.recv(1024*1024*20)

s.close()
