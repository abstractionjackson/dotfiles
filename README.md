# dotfiles
macOS system config
![meme](https://imgflip.com/i/6zg05)

## What
The dotfiles application is designed to manage system configuration.
The CLI provides symlink management, while the repository houses configuration data, in the form of dotfiles.
Much of your software depends on configuration for behavior, and if your machine changes (say, you upgrade the laptop) then __.dotfiles__ can help retain the preferences, settings, and configuration variables from the previous machines.

## How
Programs often create these config files (hereafter "dotfiles") when installed, or -- perhaps -- you created them when setting up a program. In order to consolidate dotfiles for migration and general management, yet make them available to the program in question, it is sometimes necessary to tell the program where they now live. It may instead be necessary to place a link from where the program _expects_ the dotfile to be, and where it is being managed. __dotfiles__ can do both.

### The Former: ENV Variables
This feature is still in development

### The Latter: Symbolic Links
`dotfiles ln` (working call `links`) includes features that manage links between the application and the operationg system, and -- by extension -- the programs that use dotfiles.
- Save: place a link in the operating system home directory, where programs typically start to look for them
- List: view the current links
- Update: change the path the link, or dotfile
- Remove: unlink a dotfile
- Sync: add all links to the home directory

#### Use
Links is a python package, and -- as such -- may be executed from a terminal (you've got python installed, right?i OK, whew...). Simply cd into the __.dotfiles__ directory, and run:
```zsh
python links save <name> <src> <target>```
Wow! You created a link in the home directory of your machine! If you hadn't a dotfile on the target path, nor a program expecting to read from the source, it won't do a whole lot, but still... 'atta boy!

## Next
__.dotfiles__ development, testing, and documentation continues. Other than adding ENV var management, expect a start script that installs those programs you know and love. For the latest updates, refer to a [live](https://trello.com/b/a06gi7q0/dotfile) project board on Trello.

## Thanks
__.dotfiles__ is inspired by a [project](https://github.com/eieioxyz/dotfiles_maco) [GitHub@eieioxyz](https://github.com/eieioxyz) put together.

## Author
Jackson Galan

## License
MIT
