import pandas as pd
import numpy as np


def random_float_valued_table(n_rows, n_columns, values_type='both'):
    """

    :param n_rows: Number of rows of the table.
    :param n_columns: Number of columns of the table.
    :param values_type: Sets the type of values to be positive, negative, or both. Default both.
    :return: DataFrame with the specified number of rows, columns, and value type.
    """
    if values_type not in ['positive', 'negative', 'both']:
        raise ValueError("values_typ must be one of the following values: positive, negative or both.")
    df = pd.DataFrame()
    if values_type == 'positive':
        for i in range(1, n_columns + 1):
            values = []
            decimal_places = np.random.randint(7)
            for j in range(n_rows):
                values.append(np.round(10 ** np.random.randint(7) * np.random.random_sample(), decimal_places))
            df['column_' + str(i)] = values
    elif values_type == 'negative':
        for i in range(1, n_columns + 1):
            values = []
            decimal_places = np.random.randint(7)
            for j in range(n_rows):
                values.append((-1) * np.round(10 ** np.random.randint(7) * np.random.random_sample(), decimal_places))
            df['column_' + str(i)] = values
    elif values_type == 'both':
        for i in range(1, n_columns + 1):
            values = []
            decimal_places = np.random.randint(7)
            for j in range(n_rows):
                values.append((2 * np.random.randint(2) - 1)
                              * np.round(10 ** np.random.randint(7) * np.random.random_sample(), decimal_places))
            df['column_' + str(i)] = values
    return df
