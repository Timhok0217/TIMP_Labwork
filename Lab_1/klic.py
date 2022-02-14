import os
import ntsecuritycon as con
import win32security as win32sec
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

folder_track=r'D:\for python\sublime'

def best():
    sd = win32sec.GetFileSecurity(r'D:\for python\sublime\template.tbl',win32sec.DACL_SECURITY_INFORMATION)# получаем DACL FILENAME
    dacl = win32sec.ACL()# инициализация для того чтобы установить новые настройки
    sid = win32sec.SID(win32sec.ConvertStringSidToSid("S-1-1-0"))
    dacl.AddAccessAllowedAce(win32sec.ACL_REVISION, con.FILE_ALL_ACCESS, sid)
    sd.SetSecurityDescriptorDacl(1, dacl, 0)# прикрепляю измененные значения к дескриптору
    win32sec.SetFileSecurity(r'D:\for python\sublime\template.tbl', win32sec.DACL_SECURITY_INFORMATION,sd)# возвращаю дескриптор

    file_tbl = open("template.tbl", "r")
    b = file_tbl.read()
    b = str(b).split(" ")

    sd = win32sec.GetFileSecurity(r'D:\for python\sublime\template.tbl',win32sec.DACL_SECURITY_INFORMATION)
    dacl = win32sec.ACL()
    sid = win32sec.SID(win32sec.ConvertStringSidToSid("S-1-1-0"))
    dacl.AddAccessDeniedAce(win32sec.ACL_REVISION, con.FILE_ALL_ACCESS, sid)
    sd.SetSecurityDescriptorDacl(1, dacl, 0)
    win32sec.SetFileSecurity(r'D:\for python\sublime\template.tbl', win32sec.DACL_SECURITY_INFORMATION,sd)
    return b

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir(folder_track):
            a = filename[:filename.index(".")]
            pyti=event.src_path
            pyti = pyti[22:pyti.find(".")]
            if (a in best()) and (a==pyti):
                c=str(a)+'.txt'
                os.remove(c)
                print("Вы создали недопустимый файл, он будет автоматически удален.")

def arrow():
    for filename in os.listdir(folder_track):
        filename = filename[:filename.index(".")]
        if filename in best():
            FILENAME = r"D:\for python\sublime\{}.txt".format(filename)
            sd = win32sec.GetFileSecurity(FILENAME, win32sec.DACL_SECURITY_INFORMATION)
            dacl = win32sec.ACL()
            sid = win32sec.SID(win32sec.ConvertStringSidToSid("S-1-1-0"))
            dacl.AddAccessDeniedAce(win32sec.ACL_REVISION, con.FILE_ALL_ACCESS, sid)
            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32sec.SetFileSecurity(FILENAME, win32sec.DACL_SECURITY_INFORMATION, sd)

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_track, recursive=False)
    observer.start()
    while True:
        try:
            print("Введите пароль")
            passwd = input()
            if passwd == "123":
                print("Пароль верный!")
                for filename in os.listdir(folder_track):
                    filename = filename[:filename.index(".")]
                    if filename in best():
                        FILENAME = r"D:\for python\sublime\{}.txt".format(filename)
                        sd = win32sec.GetFileSecurity(FILENAME, win32sec.DACL_SECURITY_INFORMATION)
                        dacl = win32sec.ACL()
                        sid = win32sec.SID(win32sec.ConvertStringSidToSid("S-1-1-0"))
                        dacl.AddAccessAllowedAce(win32sec.ACL_REVISION, con.FILE_ALL_ACCESS,sid)
                        sd.SetSecurityDescriptorDacl(1, dacl, 0)
                        win32sec.SetFileSecurity(FILENAME, win32sec.DACL_SECURITY_INFORMATION,sd)
                pass
                observer.stop()
                break
            else:
                print("Неправильный пароль! До свидания!")
                exit()
        except KeyboardInterrupt:
            print(":(")

    temp = input("Хотите открыть template? (Д\Н)")
    if temp == "Д":
        print("У вас есть 20 секунд!")
        sd = win32sec.GetFileSecurity(r'D:\for python\sublime\template.tbl',win32sec.DACL_SECURITY_INFORMATION)
        dacl = win32sec.ACL()
        sid = win32sec.SID(win32sec.ConvertStringSidToSid("S-1-1-0"))
        dacl.AddAccessAllowedAce(win32sec.ACL_REVISION, con.FILE_ALL_ACCESS, sid)
        sd.SetSecurityDescriptorDacl(1, dacl, 0)
        win32sec.SetFileSecurity(r'D:\for python\sublime\template.tbl', win32sec.DACL_SECURITY_INFORMATION,sd)
        time.sleep(20)
        print("Время вышло!")

    sd = win32sec.GetFileSecurity(r'D:\for python\sublime\template.tbl',win32sec.DACL_SECURITY_INFORMATION)
    dacl = win32sec.ACL()
    sid = win32sec.SID(win32sec.ConvertStringSidToSid("S-1-1-0"))
    dacl.AddAccessDeniedAce(win32sec.ACL_REVISION, con.FILE_ALL_ACCESS, sid)
    sd.SetSecurityDescriptorDacl(1, dacl, 0)
    win32sec.SetFileSecurity(r'D:\for python\sublime\template.tbl', win32sec.DACL_SECURITY_INFORMATION,sd)
    nachalo=input("Хотите заново ограничить права? (Д\Н)")
    if (nachalo=="Д"):
        arrow()
    else:
        exit()
arrow()


