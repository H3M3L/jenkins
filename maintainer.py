#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print('Usage: {} <codename>'.format(argv[0]))
    exit(1)

maintainers = {
    'begonia': 'aashil123',
    'ginkgo': 'Introdructor',
    'raphael': 'ritzz97',
    'mido': 'Apon77',
    'X00P': 'Flamefusion',
    'santoni': 'jubayerhimel',
    'violet': 'ShivamKumar2002',
    'jd2019': 'merser2005',
    's2': 'merser2005',
    'tissot': 'Takeshiro',
}

device = argv[1]

maintainer = maintainers.get(device, 'CorvusJenkinsBot')
print(f'@{maintainer}  {device} !')
