import platform
import socket
import os


def Get_information():
    sysinfo_lis=[]
    sysinfo=platform.uname()
    for i in sysinfo:
        sysinfo_lis.append(i)
    
    return sysinfo_lis





def Get_ip():
    Host_name=socket.gethostname()
    ip_address=socket.gethostbyname(Host_name)
    return ip_address


def Get_cores():
    cnumbers=os.cpu_count()
    return cnumbers



