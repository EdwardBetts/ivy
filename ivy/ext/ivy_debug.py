# --------------------------------------------------------------------------
# This extension adds a 'debug' command to Ivy's CLI.
# --------------------------------------------------------------------------

import ivy
import sys
import shutil
import os


# Command help text.
helptext = """
Usage: %s debug [FLAGS]

  Print debug information for the current site.

Flags:
  --help                Print this command's help text and exit.

""" % os.path.basename(sys.argv[0])


# Register our new command on the 'cli' event hook.
@ivy.hooks.register('cli')
def register_tree_command(parser):
    parser.add_cmd("debug", helptext, callback)


# Command callback.
def callback(parser):

    @ivy.hooks.register('main')
    def tree_callback():
        if not ivy.site.home():
            sys.exit("Error: cannot locate the site's home directory.")

        cols, _ = shutil.get_terminal_size()

        print('-' * cols)
        print('Site: %s' % ivy.site.home())
        print('-' * cols)
        print(ivy.nodes.root().str())
        print('-' * cols)
