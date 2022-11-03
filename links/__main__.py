import sqlite3
import argparse

con = sqlite3.connect('links.db')

with con:
    con.execute('''CREATE TABLE IF NOT EXISTS links(
                id INTEGER PRIMARY KEY,
                name VARCHAR UNIQUE,
                source VARCHAR,
                target, VARCHAR);''')

def save(args):
    stmt = '''
    INSERT INTO links(name, source, target)
    VALUES (:name, :source, :target);
    '''
    with con:
       con.execute(stmt, args)

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
    WHERE name = :name;'''
    with con:
        con.execute(stmt, args)

def generate(args):
    stmt = '''
    SELECT name, source, target FROM links;'''
    links = []
    with con:
        res = con.execute(stmt)
        links.extend(res.fetchall())
    # use the os module to create each target from source
    for _id, name, source, target in links:
        pass

parser = argparse.ArgumentParser(
    prog = 'Links Management System',
    description = 'Perform CRUD operations on links (hard) for the .dotfiles utility'
    )
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
args.func(vars(args))
