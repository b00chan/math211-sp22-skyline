test = {   'name': 'q1_13',
    'points': [0, 0, 0, 4],
    'suites': [   {   'cases': [   {'code': ">>> # Check your column labels and spelling\n>>> region_counts.labels == ('region', 'count')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> # Counts must sum to 50\n>>> sum(region_counts.column('count')) == 50\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> list(region_counts.sort("count").column("count"))\n[5, 7, 8, 9, 10, 11]', 'hidden': True, 'locked': False},
                                   {   'code': '>>> print(list(region_counts.sort("count").column("region")))\n'
                                               "['south_asia', 'middle_east_north_africa', 'america', 'east_asia_pacific', 'europe_central_asia', 'sub_saharan_africa']\n",
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
