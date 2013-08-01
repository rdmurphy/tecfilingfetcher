TEC Filing Fetcher
==================

Fetching TEC filing data made easy!

How it works
------------

Pretty straightforward:

::

    usage: fetchfiling [-h] [-t {contributions,expenditures}] [-s] filing_id

    positional arguments:
      filing_id             TEC filing ID

    optional arguments:
      -h, --help            show this help message and exit
      -t {contributions,expenditures}, --type {contributions,expenditures}
                            The type of data you want to get
      -s, --simple          Return just the basic fields, good if you just want
                            numbers
