import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """Filters the World DataFrame to find big countries based on area or population.

    Criteria:
    - Area >= 3,000,000 km^2
    - OR Population >= 25,000,000

    Returns:
    - DataFrame containing 'name', 'population', and 'area'.
    """
    # 1. Define boolean mask for filtering rows
    mask = (world['area'] >= 3000000) | (world['population'] >= 25000000)

    # 2. Select rows satisfying the mask and pick the required columns using .loc
    return world.loc[mask, ['name', 'population', 'area']]


if __name__ == '__main__':
    # Sample test case
    data = {
        'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
        'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
        'area': [652230, 28748, 2381741, 468, 1246700],
        'population': [25500100, 2831741, 37100000, 78115, 20609294],
        'gdp': [
            20343000000,
            12960000000,
            188681000000,
            3712000000,
            100990000000,
        ],
    }

    world_df = pd.DataFrame(data)
    result_df = big_countries(world_df)
    print(result_df)