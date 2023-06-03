import argparse
from tm_utils.utils import random_month

arg_parser = argparse.ArgumentParser(
    description="Generate sample case reports, for report templates development purpose.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

args = arg_parser.parse_args()

print(args)

# arg_parser.add_argument(
#     "-c",
#     "--client",
#     type=str,
#     required=False,
#     choices=list(srv.config.keys()),
#     default=TM_DEFAULT_CLIENT,
#     help="provide simplified client name.",
# )
#
# arg_parser.add_argument(
#     "-d",
#     "--data-file",
#     type=Path,
#     action=ExistingFile,
#     required=False,
#     default=BASE_DIR / "data" / "sample_data.json",
#     help="provide path to the JSON input data file.",
# )
#
# arg_parser.add_argument(
#     "-t",
#     "--target-directory",
#     help="provide target directory path where generated reports will be saved.",
#     type=Path,
#     action=ExistingWritableDir,
#     default=BASE_DIR / "data" / CASE_REPORT_TARGET_DIR,
#     required=False,
# )
#
# arg_parser.add_argument(
#     "-l",
#     "--limit",
#     help="how many reports should be generated, when set to 0 - all.",
#     type=int,
#     default=3,
#     required=False,
# )
#
# arg_parser.add_argument(
#     "-m",
#     "--html",
#     help="generate reports in HTML format too.",
#     action="store_true",
#     default=False,
#     required=False,
# )

print(random_month())