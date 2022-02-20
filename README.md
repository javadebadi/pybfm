# PYBFM
**PYBFM** is an open-source python libraray which implements functions and classes that can be used in Business or Corporate Financial Management.

### Internal Rate of Return (IRR)
Calculating the Internal Rate of Return is very commont in project appraisal.
```Python
>>> multiple_irr = IRR(
    [0, 1, 2],
    [-3000, 15000, -13000],
    [None, None, None],
)
>>> irr = multiple_irr.find()
```
