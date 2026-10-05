import pandas as pd


def find_customers(
    customers: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
  """Filters the Customers DataFrame to find customers who never placed an order.

  Criteria:
  - customers.id NOT IN orders.customerId

  Returns:
  - DataFrame containing 'Customers' (renamed from 'name').
  """
  # 1. Define boolean mask using isin and negation operator (~)
  mask = ~customers['id'].isin(orders['customerId'])

  # 2. Select matching rows and pick the required column using .loc
  result = customers.loc[mask, ['name']]

  # 3. Rename column to match required output format
  return result.rename(columns={'name': 'Customers'})
