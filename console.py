#!/usr/bin/python3
'''
    Define class HBNBCommand
'''


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def help_help(self):
        print("Help")

    def emptyline(self):
        pass
    def do_create():
        pass
    def do_show():
        pass
    def do_destroy():
        pass
    def do_all():
        pass
    def do_update():
        pass
    def do_quit(self, line):
        return True
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()