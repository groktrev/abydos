#!/usr/bin/env python
# coding=utf-8
#
# Copyright © 2026  Trevor Scroggins

from exec_anaconda import exec_anaconda_or_die

exec_anaconda_or_die()

import importlib
import os
import sys

import numpy

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option

@Configuration()
class AbydosCommand(StreamingCommand):
    modules = [
        "distance",
        "fingerprint",
        "phonetic",
        "stemmer",
        "tokenizer"
    ]

    module = Option(require=True)
    algorithm = Option(require=True)

    def stream(self, records):
        self.logger.debug("AbydosCommand: %s", self)

        cls = None
        func = None

        if self.module not in self.modules:
            raise ValueError(f"{self.module} is not a supported module")

        module = importlib.import_module(f".{self.module}", package="abydos")

        if not (hasattr(module, self.algorithm) and callable(getattr(module, self.algorithm))):
            raise ValueError(f"{self.algorithm} is not a valid alogrithm in {self.module}")

        cls = getattr(module, self.algorithm)()

        if self.module == "distance":
            if len(self.fieldnames) != 2:
                raise ValueError("distance alogrithms take two fields as input")

            func = getattr(cls, "dist")

        elif self.module == "fingerprint":
            if len(self.fieldnames) != 1:
                raise ValueError("fingerprint alogrithms take one field as input")

            func = getattr(cls, "fingerprint")

        elif self.module == "phonetic":
            if len(self.fieldnames) != 1:
                raise ValueError("phonetic alogrithms take one field as input")

            if (hasattr(cls, "encode_alpha")):
                func = getattr(cls, "encode_alpha")
            else:
                func = getattr(cls, "encode")

        elif self.module == "stemmer":
            if len(self.fieldnames) != 1:
                raise ValueError("stemmer alogrithms take one field as input")

            func = getattr(cls, "stem")

        elif self.module == "tokenizer":
            if len(self.fieldnames) != 1:
                raise ValueError("tokenizer alogrithms take one field as input")

            func = getattr(cls, "tokenize")

        else:
            raise ValueError(f"{self.module} is not impelemented")

        for record in records:
            in_val = [record[key] for key in self.fieldnames]
            ret_val = func(*in_val)
            record.update({self.algorithm: ret_val})
            yield record

dispatch(AbydosCommand, sys.argv, sys.stdin, sys.stdout, __name__)

