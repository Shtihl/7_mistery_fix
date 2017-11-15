from math import sqrt


def get_roots(coef_a, coef_b, coef_c):
    discriminant = coef_b ** 2 - 4 * coef_a * coef_c
    if discriminant >= 0:
        root1 = (-coef_b - sqrt(discriminant)) / (2 * coef_a)
        root2 = None
        if discriminant > 0:
            root2 = (-coef_b + sqrt(discriminant)) / (2 * coef_a)
        return root1, root2
    else:
        return None, None

