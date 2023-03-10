test = {   'name': 'q2_2',
    'points': [0, 0, 0, 4],
    'suites': [   {   'cases': [   {   'code': ">>> # Check your column labels and spelling\n>>> recent_poverty_total.labels == ('geo', 'poverty_percent', 'population_total', 'poverty_total')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # Careful, the population of Australia in 2010 was 22,154,687\n>>> recent_poverty_total.where('geo', 'aus').column(2).item(0)\n22154687",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The number of people estimated to be living in extreme poverty\n'
                                               ">>> # in Australia should be 301,304. That's 22,154,687 * 0.0136\n"
                                               '>>> # rounded to the nearest integer.\n'
                                               ">>> float(recent_poverty_total.where('geo', 'aus').column(3).item(0))\n"
                                               '301304.0',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> sum(recent_poverty_total.column(3))\n990049954.0', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
