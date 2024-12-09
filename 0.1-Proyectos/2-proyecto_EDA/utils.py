def update_release_years(df, release_years_dict):
  """
  Updates the 'Year' column of a DataFrame based on a dictionary of game id's and their release years.

  Args:
    df: The DataFrame to be updated.
    release_years_dict: A dictionary mapping game rank to their release years.

  Returns:
    The updated DataFrame.
  """

  for n in df.index:
    if n in release_years_dict.keys():
        df.at[n, 'Year'] = release_years_dict[n]
#   return df


def update_publisher(df, publisher_data):
  """
  Updates the 'Publisher' column of a DataFrame based on a dictionary of game id's and their publishers name.

  Args:
    df: The DataFrame to be updated.
    publisher_data: A dictionary mapping game rank to their release years.

  Returns:
    The updated DataFrame.
  """

  for n in df.index:
    if n in publisher_data.keys():
        df.at[n, 'Publisher'] = publisher_data[n]
#   return df

