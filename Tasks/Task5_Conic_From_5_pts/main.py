import sympy as sp

sp.init_printing()
x, y = sp.symbols('x y')


def find_conic_from_pts(pts):
    '''Function that takes a list of 5 points and returns the conic equation
    that corresponds to those points

    Returns
    -------
    Sympy equation of the conic

    '''

    # We assume the equation to be A*x**2+B*y**2+C*x*y+D*x+E*y+1=0

    d = sp.Matrix()

    for i, pt in enumerate(pts):
        p_x, p_y = pt[0], pt[1]
        d = d.row_insert(i, sp.Matrix([[p_x**2, p_y**2, p_x * p_y, p_x, p_y]]))

    d_det = d.det()
    coeff = []
    for i in range(len(pts)):
        d_coeff = d.copy()
        d_coeff.col_del(i)
        d_coeff = d_coeff.col_insert(i, sp.Matrix([-1, -1, -1, -1, -1]))
        coeff.append(d_coeff.det() / d_det)

    return sp.Eq(coeff[0] * x**2 + coeff[1] * y**2 + coeff[2] * x * y + coeff[3] * x + coeff[4] * y + 1, 0)


# Some set of points
pts = [sp.Point(1, 1), sp.Point(2, 2), sp.Point(
    3, 4), sp.Point(0, 2), sp.Point(-1, 4)]

print(find_conic_from_pts(pts))
