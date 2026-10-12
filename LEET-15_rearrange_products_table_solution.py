import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    """Rearranges product prices from columns into rows.

    Criteria:
    - Convert store columns into rows.
    - Keep product_id as the identifier.
    - Exclude rows with missing prices.

    Returns:
    - DataFrame containing 'product_id', 'store', and 'price'.
    """
    # 1. Convert store columns into rows
    result = products.melt(
        id_vars=['product_id'],
        var_name='store',
        value_name='price'
    )

    # 2. Remove rows where the price is missing
    result = result.dropna(subset=['price'])

    # 3. Return the required columns
    return result[['product_id', 'store', 'price']]


if __name__ == '__main__':
    # Sample test case
    products_data = {
        'product_id': [0, 1],
        'store1': [95, 70],
        'store2': [100, None],
        'store3': [105, 80],
    }

    products_df = pd.DataFrame(products_data)

    result_df = rearrange_products_table(products_df)
    print(result_df)
