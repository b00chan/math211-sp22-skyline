test = {   'name': 'q3_0',
    'points': [0, 0, 0, 0.75, 0.75, 0.75, 0.75],
    'suites': [   {   'cases': [   {'code': '>>> 0.0 <= distance_first_to_second <= 0.1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(distance(make_array(1, 2), make_array(1, 2)), 0)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(distance(make_array(1, 2, 3), make_array(2, 4, 5)), 3)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(round(distance_first_to_second, 5), 0.03335)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> a1 = np.array([1, 2, 3])\n>>> a2 = np.array([3, 4, 5])\n>>> np.isclose(round(distance(a1, a2), 4), 3.4641)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> a2 = np.array([3, 4, 5])\n>>> a3 = np.array([9, 5, 4])\n>>> np.isclose(round(distance(a2, a3), 4), 6.1644)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> a1 = np.array([1, 2, 3])\n>>> a3 = np.array([9, 5, 4])\n>>> np.isclose(round(distance(a1, a3), 4), 8.6023)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
