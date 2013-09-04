import argparse
import sys
import csv
import urllib2

from settings import settings


def fetch_page(tec_id):
    return urllib2.urlopen('http://204.65.203.5/public/{0}noadd.csv'.format(str(tec_id)))


def prepare_rows(page):
    return csv.reader(page)


def get_data(filing_id, type, basic=False, cli=False):
    page = fetch_page(filing_id)
    rows = prepare_rows(page)

    row_list = []

    header_row = settings[type]['full_pull']['header']
    indexes = settings[type]['full_pull']['indexes']
    type_code = settings[type]['type_code']

    if basic:
        header_row = settings[type]['basic_pull']['header']
        indexes = settings[type]['basic_pull']['indexes']

    for row in rows:
        if not row:
            continue

        if row[0] == type_code:
            row = [row[x] for x in indexes]
            row_list.append(row)

    if cli:
        write_to = csv.writer(sys.stdout)
        write_to.writerow(header_row)

        for row in row_list:
            write_to.writerow(row)
    else:
        return [dict(zip(header_row, x)) for x in row_list]


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('filing_id', help='TEC filing ID')
    parser.add_argument('-t', '--type',
                        help='The type of data you want to get',
                        choices=['contributions', 'expenditures'])
    parser.add_argument('-s', '--simple',
                        help='Return just the basic fields, good if you just want numbers',
                        action='store_true')
    args = parser.parse_args()

    if not args.type:
        parser.error('No data type provided, please supply a --type')

    basic_status = args.simple

    get_data(args.filing_id, args.type, basic_status, True)


if __name__ == '__main__':
    main()
