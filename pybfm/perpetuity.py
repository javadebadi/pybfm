"""Module to calculate Present Value of Perpetuity Formula
"""

def perpetuity_present_value(
  continuous_cash_payment: float,
  interest_rate: float,
):
  """Returns the Present Value of Perpetuity Formula.
  
  Parameters
  ----------
  continuous_cash_payment : float
      Amount of continuous cash payment.
      
  interest_rate : float
      Interest rate, yield or discount rate.
      
  Returns
  -------
  float:
      Present value of perpetuity
  """
  return continuous_cash_payment / interest_rate
