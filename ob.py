# K-fuscator
# Author: KasRoudra
# Github:  https://github.com/KasRoudra
# Contact: https://m.me/KasRoudra

# Encrypt(obfuscate) or decrypt bash/shell script or compile python script

import os, base64
from pprint import pformat
os.system("clear")
alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]
MAX_STR_LEN = 70
OFFSET = 10
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
P="\033[0;35m"
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
success = G + '[' + W + '√' + G + '] '
error = R + '[' + W + '!' + R + ']'

def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code


def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")


def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )


def encryptsh():
    script = input(ask + C + "Input Filename " + G + "> " + B)
    if not os.path.exists(script):
        print(error+' File not found')
        os.system("sleep 2")
        encryptsh()
    try:
        os.system("bash-obfuscate " + script + " -o .temp")
    except:
       print(error+" Bash-Obfuscate not installed! Install it by:\n"+G+"[+] \"apt install nodejs -y && npm install -g bash-obfuscate\"")
       exit(1)
    if not os.path.exists(".temp"):
       print(error+" Bash-Obfuscate not installed! Install it by:\n"+G+"[+] \"apt install nodejs -y && npm install -g bash-obfuscate\"")
       exit(1)
    m = open(".temp",'r')
    filedata = m.read()
    m.close()
    output = input(ask + C + "Output Filename " + G + "> " + B)
    os.remove(output)
    g = open(output,'w')
    g.write("# Encrypted by K-fuscator\n# Github- https://github.com/KasRoudra/k-fuscator\n\n"+filedata)
    g.close()
    os.remove(".temp")
    print(success + output + " saved in current directory")
    if os.path.exists("/sdcard/Download"):
        os.system("cp -r "+output+" /sdcard/Download")
        print(success+ output+ " copied to Download or /sdcard/Download")
    if os.path.exists("/home/Downloads"):
        os.system("cp -r "+output+" /home/Downloads")
        print(success+ output+ " copied to Downloads or /home/Downloads")
    os.system("sleep 3")    
    main()
    

def decryptsh():
    try:
        text1 = input(ask + C + "Input File " + G + "> " + B)
        if not os.path.exists(text1):
            print(error+' File not found')
            os.system("sleep 2")
            decryptsh()
        f = open(text1,'r')
        filedata = f.read()
        f.close()
        if not (filedata.find("eval") != -1):
            print(error+" Cannot be decrypted!")
            exit()

        newdata = filedata.replace("eval","echo")
        
        output = input(ask + C + "Output File " + G + " > " + B)
        f = open(".temp1",'w')
        f.write(newdata)
        f.close()

        os.system("touch .temp2")
        os.system("bash .temp1 > .temp2")
        os.remove(".temp1")
        m = open(".temp2",'r')
        filedata = m.read()
        m.close()
        g = open(output,'w')
        g.write("# Decrypted by K-fuscator\n# Github- https://github.com/KasRoudra/k-fuscator\n\n"+filedata)
        g.close()
        os.remove(".temp2")
        print (success + output + " saved in current directory")
        if os.path.exists("/sdcard/Download"):
            os.system("cp -r "+output+" /sdcard/Download")
            print(success+ output+ " copied to Download or /sdcard/Download")
        if os.path.exists("/home/Downloads"):
            os.system("cp -r "+output+" /home/Downloads")
            print(success+ output+ " copied to Downloads or /home/Downloads")
        os.system("sleep 3")
        main()
    except KeyboardInterrupt:
        print (error + " Stopped!")
    except IOError:
        print (error + " File Not Found!")

       
