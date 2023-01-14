test = {   'name': 'q3_7',
    'points': [0, 0, 0, 1, 1, 1, 1],
    'suites': [   {   'cases': [   {'code': '>>> type(original_with_shuffled_labels) == Table\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> original_with_shuffled_labels.labels == ("Gender", "Age", "Shuffled Label")\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> original_with_shuffled_labels.num_rows == 500\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(sampled_ages.column("Gender") == original_with_shuffled_labels.column("Gender"))\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> all(sampled_ages.column("Age") == original_with_shuffled_labels.column("Age"))\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> original_with_shuffled_labels.column("Age") != original_with_shuffled_labels.column("Shuffled Label")\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> all(x in original_with_shuffled_labels.column("Shuffled Label") for x in (\'male\', \'female\'))\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}