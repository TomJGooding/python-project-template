import project_name


def test_add():
    assert project_name.add(3, 4) == 7
    assert project_name.add(3.5, 4) == 7
    assert project_name.add(3.9, 4) == 7
    assert project_name.add(3.9, 4.1) == 8


def test_to_sentence():
    assert project_name.to_sentence('apple') == 'Apple.'
    assert project_name.to_sentence('Apple trees') == 'Apple trees.'
    assert project_name.to_sentence('Apple trees.') == 'Apple trees.'
