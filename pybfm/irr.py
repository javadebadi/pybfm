import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from pybfm.data_models import FormulaTuple


def generate_discounted_cash_formula(year, cf, kind=None):
    if kind is None:
        formula_string = f"{cf}/(1+r)^{year}"
        def discount_cash_formula(r):
            return cf/(1+r)**year
        return FormulaTuple(discount_cash_formula, formula_string)
    elif kind == 'perpetuity':
        formula_string = f"{cf}/r/(1+r)^{year - 1}"
        def discount_cash_formula(r):
            return cf/r/(1+r)**(year-1)
        return FormulaTuple(discount_cash_formula, formula_string)

class IRR:
    
    def __init__(self, years, cfs, kinds=None):
        if kinds is None:
            kinds = [None]*len(years)
        assert len(years) == len(cfs) and len(cfs) == len(kinds)
        self._years = years
        self._cfs = cfs
        self._kinds = kinds
        self._formula = None
        self._formula_string = None
        self._formula_tuple = self._process()
        
    @property
    def years(self):
        return self._years
    
    @property
    def cfs(self):
        return self._cfs
    
    @property
    def kinds(self):
        return self._kinds
    
    @property
    def formula(self):
        return self._formula
    
    @property
    def formula_string(self):
        return self._formula_string
    
    def _process(self):
        func_list = []
        func_string_list = []
        for year, cf, kind in zip(self.years, self.cfs, self.kinds):
            func_list.append(
                generate_discounted_cash_formula(year, cf, kind).formula
            )
            func_string_list.append(
                generate_discounted_cash_formula(year, cf, kind).formula_string
            )
        formula_string = '+'.join(func_string_list)
        def formula(r):
            return sum(f(r) for f in func_list)
        formula_tuple = FormulaTuple(formula, formula_string)
        self._formula = formula_tuple.formula
        self._formula_string = formula_tuple.formula_string
        return formula_tuple
    
    def __str__(self):
        return f"Formula = {self.formula_string}"
    
    def __repr__(self):
        s = "IRRFormula(\n"
        s += f"years={self.years},\n"
        s += f"cfs={self.cfs},\n"
        s += f"kinds={self.kinds},\n"
        s += ")"
        return s
    
    def find(self, initial_guess=0.1, precision=4):
        solution = fsolve(self._formula, initial_guess)[0]
        return round(solution, precision)
    
    def find_all(self, min_r=0, max_r=1, max_n_roots=2, precision=4):
        initial_guesses = np.linspace(min_r, max_r, max_n_roots)
        solutions = fsolve(self._formula, initial_guesses)
        solutions = [round(item, precision) for item in solutions]
        return list(set(solutions))
    
    def get_yield_curve(self, min_r=0, max_r=1, points=100):
        assert min_r < max_r
        assert type(points) == int
        xs = np.linspace(min_r, max_r, points)
        ys = self.formula(xs)
        return xs.tolist(), ys.tolist()
    
    def plot(
        self,
        min_r=0,
        max_r=1,
        points=100,
        figsize=(10,5),
        title='Yield Curve',
        plot_label='Yield',
        y_label='NPV',
        x_label='Return Rate',
        color='blue',
        x_in_percentage=True,
        grid=True,
        ):
        xs, ys = self.get_yield_curve(min_r=min_r, max_r=max_r, points=points)
        if x_in_percentage:
            xs = [100 * x for x in xs]
            xlabel = x_label + " (%)"
        fig, ax = plt.subplots(figsize=figsize)
        _ = ax.plot(xs, ys, label=plot_label, color=color)
        _ = ax.set_ylabel(y_label)
        _ = ax.set_xlabel(x_label)
        if grid is True:
            _ = ax.grid()
        return fig, ax
