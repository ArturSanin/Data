import pandas as pd
import numpy as np
import pathlib
import os


def random_integer_table_to_csv(n_rows, n_columns, values_type='both'):
    """

    :param n_rows: Number of rows of the table.
    :param n_columns: Number of columns of the table.
    :param values_type: Sets the type of values to be positive, negative, or both. Default both.
    :return: Creates a csv-File in the directory csv_files.
    """
    if values_type not in ['positive', 'negative', 'both']:
        raise ValueError("values_typ must be one of the following values: positive, negative or both.")
    df = pd.DataFrame()
    if values_type == 'positive':
        for i in range(1, n_columns + 1):
            values = []
            r = 10 ** np.random.randint(1, 7)
            for j in range(n_rows):
                values.append(np.random.randint(r))
            df['column_' + str(i)] = values
    elif values_type == 'negative':
        for i in range(1, n_columns + 1):
            values = []
            r = 10 ** np.random.randint(1, 7)
            for j in range(n_rows):
                values.append((-1) * np.random.randint(r))
            df['column_' + str(i)] = values
    elif values_type == 'both':
        for i in range(1, n_columns + 1):
            values = []
            r = 10 ** np.random.randint(1, 7)
            for j in range(n_rows):
                values.append((2 * np.random.randint(2) - 1) * np.random.randint(r))
            df['column_' + str(i)] = values
    pathlib.Path(os.getcwd() + '/csv_files').mkdir(parents=True, exist_ok=True)
    lst = os.listdir(os.getcwd() + '/csv_files')
    df.to_csv(os.getcwd() + '/csv_files' + '/integer_table_' + str(len(lst) + 1) + '.csv', index=False)
