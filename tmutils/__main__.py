import argparse
from tmutils.utils import random_month

arg_parser = argparse.ArgumentParser(
    description="Generate sample case reports, for report templates development purpose.",
    prog='python -m tmutils',
    allow_abbrev=True,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    # formatter_class=argparse.RawDescriptionHelpFormatter,
)

arg_parser.add_argument(
    "-i",
    "--init",
    help="initialize templates sandbox",
    action="store_true",
    default=False,
    required=False,
)

arg_parser.add_argument(
    "-r",
    "--reset",
    help="reset templates sandbox",
    action="store_true",
    default=False,
    required=False,
)

arg_parser.add_argument(
    "-d",
    "--dir",
    help="target directory for generated reports",
    type=str,
    default=".",
    required=False,
)

arg_parser.add_argument(
    "-g",
    "--generate",
    metavar="NUM",
    help="generate sample reports, 0 means all",
    nargs='?',
    const=3,
    required=False,
)

args = arg_parser.parse_args()

if args.reset:
    print("RESET TEMPLATES SANDBOX FFFF")
elif args.init:
    print("INITIALIZE TEMPLATES SANDBOX FFFF")
elif args.generate:
    if args.generate == "0":
        print("GENEARATE ALL THE REPORTS.")
    else:
        print(f"GENERATE {args.generate} REPORTS.")
else:
    arg_parser.print_usage()
