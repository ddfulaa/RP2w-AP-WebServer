import os, time, wifi, socketpool

wifi.radio.start_station()
if not wifi.radio.ap_active:
    wifi.radio.start_ap(os.getenv('WIFI_SSID'),os.getenv('WIFI_PW'))

print(wifi.radio.ipv4_address_ap)   

pool = socketpool.SocketPool(wifi.radio)

html = """<!DOCTYPE html>
<html>
    <head> <title>Raspberry Pi Pico W</title> <meta http-equiv="content-type" content="text/html;charset=utf-8" /></head>
    <body> <h1>Hola</h1>
        <p>¡Hola! Saludos desde la Raspberry Pi pico W.</p>        
    </body>
</html>
"""

pool = socketpool.SocketPool(wifi.radio)
addr = pool.getaddrinfo('0.0.0.0', 80)[0][-1]
s = pool.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        b = bytearray(1024)
        request = cl.recv_into(b,1024)
        print(request)

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()
        

    except OSError as e:
        cl.close()
        print('connection closed')
