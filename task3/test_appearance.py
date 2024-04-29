from appearance import appearance


def test_appearance_default_1():
    test = {'intervals': {'lesson': [1594663200, 1594666800],
                          'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                          'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
            'answer': 3117
            }

    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer']


def test_appearance_default_2():
    test = {'intervals': {'lesson': [1594702800, 1594706400],
                          'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                                    1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                                    1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                                    1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                          'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
            'answer': 3577
            }

    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer']


def test_appearance_default_3():
    test = {'intervals': {'lesson': [1594692000, 1594695600],
                          'pupil': [1594692033, 1594696347],
                          'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
            'answer': 3565
            }

    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer']


def test_appearance_my_1():
    test = {
        'intervals': {
            'lesson': [0, 9],
            'pupil': [0, 2, 4, 6, 7, 9],
            'tutor': [0, 9],
        },
        'answer': 6,
    }

    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer']


def test_appearance_my_out_of_bounds():
    test = {
        'intervals': {
            'lesson': [0, 9],
            'pupil': [-200, 2, 4, 9, 7, 900],
            'tutor': [0, 4, 5, 9],
        },
        'answer': 6,
    }

    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer']


def test_appearance_my_zero_intersection():
    test = {
        'intervals': {
            'lesson': [0, 9],
            'pupil': [3, 5],
            'tutor': [0, 3, 5, 9],
        },
        'answer': 0,
    }

    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer']


def test_appearance_my_3():
    test = {
        'intervals': {
            'lesson': [0, 9],
            'pupil': [0, 0, 1, 1, 2, 2, 9, 9],
            'tutor': [0, 9],
        },
        'answer': 0,
    }

    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer']