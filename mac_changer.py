

import subprocess
import optparse


def change_mac(interface, mac_address):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
    subprocess.call(['ifconfig', interface, 'up'])
    print('[+] Interface = ' + options.interface + '\n[+] New Mac Address =' + options.mac_address)


def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option('-i', '--interface', dest="interface", help='Interface of the module to change mac addres')
    parse.add_option('-m', '--mac', dest="mac_address", help="mac address to be changed")
    (options,arguments)= parse.parse_args()
    if not options.interface:
        parse.error('[-] please specify a valid interface. For help check --help command')
    elif not options.mac_address:
        parse.error('[-] please specify a valid mac address. For help check --help command')
    return options



# interface = input('\tInterface(wlan0/eth0/other) > ')
# mac_address = input('\tNew Mac > ')

print('[+] Mac Address changing program ')
print('[+] NOTE::Use python 3 to run this program(recomended) ')

options = get_arguments()

interface = options.interface   #interface = options.(destination(dest in parse.add_option) file name)
mac = options.mac_address      #mac= new variable

change_mac(interface, mac)
