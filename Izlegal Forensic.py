try:
    import requests
    import os
except Exception:
    print("pip install requests")

os.system("cls")

banner = """Izlegal[MrX] Forensic Tool"""

menu = """
    Izlegal[MrX] Forensic Tool
    Eğer 'Quoota Limit' diye hata verirse IP değiştirin.
    
 0 => Close The Program
 1 => Reverse DNS
 2 => DNS Lookup
 3 => Geolocation IP
 4 => Zone Transfer
 5 => DNS Host Records (Subdomains)
 6 => Reverse IP Lookup
 7 => ASN Lookup
 8 => Email Validator (ALL SMTP SERVER)
 9 => Have I Been Pwned?!
 10 => DMARC Lookup
"""

print(menu)

choice = int(input(" Choose ur want: "))
os.system("cls")
if choice == 0:
    exit()
print(banner)


headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded"
        }

if choice == 1:
    def reversedns():
        dns = input("IP Address: ")
        print("")
        r = requests.get(f"https://api.hackertarget.com/reversedns/?q={dns}")

        print(r.text, "| => Press ENTER For Exit.")
        input()

    reversedns()

if choice == 2:
    def dnslookup():
        lookup = input("Domain Name: ")
        print("")
        x = requests.get(f"https://api.hackertarget.com/dnslookup/?q={lookup}")

        print(x.text), "| => Press ENTER For Exit."
        input()

    dnslookup()

if choice == 3:
    def geoip():
        geoip = input("IP Address: ")
        print("")
        i = requests.get(f"https://api.hackertarget.com/geoip/?q={geoip}")

        print(i.text), "| => Press ENTER For Exit."
        input()

    geoip()

if choice == 4:
    def zonetransfer():
        zonetransfer = input("IP Address: ")
        print("")
        z = requests.get(f"https://api.hackertarget.com/zonetransfer/?q={zonetransfer}")

        print(z.text), "| => Press ENTER For Exit."
        input()

    zonetransfer()

if choice == 5:
    def dnssubdomain():
        subdomain = input("Domain Name: ")
        print("")
        k = requests.get(f"https://api.hackertarget.com/hostsearch/?q={subdomain}")

        print(k.text), "| => Press ENTER For Exit."
        input()

    dnssubdomain()

if choice == 6:
    def reverseip():
        reverseip = input("IP Address: ")
        print("")
        mrx = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={reverseip}")

        print(mrx.text), "| => Press ENTER For Exit."
        input()

    reverseip()

if choice == 7:
    def ASN():
        asnlookup = input("IP Address or ASN: ")
        print("")
        hasfa = requests.get(f"https://api.hackertarget.com/aslookup/?q={asnlookup}")

        print(hasfa.text), "| => Press ENTER For Exit."
        input()

    ASN()

if choice == 8:
    def emailvalid():
        mailvalid = input("Email Gir: ")
        print("")

        datas = f'address=&email={mailvalid}&submit=Verify+Email+Address'
        
        mrxvalid = requests.post("https://www.iplocation.net/verify-email-address/", data=datas, headers=headers)

        if 'is a valid email' in mrxvalid.text:
            print("[+] Bu Mail E-Posta alabilir.")
        elif "is an invalid email" in mrxvalid.text:
            print("[-] Bu Mail Çalışmamaktadır.")

    emailvalid()

if choice == 9:
    def proxycheck():
        proxy = input("Mail Address: ")
        print("")
        proxy.replace("@","%40")

        datas = f'email={proxy}&submit=Breached%3F'
        proxyy = requests.post("https://www.iplocation.net/data-breach-check", data=datas, headers=headers)

        if "Congratulations" in proxyy.text:
            print("[+] Private Mail Address")
        elif "We found" in proxyy.text:
            print("[-] Mail Public!!")

    proxycheck()

if choice == 10:
    def DMARC():
        ece = input("Domain Address: ")
        print("")

        datas = f'url={ece}&submit='
        DMARCR = requests.post("https://tools.iplocation.net/dmarc-lookup", data=datas, headers=headers)

        if "v=DMARC1" in DMARCR.text:
            print("[+] Have Firewall")
        elif "No record found" in DMARCR.text:
            print("[-] No Firewall")

    DMARC()