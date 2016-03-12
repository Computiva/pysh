from subprocess import Popen, PIPE
import os


class Process(object):

    def __init__(self, command, argv):
        self.command_name = command
        self.argv = map(str, argv)
        self.previous_process = None

    def __or__(self, next_process):
        next_process.previous_process = self
        return next_process

    def __str__(self):
        return self.process.stdout.read()

    @property
    def process(self):
        command = [self.command_name]
        command.extend(self.argv)
        if self.previous_process:
            return Popen(command, stdin=self.previous_process.process.stdout, stdout=PIPE)
        else:
            return Popen(command, stdout=PIPE)


class Command(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, *argv):
        return Process(self.name, argv)


for directory in os.environ["PATH"].split(":"):
    for command_name in os.listdir(directory):
        globals()[command_name] = Command(command_name)
