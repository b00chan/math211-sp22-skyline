test = {   'name': 'q1_5',
    'points': [0, 0, 0, 5],
    'suites': [   {   'cases': [   {'code': '>>> len(parameters) == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> # Make sure your function is returning an array!\n>>> type(parameters) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(parameters.item(0), 0.8343076972837598)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.allclose(parameters, [0.8343077, 0.09295728, -1.56652097])\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}