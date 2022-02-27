#!/usr/bin/env python3
import sys
import argparse
from wiki import search
from wiki import utils

xB = utils.BOLD
xE = utils.END
xBlue = utils.BLUE
xPur = utils.PURPLE

version='0.0.1'
repo='https://github.com/xxx/xxxx'
helpTxt = f'''\
{xPur}wiki v{version}{xE}
search and print wikipedia articles

usage: {xB}wiki{xE} [FLAGS] [QUERY]
       -s, --search    search wikipedia
       -f, --full      print entire article
       -i, --info      print first section of article
       -v, --version   print version ({version})
       -h, --help      print this message

{xBlue}{repo}{xE}'''

class Parser(argparse.ArgumentParser):
    def print_help(self):
        print(helpTxt)

parser = Parser()
parser.add_argument('-v','--version',action='store_true')
parser.add_argument('-s','--search')
parser.add_argument('-f','--full')
parser.add_argument('-i','--info')

args = parser.parse_args()

def arguments():
    if args.search:
        search.searchInfo(args.search)
    if args.full:
        search.getInfo(args.full)
    if args.info:
        search.getSummary(args.info)
    if args.version:
       print(version)
