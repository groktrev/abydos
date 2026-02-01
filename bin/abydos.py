#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2026 Trevor Scroggins

from exec_anaconda import exec_anaconda_or_die

exec_anaconda_or_die()

import os
import platform
import sys

SUPPORTED_SYSTEMS = {
    ('Linux', 'x86_64'): 'linux_x86_64',
    ('Darwin', 'x86_64'): 'darwin_x86_64',
    ('Darwin', 'arm64'): 'darwin_arm64',
    ('Windows', 'AMD64'): 'windows_x86_64',
}

if platform.system() == "Darwin" and "ARM64" in platform.version():
    system = (platform.system(), "arm64")
else:
    system = (platform.system(), platform.machine())
if system not in SUPPORTED_SYSTEMS:
    raise Exception(f'Unsupported platform: {system}')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), SUPPORTED_SYSTEMS[system], "bin"))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option

from AbydosWrapper import AbydosWrapper

@Configuration()
class AbydosCommand(StreamingCommand):
    module = Option(require=True)
    algorithm = Option(require=True)
    nltk_tokenizer = Option(require=False)

    def stream(self, records):
        self.logger.debug("AbydosCommand: %s", self)

        abydos = AbydosWrapper(self.module, self.algorithm, self.nltk_tokenizer, self.fieldnames)

        for record in records:
            in_val = [record[key] for key in self.fieldnames]
            ret_val = abydos.invoke(*in_val)
            record.update({self.algorithm: ret_val})
            yield record

dispatch(AbydosCommand, sys.argv, sys.stdin, sys.stdout, __name__)

