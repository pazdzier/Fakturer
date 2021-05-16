import argparse
from dev_tools.populator import fake_contractor, fake_user

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--user', action='store_true', help="Tworzy użytkownika")
parser.add_argument('-c', '--contractor', action='store_true', help="Tworzy kontrahenta")
parser.add_argument('-n', type=int, help="Podaj liczbę kontrahentów do utworzenia")

args = parser.parse_args()

if args.n and not args.contractor:
    parser.error('Argument')

if args.contractor:
    if args.n:
        fake_contractor(args.n)
    else:
        fake_contractor(1)

if args.user:
    fake_user()