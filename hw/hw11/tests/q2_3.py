test = {   'name': 'q2_3',
    'points': [0, 8],
    'suites': [   {   'cases': [   {   'code': '>>> len(compute_resampled_line(Table().with_columns(\'x\', make_array(0, 1), \'y\', make_array(1, 3)), "x", "y")) == 2\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(0)\n>>> np.allclose(compute_resampled_line(birds, "Egg Weight", "Bird Weight"), np.array([0.64163345, 0.53766856]))\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}