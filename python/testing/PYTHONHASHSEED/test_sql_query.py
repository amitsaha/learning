def create_where_clause(conditions):
    where_clause = ''
    for k, v in conditions.iteritems():
        where_clause += '%s=%s AND ' % (k, v)
    # remove the last AND and a trailing space
    return where_clause[:-5]

# This will fail for *some* PYTHONHASHSEED
def test_where_clause_1():

    where_clause = create_where_clause({'item1': 1, 'item2': 2})
    expected_where_clause = 'item1=1 AND item2=2'
    assert where_clause==expected_where_clause

# This will not fail for *any* PYTHONHASHSEED
def test_where_clause_2():

    where_clause = create_where_clause({'item1': 1, 'item2': 2})
    # Deconstruct the string returned into individual conditions
    conditions = [cond.strip() for cond in where_clause.split('AND')]
    assert 'item1=1' in conditions
    assert 'item2=2' in conditions
