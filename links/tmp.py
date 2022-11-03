import argparse
import csv
from pkg_resources import resource_filename

DB = resource_filename(__name__, 'links.csv')

def save(args):
    print(f'Saving {args.id}')
    with open(DB, 'w') as db:
        db_writer = csv.writer(db)
        db_writer.writerow([args.id, args.source, args.target])

def ls(args):
    print(f'Environment Variables')
    print(f'ID | SRC | Target')
    with open(DB, 'r') as db:
        db_reader = csv.reader(db)
        for row in db_reader:
            print(' | '.join(row))

def update(args):
    print(f'Updating {args.id}')
    line_num = None
    with open(DB, 'r') as db:
        db_reader = csv.reader(db)
        for row in db_reader:
            if row[0] == args.id:
                line_num = db_reader.line_num

    if line_num is not None:
        with open(DB, 'w') as db:
            

parser = argparse.ArgumentParser(
    prog = 'Links Management System',
    description = 'Perform CRUD operations on links (hard) for the .dotfiles utility'
    )
op_parsers = parser.add_subparsers(title='operation')
save_parser = op_parsers.add_parser('save')
save_parser.add_argument('id')
save_parser.add_argument('source')
save_parser.add_argument('target')
save_parser.set_defaults(func=save)
ls_parser = op_parsers.add_parser('ls')
ls_parser.set_defaults(func=ls)
update_parser = op_parsers.add_parser('update')
update_parser.add_argument('id')
update_parser.set_defaults(func=update)
args = parser.parse_args()
args.func(args)
