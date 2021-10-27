#!/usr/bin/python3
'''Console module'''
import cmd
import models
import readline


class HBNBCommand(cmd.Cmd):
    '''Console class for builtin commands'''

    prompt = '(hbnb) '

    def do_quit(self, args):
        '''quit:
        Exits the application
        '''
        models.storage.save()
        raise SystemExit

    def do_EOF(self, args):
        '''EOF:
        Exits application on End of File
        '''
        models.storage.save()
        raise SystemExit

    def emptyline(self):
        '''Handles emptyline'''
        pass

    def do_create(self, args):
        '''create:
        Creates a BaseModel object, Saves it to JSON file, and Prints the id
        '''
        if not args:
            print('** class name missing **')
            return

        try:
            thing = getattr(models, args)()
            models.storage.new(thing)
            print(thing.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''show:
        Print the __str__ of an object by class & id
        '''
        arg_list = args.split(' ')
        if not args:
            return print('** class name missing **')

        try:
            getattr(models, args.split(' ')[0])
        except:
            return print("** class doesn't exist **")

        if len(arg_list) < 2:
            return print('** instance id missing **')

        try:
            print(str(
                models.storage.all()['.'.join(i for i in args.split(' '))]))
        except:
            print('** no instance found **')

    def do_destroy(self, args):
        '''destoy:
        Delete an instance of an object by class & id
        '''
        arg_list = args.split(' ')
        if not args:
            return print('** class name missing **')

        try:
            getattr(models, args.split(' ')[0])
        except:
            return print("** class doesn't exist **")

        if len(arg_list) < 2:
            return print('** instance id missing **')

        try:
            del models.storage.all()['.'.join(i for i in args.split(' '))]
        except:
            print('** no instance found **')

    def do_all(self, args):
        if args:
            try:
                getattr(models, args.split(' ')[0])
            except:
                return print("** class doesn't exist **")

        print([str(models.storage.all()[key]) for key in models.storage.all()])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
