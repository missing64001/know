try:
    import wmi
    Nowmi = False
except Exception:
    Nowmi = True

import os
CURRENTURL = os.path.dirname(__file__)

def main():
    data = get_computer_info()
    print(data)

def get_computer_info():
    bios = get_disk_info()    
    filename = os.path.join(CURRENTURL,'bios.txt')
    with open(filename,'r',encoding='utf-8') as f:
        data = f.read()
        bioses = [ da.strip() for da in data.split('\n')]
    i=-1
    for i,bi in enumerate(bioses):
        if bios in bi:
            return i,bi.split(',')[1]

    with open(filename,'a',encoding='utf-8') as f:
        f.write(bios+',\n')
    return i+1,''


def get_disk_info():
    tmplist = []
    encrypt_str = ""
    c = wmi.WMI ()
    for cpu in c.Win32_Processor():
        encrypt_str = encrypt_str+cpu.ProcessorId.strip()
    for physical_disk in c.Win32_DiskDrive():
        encrypt_str = encrypt_str+physical_disk.SerialNumber.strip()
        tmpdict = {}
        tmpdict["Caption"] = physical_disk.Caption
        tmpdict["Size"] = int(physical_disk.Size)/1000/1000/1000
        tmplist.append(tmpdict)
    for board_id in c.Win32_BaseBoard():
        encrypt_str = encrypt_str+board_id.SerialNumber.strip()

    return encrypt_str 

if __name__ == '__main__':
    main()

if Nowmi:
    get_computer_info = ''
else:
    get_computer_info = get_computer_info()