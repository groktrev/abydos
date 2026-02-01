# Community App for Abydos

Copyright (c) 2026 Trevor Scroggins\
Abydos Copyright (c) 2014-2020 Christopher C. Little\
SyllabiPy Copyright (c) 2016 Alex Estes and Christopher Hench\
Natural Language Toolkit (NLTK) Copyright (c) 2001-2025 NLTK Project\
Punkt by Tibor Kiss and Jan Strunk\
Splunk Enterprise SDK for Python Copyright (c) 2011-2024 Splunk Inc.\
Python for Scientific Computing Copyright (c) 2015-2019 Splunk Inc.

## Introduction

Community App for Abydos is a Splunk wrapper for the [Abydos](https://github.com/chrislit/abydos) library.

The `abydos` streaming search command provides access to the `abydos.distance`, `abydos.fingerprint`, `abydos.phonetic`, `abydos.stemmer`, and `abydos.tokenizer` modules using default class parameters and the `dist_abs()`, `fingerprint()`, `enocde_alpha()` or `encode()`, `stem()`, and `tokenize()` functions, respectively.

See the Abydos [documentation](https://abydos.readthedocs.io/) for available algorithms.

Limited support for `abydos.tokenizer.NLTKTokenizer` NLTK tokenizers is available. See the nltk.tokenize [documentation](https://www.nltk.org/api/nltk.tokenize.html) for available tokenizers.

`abydos.distance.NCDlzss`, and `abydos.distance.NCDpaq9a` are not implemented.

## Requirements

Community App for Abydos requires a non-EOL version of Splunk Enterprise and Python for Scientific Computing:

- [Python for Scientific Computing (for Linux 64-bit)](https://splunkbase.splunk.com/app/2882)
- [Python for Scientific Computing (for Mac Apple Silicon)](https://splunkbase.splunk.com/app/6785)
- [Python for Scientific Computing (for Mac Intel)](https://splunkbase.splunk.com/app/2881)
- [Python for Scientific Computing (for Windows 64-bit)](https://splunkbase.splunk.com/app/2883)

## Examples

Return the Levenshtein distance between two field values:

`| abydos module=distance algorithm=Levenshtein field1 field2`

Return the skeleton key string fingerprint of a single field value:

`| abydos module=fingerprint algorithm=SkeletonKey field1`

Return the Beider-Morse encodings of a single field value:

`| abydos module=phonetic algorithm=BeiderMorse field1`

Return the English stem of a single field value:

`| abydos module=stemmer algorithm=Porter field1`

Return the q-grams of a single field value:

`| abydos module=tokenizer algorithm=QGrams field1`

Return sentences using the NLTK Punkt Sentence Tokenizer:

`| abydos module=tokenizer algorithm=NLTKTokenizer nltk_tokenizer=PunktSentenceTokenizer field1`

## References

Tibor Kiss and Jan Strunk. 2006. [Unsupervised Multilingual Sentence Boundary Detection](https://aclanthology.org/J06-4003/). *Computational Linguistics*, 32(4):485–525.
