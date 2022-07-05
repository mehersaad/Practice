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

    d = sp.Matrix([[x**2,x*y,y**2,x,y,1]])

    for i, pt in enumerate(pts):
        p_x, p_y = pt[0], pt[1]
        d = d.row_insert(i+1, sp.Matrix([[p_x**2, p_x * p_y, p_y**2, p_x, p_y,1]]))
    
    return sp.Eq(d.det(),0)


# Some set of points
pts = [sp.Point(0, 1), sp.Point(0, 0), sp.Point(
    3 / 4, 3 / 4), sp.Point(3 / 4, 1 / 4), sp.Point(1, 1 / 2)]

print(find_conic_from_pts(pts))
