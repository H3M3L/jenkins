#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print('Usage: {} <codename>'.format(argv[0]))
    exit(1)

maintainers = {
    'begonia': 'aashil123',
    'raphael': 'ritzz97',
    'mido': 'Apon77',
    'X00P': 'Flamefusion',
    'jd2019': 'merser2005',
    's2': 'merser2005',
}

device = argv[1]

maintainer = maintainers.get(device, 'CorvusJenkinsBot')
print(f'@{maintainer}  {device} !')
