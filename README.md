# Community App for Abydos
## Introduction
Community App for Abydos is a Splunk wrapper for the [Abydos](https://github.com/chrislit/abydos) library.

The `abydos` streaming search command provides access to the `abydos.distance`, `abydos.fingerprint`, `abydos.phonetic`, `abydos.stemmer`, and `abydos.tokenizer` modules using default class parameters and the `dist_abs()`, `fingerprint()`, `enocde_alpha()` or `encode()`, `stem()`, and `tokenize()` functions, respectively.

See the Abydos [documentation](https://abydos.readthedocs.io/) for available algorithms. Algorithms requiring SyllabiPy, NLTK, PyLZSS, or paq are not implemented.
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

Return the Beider-Morse encordings of a single field value:

`| abydos module=phonetic algorithm=BeiderMorse field1`

Return the English stem of a single field value:

`| abydos module=stemmer algorithm=Porter field1`

Return the q-grams of a single field value:

`| abydos module=tokenizer algorithm=QGrams field1`
