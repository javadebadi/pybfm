p1_irr = IRR(
    [0,1],
    [-11,12],
    [None, None]
)
p2_irr = IRR(
    [0, 0, 1, 2, 3, 4, 5, 6],
    [-5, -6, -4, -10, 1, 2, 4, 40],
    [None, None, None, None ,None, None, None, None],
)
p3_irr = IRR(
    [0, 0, 1, 2, 3],
    [-5, -6, -10, 0, 5],
    [None, None, None, None ,'perpetuity'],
)
cam_irr = IRR(
    [0, 1, 2, 3, 4],
    [-120, 48, 48, 48, 48],
    [None, None, None, None, None],
)
atr_irr = IRR(
    [0, 1, 2, 3, 4],
    [-250, 90, 90, 90, 90],
    [None, None, None, None, None],
)
multiple_irr = IRR(
    [0, 1, 2],
    [-3000, 15000, -13000],
    [None, None, None],
)
print(p1_irr)
p1_irr
p1_irr.find()
multiple_irr.find_all()
multiple_irr.get_yield_curve()
fig, ax = multiple_irr.plot(0,10)
fig.show()
