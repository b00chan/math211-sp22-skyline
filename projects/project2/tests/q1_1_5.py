test = {   'name': 'q1_1_5',
    'points': [0, 0, 1, 1, 2],
    'suites': [   {   'cases': [   {'code': '>>> len(cities.labels) == 8\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> cities.labels[-1] == "Region"\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> cities.row(0).item('Region') == 'Northwest'\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(np.sort(cities.group('Region').column('Region')) == make_array('Northeast', 'Northwest', 'Southeast', 'Southwest'))\nTrue",
                                       'hidden': True,
                                       'locked': False},
                                   {'code': ">>> np.all(cities.group('Region').column('count') == make_array(149,  62, 203,  47))\nTrue", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
