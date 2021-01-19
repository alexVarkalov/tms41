from funcs.funcs_02 import (
    create_matrix,
    get_max_elem,
    get_min_elem,
    get_mutrix_sum,
)


def test_create_matrix():
    matrix = create_matrix(3, 4, 1, 9)
    assert len(matrix) == 3
    for i in range(3):
        assert len(matrix[i]) == 4
        for j in range(4):
            assert isinstance(matrix[i][j], int)
            assert matrix[i][j] > 0
            assert matrix[i][j] < 10


def test_get_max_elem_positive():
    matrix = [[1, 2], [5, 3]]
    result = get_max_elem(matrix)
    assert result == 5


def test_get_max_elem_negative():
    matrix = [[-1, -2], [-5, -3]]
    result = get_max_elem(matrix)
    assert result == -1


def test_get_min_elem_positive():
    matrix = [[1, 2], [5, 3]]
    result = get_min_elem(matrix)
    assert result == 1


def test_get_min_elem_negative():
    matrix = [[-1, -2], [-5, -3]]
    result = get_min_elem(matrix)
    assert result == -5


def test_get_matrix_sum():
    matrix = [[-1, -2], [-5, -3]]
    result = get_mutrix_sum(matrix)
    assert result == -11
