#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2026 Trevor Scroggins

import importlib
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
os.environ["NLTK_DATA"] = os.path.join(os.path.dirname(__file__), "..", "usr", "share", "nltk_data")

import nltk

class AbydosWrapper(object):
    _module_names = {
        # "module": num_args
        "distance": 2,
        "fingerprint": 1,
        "phonetic": 1,
        "stemmer": 1,
        "tokenizer": 1
    }

    _module_name = None
    _algorithm = None
    _nltk_tokenizer = None

    def __init__(self, module_name=None, algorithm_name=None, nltk_tokenizer_name=None, fieldnames=None):
        if module_name not in self._module_names:
            raise ValueError(f"{module_name} is not a supported module")

        self._module_name = module_name
        module = importlib.import_module(f".{module_name}", package="abydos")
        
        if not (hasattr(module, algorithm_name) and callable(getattr(module, algorithm_name))):
            raise ValueError(f"{algorithm_name} is not a valid alogrithm in {module_name}")

        if algorithm_name != "NLTKTokenizer" and nltk_tokenizer_name is not None:
            raise TypeError("nltk_tokenizer must be used with the NLTKTokenizer algorithm")

        if algorithm_name == "NLTKTokenizer":
            self._nltk_tokenizer = getattr(nltk.tokenize, nltk_tokenizer_name)()
            self._algorithm = getattr(module, "NLTKTokenizer")(self._nltk_tokenizer)
        else:
            self._algorithm = getattr(module, algorithm_name)()

    def invoke(self, *args):
        if len(args) != self._module_names[self._module_name]:
            raise TypeError(f"{self._module_name} algorithms take {self._module_names[self._module_name]} field(s) as input")

        return getattr(self, f"{self._module_name}")(*args)

    def distance(self, *args):
        return self._algorithm.dist_abs(*args)

    def fingerprint(self, *args):
        return self._algorithm.fingerprint(*args)

    def phonetic(self, *args):
        return self._algorithm.encode_alpha(*args)

    def stemmer(self, *args):
        return self._algorithm.stem(*args)

    def tokenizer(self, *args):
        if self._algorithm.__class__.__name__ == "NLTKTokenizer":
            return self._algorithm.__class__(self._nltk_tokenizer).tokenize(*args)
        else:
            return self._algorithm.__class__().tokenize(*args)

