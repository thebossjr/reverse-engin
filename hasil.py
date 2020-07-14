# Decompiled by Khairul Syabana
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Sazxt>
import os, sys, time, random, socket, select, datetime, threading
version = '2.4.8'
expired = '14/07/2020'
Tsel_Ruangguru = [
 '118.98.93.6:443', 'video-cdn.quipper.com:443', '118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Ilmupedia = ['118.98.104.36:443', '118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Gamesmax = ['118.98.95.91:443', '118.98.95.106:444']
Tsel_Musicmax = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Videomax = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Gigamax = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Maxtream = [
 '118.98.93.65:443',
 '118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Whatsapp = [
 '118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Omg = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Tiktok = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Youtube = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Instagram = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Facebook = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_Conference = ['118.98.95.106:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Tsel_0p0k = ['118.97.159.51:80']
Isat_Edukasi = ['video-cdn.quipper.com:443']
Axis_Ruangguru = ['rubel-video-cdn.ruangguru.com.akamaized.net:443', 'video-cdn.quipper.com:443', '23.219.184.41:443']
Axis_Gaming = ['iflix-videocdn-p2.akamaized.net', 'filecdn-igamecj.akamaized.net:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443', '23.219.184.41:443']
Axis_Sosmed = ['23.45.116.48:443', '23.219.184.41:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Axis_Iflix = ['iflix-videocdn-p1.akamaized.net', 'iflix-videocdn-p2.akamaized.net', 'iflix-videocdn-p3.akamaized.net', 'iflix-videocdn-p6.akamaized.net', 'iflix-videocdn-p7.akamaized.net', 'iflix-videocdn-p8.akamaized.net', 'rubel-video-cdn.ruangguru.com.akamaized.net:443', 'video.iflix.com:443', '23.219.184.41:443']
Xl_Ruangguru = ['rubel-video-cdn.ruangguru.com.akamaized.net:443', 'video-cdn.quipper.com:443']
Xl_Gaming = ['iflix-videocdn-p2.akamaized.net', 'filecdn-igamecj.akamaized.net:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Xl_Iflix = ['iflix-videocdn-p1.akamaized.net', 'iflix-videocdn-p2.akamaized.net', 'iflix-videocdn-p3.akamaized.net', 'iflix-videocdn-p6.akamaized.net', 'iflix-videocdn-p7.akamaized.net', 'iflix-videocdn-p8.akamaized.net', 'video.iflix.com:443', 'rubel-video-cdn.ruangguru.com.akamaized.net:443']
Smart_Ruangguru = ['rubel-video-cdn.ruangguru.com.akamaized.net:443']
Smart_Tiktok = ['rubel-video-cdn.ruangguru.com.akamaized.net:443', 'iflix-videocdn-p1.akamaized.net', 'iflix-videocdn-p2.akamaized.net', 'iflix-videocdn-p3.akamaized.net', 'iflix-videocdn-p6.akamaized.net', 'iflix-videocdn-p7.akamaized.net', 'iflix-videocdn-p8.akamaized.net', 'video.iflix.com:443']

def login():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d/%m/%Y')
    if tgl == expired:
        print colors(('\n').join(['[lightcyan]==================================',
         '[abang]         Script Expired           \n[ijo] Silahkan Update Ke Versi Terbaru ',
         '[lightcyan]==================================',
         '[ijo]>>>[kuneng]sobatgretongan.blogspot.com[ijo]<<<<',
         '[lightcyan]==================================',
         '[ungu]   SALAM GRETONGERS INDONESIA     [kuneng]',
         '[lightcyan]----------------------------------']))
        sys.exit()
    else:
        main()


def main():
    os.system('clear')
    print colors(('\n').join([
     '[cyan]==========================================',
     '[ungu]    =+[ijo] FREENET TOOLS               [ungu]+=',
     '[ungu]    =+[kuneng] SCRIPT Qpython v' + version + '       [ungu]+=',
     '[ungu]    =+[cyan]-----------------------------[ungu]+=',
     '[ungu]    =+[cyantik] Contact Me:                 [ungu]+=',
     '[ungu]    =+[lightblue] facebook.com/vipscript.py   [ungu]+=',
     '[ungu]    =+[cyantik] Update Script:              [ungu]+=',
     '[ungu]    =+[lightblue] sobatgretongan.blogspot.com [ungu]+=',
     '[cyan]==========================================',
     '[ijo]Set Psiphon:[darkgray]                Exp:' + expired + '',
     '[kuneng]Host:127.0.0.1',
     '[kuneng]Port:8080',
     '[ijo]Note:',
     '[kuneng]User popon wajib Speed Boost/Trial akun \nSupaya mendapatkan Speed yang Maxsimal',
     '[lightcyan]------------------------------------------',
     '[ungu]|NO| SC   Nama Paket   Keterangan|',
     '[ungu][[ijo]01[ungu]][abang] TSEL[lightcyan] RuangGuru[ijo]    [All TKP]',
     '[ungu][[ijo]02[ungu]][abang] TSEL[lightcyan] IlmuPedia[ijo]    [All TKP]',
     '[ungu][[ijo]03[ungu]][abang] TSEL[lightcyan] GamesMax[ijo]     [All TKP]',
     '[ungu][[ijo]04[ungu]][abang] TSEL[lightcyan] MusicMax[ijo]     [All TKP]',
     '[ungu][[ijo]05[ungu]][abang] TSEL[lightcyan] VideoMax[ijo]     [All TKP]',
     '[ungu][[ijo]06[ungu]][abang] TSEL[lightcyan] GigaMax[ijo]      [All TKP]',
     '[ungu][[ijo]07[ungu]][abang] TSEL[lightcyan] Maxtream[ijo]     [All TKP]',
     '[ungu][[ijo]08[ungu]][abang] TSEL[lightcyan] Unlimited Whatsapp[ijo]  [All TKP]',
     '[ungu][[ijo]09[ungu]][abang] TSEL[lightcyan] Omg[ijo]          [All TKP]',
     '[ungu][[ijo]10[ungu]][abang] TSEL[lightcyan] Ketengan Tiktok[ijo]     [All TKP]',
     '[ungu][[ijo]11[ungu]][abang] TSEL[lightcyan] Ketengan Youtube[ijo]    [All TKP]',
     '[ungu][[ijo]12[ungu]][abang] TSEL[lightcyan] Ketengan Instagram[ijo]  [All TKP]',
     '[ungu][[ijo]13[ungu]][abang] TSEL[lightcyan] Ketengan Facebook[ijo]   [All TKP]',
     '[ungu][[ijo]14[ungu]][abang] ISEL[lightcyan] Ketengan Conference[ijo] [All TKP]',
     '[ungu][[ijo]15[ungu]][abang] TSEL[lightcyan] 0P0K [ijo]        [TKP Jateng]',
     '[ungu][[ijo]16[ungu]][kuneng] ISAT[lightcyan] Edukasi 5K[ijo]   [All TKP]',
     '[ungu][[ijo]17[ungu]][ungu] AXIS[lightcyan] RuangGuru[ijo]    [All TKP]',
     '[ungu][[ijo]18[ungu]][ungu] AXIS[lightcyan] Gaming[ijo]       [All TKP]',
     '[ungu][[ijo]19[ungu]][ungu] AXIS[lightcyan] Sosmed[ijo]       [All TKP]',
     '[ungu][[ijo]20[ungu]][ungu] AXIS[lightcyan] Iflix[ijo]        [All TKP]',
     '[ungu][[ijo]21[ungu]][lightblue] XL[lightcyan]   Ruangguru[ijo]    [All TKP]',
     '[ungu][[ijo]22[ungu]][lightblue] XL[lightcyan]   Xtra Games[ijo]   [All TKP]',
     '[ungu][[ijo]23[ungu]][lightblue] XL[lightcyan]   Iflix[ijo]        [All TKP]',
     '[ungu][[ijo]24[ungu]][abang] SMARTFREN[lightcyan] Ruangguru[ijo]      [All TKP]',
     '[ungu][[ijo]25[ungu]][abang] SMARTFREN[lightcyan] Tiktok[ijo]  [All TKP]',
     '[ungu][[ijo]26[ungu]][kuneng] Costum  Bug[ijo]       [Pengembang]',
     '[ungu][[ijo]27[ungu]][kuneng] Scaning Bug[ijo]       [Pengembang]',
     '[ungu][[ijo]00[ungu]][abang] Exit',
     '[kuneng]']))
    inject('127.0.0.1', '8080 ').start()


lock = threading.RLock()
os.system('cls' if os.name == 'nt' else 'clear')

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name


def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [ x for x in array if x ]


def colors(value):
    patterns = {'puteh': '\x1b[0m', 
       'abang': '\x1b[31;1m', 
       'abang_m': '\x1b[31;2m', 'ijo': '\x1b[32;1m', 
       'ijo_m': '\x1b[32;2m', 
       'kuneng': '\x1b[33;1m', 
       'kuneng_m': '\x1b[33;4m', 
       'ungu': '\x1b[35;1m', 
       'ungu_janda': '\x1b[35;2m', 
       'cyan': '\x1b[0;36m', 
       'cyantik': '\x1b[2;36m', 
       'purple': '\x1b[0;35m', 
       'brown': '\x1b[0;33m', 
       'lightgray': '\x1b[0;37m', 
       'darkgray': '\x1b[1;30m', 
       'lightblue': '\x1b[1;34m', 
       'lightgreen': '\x1b[1;32m', 
       'lightcyan': '\x1b[4;36m', 
       'lightred': '\x1b[1;31m', 
       'lightpurple': '\x1b[1;35m', 
       'yellow': '\x1b[1;33m', 
       'white': '\x1b[1;37m'}
    for code in patterns:
        value = value.replace(('[{}]').format(code), patterns[code])

    return value


def log(value, status='[cyan]::', color='[puteh]'):
    value = colors(('{color}[ungu][{time}] [puteh]{color}{status} [puteh]{color}{value}[puteh]').format(time=datetime.datetime.now().strftime('%H:%M:%S'), value=value, color=color, status=status))
    with lock:
        print value


def log_replace(value, status='WARNING', color='[kuneng]'):
    value = colors(('{}{} ({})        [puteh]\r').format(color, status, value))
    with lock:
        sys.stdout.write(value)
        sys.stdout.flush()


class inject(object):

    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()
        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def log(self, value, color='[ijo]'):
        log(value, color=color)

    def start(self):
        try:
            pilih = raw_input('Pilih : ')
            if pilih == '0' or pilih == '00':
                print colors(('\n').join(['[ijo]Bye Sob...[puteh]']))
                sys.exit()
            else:
                if pilih == '1' or pilih == '01':
                    frontend_domains = Tsel_Ruangguru
                else:
                    if pilih == '2' or pilih == '02':
                        frontend_domains = Tsel_Ilmupedia
                    elif pilih == '3' or pilih == '03':
                        frontend_domains = Tsel_Gamesmax
                    elif pilih == '4' or pilih == '04':
                        frontend_domains = Tsel_Musicmax
                    elif pilih == '5' or pilih == '05':
                        frontend_domains = Tsel_Videomax
                    elif pilih == '6' or pilih == '06':
                        frontend_domains = Tsel_Gigamax
                    elif pilih == '7' or pilih == '07':
                        frontend_domains = Tsel_Maxtream
                    elif pilih == '8' or pilih == '08':
                        frontend_domains = Tsel_Whatsapp
                    elif pilih == '9' or pilih == '09':
                        frontend_domains = Tsel_Omg
                    elif pilih == '10':
                        frontend_domains = Tsel_Tiktok
                    elif pilih == '11':
                        frontend_domains = Tsel_Youtube
                    elif pilih == '12':
                        frontend_domains = Tsel_Instagram
                    elif pilih == '13':
                        frontend_domains = Tsel_Facebook
                    elif pilih == '14':
                        frontend_domains = Tsel_Conference
                    elif pilih == '15':
                        frontend_domains = Tsel_0p0k
                    elif pilih == '16':
                        frontend_domains = Isat_Edukasi
                    elif pilih == '17':
                        frontend_domains = Axis_Ruangguru
                    elif pilih == '18':
                        frontend_domains = Axis_Gaming
                    elif pilih == '19':
                        frontend_domains = Axis_Sosmed
                    elif pilih == '20':
                        frontend_domains = Axis_Iflix
                    elif pilih == '21':
                        frontend_domains = Xl_Ruangguru
                    elif pilih == '22':
                        frontend_domains = Xl_Gaming
                    elif pilih == '23':
                        frontend_domains = Xl_Iflix
                    elif pilih == '24':
                        frontend_domains = Smart_Ruangguru
                    elif pilih == '25':
                        frontend_domains = Smart_Tiktok
                    elif pilih == '26':
                        bug = raw_input('Bug : ')
                        frontend_domains = [bug]
                    elif pilih == '27':
                        print colors(('\n').join(['[lightcyan]Bikin file[kuneng] bug.ini[lightcyan] dalem folder scripts\n', '[ijo]Scaning bug...']))
                        frontend_domains = open(real_path('/bug.ini')).readlines()
                    else:
                        print colors(('\n').join(['[ijo]Pilihan tidak ada sob..']))
                        raw_input(colors('[cyan][Enter][puteh]'))
                        sys.exit()
                        frontend_domains = filter_array(frontend_domains)
                    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket_server.bind((self.inject_host, self.inject_port))
                    socket_server.listen(1)
                    if len(frontend_domains) == 0:
                        self.log('Bugnya mana cokk', color='[kuneng]')
                        return
                self.log(('START [kuneng]PSIPHON[cyan] ||[ijo]=[abang]-------[abang]-[ijo]=[cyan]||').format(self.inject_host, self.inject_port))
                while True:
                    socket_client, _ = socket_server.accept()
                    socket_client.recv(99999)
                    domain_fronting(socket_client, frontend_domains).start()

        except Exception as exception:
            print colors(('\n').join(['[abang]        Bersihkan Cache nya Sob[ijo]:[abang]v[puteh]']))
            sys.exit()


class domain_fronting(threading.Thread):

    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()
        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = 99999
        self.daemon = True

    def log(self, value, status='[cyan]::', color='[puteh]'):
        log(value, status=status, color=color)

    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [
         socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 1
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors:
                break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data:
                            break
                        elif sock is socket_client:
                            socket_tunnel.sendall(data)
                        elif sock is socket_tunnel:
                            socket_client.sendall(data)
                        timeout = 0
                    except:
                        break

            if timeout == 30:
                break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 2 and self.proxy_host_port[1] else '443'
            self.log(('[ijo]CONNECTING [cyan]:: ||[ijo]=[abang]-[lightblue] +|+  [abang]-[ijo]=[cyan]||').format(self.proxy_host, self.proxy_port))
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall('HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            self.log(('[kuneng]CONNECTEDD[cyan] :: ||[ijo]=[abang]-[lightblue]  +|+ [abang]-[ijo]=[cyan]||').format(self.proxy_host, self.proxy_port), color='[puteh]')
        except OSError:
            self.log('Connection Error', color='[puteh]')
        except TimeoutError:
            self.log(('{} Not Responding').format(self.proxy_host), color='[abang]')


if __name__ == '__main__':
    login()