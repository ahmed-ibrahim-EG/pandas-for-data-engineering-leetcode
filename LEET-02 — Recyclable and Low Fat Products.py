import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """Filters the Products DataFrame to find products that are both
    low fat and recyclable.

    Criteria:
    - low_fats = 'Y'
    - recyclable = 'Y'

    Returns:
    - DataFrame containing 'product_id'.
    """
    # 1. Define boolean mask for filtering rows
    mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')

    # 2. Select rows satisfying the mask and pick the required column using .loc
    return products.loc[mask, ['product_id']]
