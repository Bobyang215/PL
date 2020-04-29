import socket

# created a socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# create connection
s.connect(('www.sina.com.cn',433))

# send data
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# revice data
buffer = []
while True:
    # max size of revice context
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# close the connect
s.close()

# Analytical data
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

# write the reviced data to file
with open('sina.html','wb') as f:
    f.write(html)

