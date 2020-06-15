#!/usr/bin/env ipython
import os
import ncs
import sys
import logging
import subprocess
import IPython as ipy
from IPython.terminal.interactiveshell import TerminalInteractiveShell as ipy_shell


OPER = {
    1: 'MOP_CREATED',
    2: 'MOP_DELETED',
    3: 'MOP_MODIFIED',
    4: 'MOP_VALUE_SET',
    5: 'MOP_MOVED_AFTER',
    6: 'MOP_ATTR_SET'
}

class DiffIterator(object):
     def __init__(self):
         self.count = 0
     def __call__(self, kp, op, oldv, newv):
         print('kp={0}, op={1}, oldv={2}, newv={3}'.format(
                 str(kp), OPER[op], str(oldv), str(newv)))
         self.count += 1
         return ncs.ITER_RECURSE

def compare(self):
    print("Diff set:")
    self.diff_iterate(DiffIterator(), ncs.ITER_WANT_ATTR)

class NcsPycli:
    name = 'ncs_pycli'
    command = ['ipython']
    options = []
    version = '1.1.0'

    __stdout = subprocess.PIPE
    __stderr = subprocess.PIPE

    def __init__(self, log_level=logging.INFO, log_format=None, *args, **kwargs):
        # logger setup
        self.__format = log_format
        self.logger = self.__set_logger_level(log_level)
    
    def __set_logger_level(self, log_level):
        if self.__format is None:
            self.__format = '[ %(levelname)s ] :: [ %(name)s ] :: %(message)s'
        logging.basicConfig(stream=sys.stdout, level=log_level,
                            format=self.__format, datefmt=None)
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        return logger

    def __run_command(self, command):
        self.logger.debug("command `{}` running on terminal".format(' '.join(command)))
        p = subprocess.Popen(command, stdout=self.__stdout, stderr=self.__stderr)
        out, err = p.communicate()
        out, err = out.decode('utf-8'), err.decode('utf-8')
        if err == '':
            self.logger.debug("`{}` ran successfully".format(' '.join(command)))
            return out
        self.logger.error("command issue: {}".format(err))
        self.__exit

    @property
    def __exit(self):
        sys.exit()

    def _create_profile(self):
        self.command += ['profile', 'create']
        self.logger.info('creating ipython profile')
        out = self.__run_command(self.command)
        if out is None or out == '':
            self.logger.info("couldn't able to create an ipython instance.")
            self.__exit

    def _get_shell(self):
        if ipy.get_ipython() is None:
            shell = ipy_shell.instance()
            if shell is None:
                self._create_profile()
                self._get_shell()
            shell.user_ns['shell'] = shell
        return ipy.get_ipython()

    def initialize(self):
        ncs.maapi.Transaction.compare = compare
        shell = self._get_shell()
        shell.define_macro('new_trans', """trans=m.start_write_trans()
root = ncs.maagic.get_root(trans)
print("new transaction created")
""")
        m = ncs.maapi.Maapi()
        m.start_user_session('admin', 'system', [])
        trans = m.start_write_trans()
        root = ncs.maagic.get_root(trans)
        new_trans = shell.user_ns['new_trans']

        print("Your maagic object 'root -> %s' is now prepared... go have some fun!\ntrans.compare() to see your current transaction\ntrans.apply() to commit\ntrans.revert() to revert changes\nMaapi object can be found at m" % (str(root)))
        print("""You can restart the transaction and create a fresh root object by invoking new_trans:
In [1]: new_trans
new transaction created""")
        ipy.embed(display_banner=False, config=shell.config)

def run():
    obj = NcsPycli()
    obj.initialize()


if __name__ == '__main__':
    run()
