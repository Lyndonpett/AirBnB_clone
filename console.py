#!/usr/bin/python3
'''Console module'''
import cmd
import models
import readline


class HBNBCommand(cmd.Cmd):
    '''Console class for builtin commands'''

    prompt = '(hbnb) '

    def do_quit(self, args):
        '''Exits the application'''
        raise SystemExit

    def do_EOF(self, args):
        '''Exits application on End of File'''
        raise SystemExit

    def emptyline(self):
        '''oryihgu'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
