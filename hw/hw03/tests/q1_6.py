test = {   'name': 'q1_6',
    'points': [0, 1, 1, 2],
    'suites': [   {   'cases': [   {   'code': '>>> pter_over_time.take(0)\nDate       | NEI     | NEI-PTER | Year | PTER\n1994-01-01 | 10.0974 | 11.172   | 1994 | 1.0746',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> np.all(pter_over_time.column("PTER") == pter)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> np.all(pter_over_time.column("Year") == year)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': ">>> pter_over_time.labels\n('Date', 'NEI', 'NEI-PTER', 'Year', 'PTER')", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
