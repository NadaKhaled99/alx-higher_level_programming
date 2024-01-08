#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    ll = len(m_a)
    if ll == 0:
        raise ValueError("m_a can't be empty")
    lll = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if lll is None:
            lll = len(i)
            if lll == 0:
                raise ValueError("m_a can't be empty")
        if lll != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    llll = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if llll is None:
            llll = len(i)
            if llll == 0:
                raise ValueError("m_b can't be empty")
        if llll != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if lll != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(ll):
        l = []
        for j in range(llll):
            n = 0
            for k in range(lll):
                n += m_a[i][k] * m_b[k][j]
            l.append(n)
        matrix.append(l)
    return matrix