def encryptvar():
    try:
        var= input(ask + C + "Variable to be used(Must Required)" + G + "> " + B)
        if (var==""):
            print(error + " No variable")
            os.system("sleep 3")
            encryptvar()
        if (var.find(" ")!= -1):
            print(error+" Only one word!")
            os.system("sleep 3")
            encryptvar()
        VARIABLE_NAME = var * 100
        path = input(ask + C + "Input file " + G + "> " + B)
        if not os.path.exists(path):
            print(error+' File not found')
            os.system("sleep 2")
            encryptvar()
        out = input(ask + C + "Output file " + G + "> " + B)
        
        if not os.path.isfile(path) or not path.endswith('.py'):
            print(error+' Invalid file')
            exit()
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

        obfuscated_content = obfuscate(VARIABLE_NAME, file_content)

        with open(out, 'w') as file:
            file.write("# Encrypted by K-fuscator\n# Github- https://github.com/KasRoudra/k-fuscator\n\n"+obfuscated_content)

        print (success + out + " saved in current directory")
        if os.path.exists("/sdcard/Download"):
            os.system("cp -r "+out+" /sdcard/Download")
            print(success+ out + " copied to Download or /sdcard/Download")
        if os.path.exists("/home/Downloads"):
            os.system("cp -r "+out+" /home/Downloads")
            print(success+out+" copied to Downloads or /home/Downloads")  
        os.system("sleep 3")
        main()
    except KeyboardInterrupt:
        print (error + " Stopped!")
    except IOError:
        print (error + " File Not Found!")
        

def encryptem():
    in_file= input(ask + C + "Input File " + G + "> " + B)
    if not os.path.exists(in_file):
            print(error+' File not found')
            os.system("sleep 2")
            encryptem()
    out_file= input(ask + C + "Output File " + G + "> " + B)
    if os.path.exists(in_file):
        with open(in_file) as in_f, open(out_file, "w") as out_f:
            out_f.write("# Encrypted by K-fuscator\n# Github- https://github.com/KasRoudra/k-fuscator\n\n")
            out_f.write(encode_string(in_f.read(), alphabet))
            print(success+out_file+" saved in current directory")
            if os.path.exists("/sdcard/Download"):
                os.system("cp -r "+out_file+" /sdcard/Download")
                print(success+ out_file + " copied to Download or /sdcard/Download")
            if os.path.exists("/home/Downloads"):
                os.system("cp -r "+out_file+" /home/Downloads")
                print(success+ out_file + " copied to Downloads or /home/Downloads") 
            os.system("sleep 3")
            main()
    elif not os.path.isfile(in_file) or not path.endswith('.py'):
        print(error+'Invalid file')
        exit()
    elif IOError:
        print(error+"File not found")
    else:
        print(error+"Error!")
        exit()


def main():
    os.system("clear")
    print(G+'''
     _  __     _____                    _
    | |/ /    |  ___|   _ ___  ___ __ _| |_ ___  _ __
    | ' /_____| |_ | | | / __|/ __/ _` | __/ _ \| '__|
    | . \_____|  _|| |_| \__ \ (_| (_| | || (_) | |
    |_|\_\    |_|   \__,_|___/\___\__,_|\__\___/|_|''')
    print(Y+'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(R+'[ToolName]  '+C+' :[K-fuscator] ')
    print(R+'[Version]   '+C+' :[1.0]')
    print(R+'[Author]    '+C+' :[KasRoudra] ')
    print(R+'[Github]    '+C+' :[https://github.com/KasRoudra] ')
    print(R+'[Messenger] '+C+' :[https://m.me/KasRoudra]')
    print(R+'[Email]     '+C+' :[kasroudrakrd@gmail.com]')
    print(Y+'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('''
      ____  _             _
     / ___|| |_ __ _ _ __| |_
     \___ \| __/ _` | '__| __|
      ___) | || (_| | |  | |_
     |____/ \__\__,_|_|   \__|
    
    ''')
    print(G+'[1] '+R+' Encrypt '+C+' Bash/Shell')
    print(G+'[2] '+R+' Decrypt '+C+' Bash/Shell')
    print(G+'[3] '+R+' Encrypt '+C+' Python into Variable')
    print(G+'[4] '+R+' Encrypt '+C+' Python into emoji')
    print(G+'[5] '+R+' More Tools')
    print(G+'[0] '+R+' Exit')
    print(Y+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    choose = input(R+'\n[?] '+Y+'Choose : '+B)

    while True:
        if choose == "1":
            encryptsh()
        elif choose == "2":
            decryptsh()
        elif choose == "3":
            encryptvar()
        elif choose == "4":
            encryptem()
        elif choose == "5":
            system('xdg-open https://github.com/KasRoudra?tab=repositories')
            break
        elif choose == "0":
            exit()
        else:
            print('Please choose 1 or 2 or 3 or 4 or 5 or 0 for exit')
            os.system("sleep 2")
            main()
main()        
