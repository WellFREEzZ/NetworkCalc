class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def calculate_network():
    network_str = input('Введите сеть:\n')
    dec_address, wide = network_str.split('/')
    dec_bytes = dec_address.split('.')
    wide = int(wide)
    bin_bytes = [bin(int(d)) for d in dec_bytes]
    bin_bytes_str = [str(d).replace('0b', '') for d in bin_bytes]
    bin_bytes_str_f = [d if len(d) == 8 else "0" * (8-len(d)) + d for d in bin_bytes_str]
    minimum = bcolors.FAIL
    wide_ = wide
    for i, bb in enumerate(bin_bytes_str_f):
        if wide_ >= 8:
            minimum += bb + '.'
            wide_ -= 8
        elif wide_ > 0:
            minimum += bb[:wide_] + bcolors.ENDC
            minimum += bb[wide_:] if i > 2 else bb[wide_:] + '.'
            wide_ = 0
        else:
            if bcolors.ENDC in minimum:
                minimum += bb if i > 2 else bb + '.'
            else:
                minimum += bcolors.ENDC
                minimum += bb if i > 2 else bb + '.'
    maximum = minimum[:minimum.find(bcolors.ENDC)] + bcolors.ENDC + minimum[minimum.find(bcolors.ENDC):].replace(bcolors.ENDC, '').replace('0', '1')
    print(f'{minimum} - {maximum}')
    dec_min = [str(int(d, 2)) for d in minimum.replace(bcolors.ENDC, '').replace(bcolors.FAIL, '').split('.')]
    dec_max = [str(int(d, 2)) for d in maximum.replace(bcolors.ENDC, '').replace(bcolors.FAIL, '').split('.')]
    print(f"{'.'.join(dec_min)} - {'.'.join(dec_max)}")
    print('- - - - - - - - - - - - - \n')


if __name__ == '__main__':
    while True:
        calculate_network()