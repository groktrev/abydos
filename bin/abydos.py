#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2026 Trevor Scroggins

from exec_anaconda import exec_anaconda_or_die

exec_anaconda_or_die()

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option

from AbydosWrapper import AbydosWrapper

@Configuration()
class AbydosCommand(StreamingCommand):
    module = Option(require=True)
    algorithm = Option(require=True)

    def stream(self, records):
        self.logger.debug("AbydosCommand: %s", self)

        abydos = AbydosWrapper(self.module, self.algorithm, self.fieldnames)

        for record in records:
            in_val = [record[key] for key in self.fieldnames]
            ret_val = abydos.invoke(*in_val)
            record.update({self.algorithm: ret_val})
            yield record

dispatch(AbydosCommand, sys.argv, sys.stdin, sys.stdout, __name__)

