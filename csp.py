import requests
import sys , argparse
import bcolors

def banner():
    print("""
           
            ░█████╗░░██████╗██████╗░░░░░░░░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
            ██╔══██╗██╔════╝██╔══██╗░░░░░░██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
            ██║░░╚═╝╚█████╗░██████╔╝█████╗╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
            ██║░░██╗░╚═══██╗██╔═══╝░╚════╝░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
            ╚█████╔╝██████╔╝██║░░░░░░░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
            ░╚════╝░╚═════╝░╚═╝░░░░░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝                                                                             
                                                                                         Code by NG          
              """)
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-u'):
        try:
            input_url = sys.argv[2]
            input_header = requests.get(input_url)
            h_text = input_header.headers['content-security-policy']

            parser = argparse.ArgumentParser()
            parser.add_argument("-u", required=True)
            args = parser.parse_args()

            print(bcolors.BITALIC + "Testing for Content Security Policy")
            value = h_text.split(" ")
            for l_value in value:
                if "." in l_value:
                  try:
                    l_value = l_value.replace(";", "")
                    print(l_value)
                  except:
                    print("CSP not possible for the given URL")
        except:
                print('Please enter python CSP.py -u <URL>')
                print("Give Domain with http:// or https://")

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: CSP.py [-h] -d DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u Url,   --url Url' )
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from -u or -h, with a valid url')





