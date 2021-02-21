import requests
import sys, argparse
import bcolors
import os

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
          if(os.path.exists(input_url)!= True):
            input_header = requests.get(input_url)
            if ('content-security-policy' in input_header.headers):
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
            else:
                print('content-security-policy header not present')
          elif (os.path.exists(input_url) == True):
                input_file = open(input_url, "r")
                input_file_line = input_file.readlines()
                for file_url in input_file_line:
                 try:
                    url = file_url.strip()
                    input_header = requests.get(url)
                    print('\n' + bcolors.BITALIC + "Testing for Content Security Policy" + url )
                    print('*************************************************************************')
                    if ('content-security-policy' in input_header.headers):
                        h_text = input_header.headers['content-security-policy']
                        parser = argparse.ArgumentParser()
                        parser.add_argument("-u", required=True)
                        args = parser.parse_args()
                        value = h_text.split(" ")
                        for l_value in value:
                            if "." in l_value:
                                try:
                                    l_value = l_value.replace(";", "")
                                    print(l_value)
                                except:
                                    print("CSP not possible for the given URL")
                    else:
                        print('content-security-policy header not present')
                 except:
                    print('Error in any URL')

        except:
            print('Please enter python CSP.py -u <URL>')
            print("Give Domain with http:// or https://")

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: CSP.py [-h] -u DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u Url,   --url Url')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from -u or -h, with a valid url')





