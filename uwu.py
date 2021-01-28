import winreg
import ctypes

def reboot_pc():
    restart = input("uwu successfully removed watermark! restart (y/n)")
    restart = restart.lower()
    if restart=="n":
        exit()
    elif restart=="y":
        os.system("shutdown /r /t 1")
    else:
        reboot_pc()




def remove_watermark():
    with winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER) as hkey:
        try:
            with winreg.OpenKey(hkey,r"Control Panel\Desktop",0,winreg.KEY_ALL_ACCESS) as sub_key:
                try:
                    winreg.SetValueEx(sub_key, "PaintDesktopVersion", 0, winreg.REG_DWORD, 0)
                    reboot_pc()
                except OSError:
                    try:
                        winreg.CreateKey(hkey,r"Control Panel\Desktop")
                        remove_watermark()
                    except:
                        print("Failed to make key :(")
        except:
            print("owo Failed to get admin rights. pls restart with admin rights ;_;")

print("""\

  ___    _ .--.      .--.  ___    _  
.'   |  | ||  |_     |  |.'   |  | | 
|   .'  | || _( )_   |  ||   .'  | | 
.'  '_  | ||(_ o _)  |  |.'  '_  | | 
'   ( \.-.|| (_,_) \ |  |'   ( \.-.| 
' (`. _` /||  |/    \|  |' (`. _` /| 
| (_ (_) _)|  '  /\  `  || (_ (_) _) 
 \ /  . \ /|    /  \    | \ /  . \ / 
  ``-'`-'' `---'    `---`  ``-'`-''  
                                     

""")
x = input("press 1 to start uwu")
if x==1:
    remove_watermark()
else:
    print("uwu bye!")
    exit()


        
