import sqlite3
import argparse
import os
from pathlib import Path

ROOT = Path('.') # dotfiles
HOME = Path(os.environ['HOME'])

con = sqlite3.connect('links.db')

with con:
    con.execute('''CREATE TABLE IF NOT EXISTS links(
                name VARCHAR UNIQUE,
                source VARCHAR UNIQUE,
                target, VARCHAR);''')

def add_link(src, target):
    os.symlink(ROOT/src, HOME/target)

def save(args):
    stmt = '''
    INSERT INTO links(name, source, target)
    VALUES (:name, :source, :target)
    RETURNING source, target;
    '''
    with con:
       res = con.execute(stmt, args)
       source, target = res.fetchone()
       add_link(source, target)

def ls(args):
    stmt = '''
    SELECT name, source, target FROM links;'''
    with con:
        res = con.execute(stmt)
        for ln in res.fetchall():
            print(ln)

def update(args):
    stmt = '''
    UPDATE links
    SET source = :source,
        target = :target
    WHERE name = :name;'''
    with con:
        con.execute(stmt, args)

def rm(args):
    stmt = '''
    DELETE FROM links
    WHERE name = :name
    RETURNING target;'''
    with con:
        res = con.execute(stmt, args)
        source, = res.fetchone()
        os.unlink(HOME/source)

def sync():
    stmt = '''
    SELECT name, source, target FROM links;'''
    with con:
        res = con.execute(stmt)
        for name, src, target in res.fetchall():
            add_link(src, target)

parser = argparse.ArgumentParser(
    prog = 'Links Management System',
    description = 'Perform CRUD operations on symlinks for the .dotfiles utility'
    )
parser.add_argument('-s', '--sync', help='Create links in the root', action='store_true')
op_parsers = parser.add_subparsers(title='operation', help='The action to perform.')
save_parser = op_parsers.add_parser('save', help='add a link to the system')
save_parser.add_argument('name', help='relative to the system')
save_parser.add_argument('source', help='path to the dotfile')
save_parser.add_argument('target', help='path to the link')
save_parser.set_defaults(func=save)
ls_parser = op_parsers.add_parser('ls', help='print the links')
ls_parser.set_defaults(func=ls)
update_parser = op_parsers.add_parser('update', help='change the source and target of link')
update_parser.add_argument('name', help='relative to the system')
update_parser.add_argument('source', help='path to the dotfile')
update_parser.add_argument('target', help='path to the link')
update_parser.set_defaults(func=update)
rm_parser = op_parsers.add_parser('rm', help='remove a link')
rm_parser.add_argument('name', help='The unique string identifier')
rm_parser.set_defaults(func=rm)

args = parser.parse_args()
if args.sync:
    sync()
else:
    args.func(vars(args))
