test = {   'name': 'q1_10',
    'points': [0, 0, 4],
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure histogram_statements is an array.\n>>> import numpy as np\n>>> type(histogram_statements) == np.ndarray\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure you have set histogram_statements to an array with at least 1 number\n>>> 1 <= histogram_statements.item(0) <= 3\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> histogram_statements.item(0) == 1 and histogram_statements.item(1) == 2 and histogram_statements.item(2) == 3\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
