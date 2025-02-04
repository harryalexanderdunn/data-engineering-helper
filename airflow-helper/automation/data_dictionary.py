from google.cloud import bigquery


def bq_to_df(project, dataset, table, columns):
    """
    Extracts table from BigQuery and returns a dataframe of the table

    Args:
        project (str): project location of table
        dataset (str): dataset location of table
        table (str): table name of table
        columns (str): columns to be extracted from table (split by comma)

    Returns:
        df (dataframe): dataframe of data within table for specified columns
    """
    client = bigquery.Client()
    sql = f"SELECT {columns} FROM `{project}.{dataset}.{table}`"
    df = client.query(sql).to_dataframe()
    return df


def create_md_file_from_string(string, filename):
    """
    creates or opens a file based on a file name and writes/overwrites the data within the file with from the string input

    Args:
        string (str): string to be written into the file
        filename (str): name and location of file to be written to
    """
    with open(filename, "w") as file:
        file.write(string)


def extract_information_schema_to_markdown(project, dataset):
    """
    Extract the information schema from BQ and translate to markdown
    
    Args:
        project (str): project location of table
        dataset (str): dataset location of table
    """
    columns = "table_name, column_name, data_type, description, collation_name, rounding_mode"
    table = "INFORMATION_SCHEMA.COLUMN_FIELD_PATHS"

    df = bq_to_df(project, dataset, table, columns)
    tables = df["table_name"].unique()
    md_string = f"# {dataset} \n \n## Data Dictionary for {dataset} in {project} \n"
    for t in tables:
        filtered_df = df.loc[df["table_name"] == t]
        filtered_df = filtered_df.reset_index(drop=True)
        table_string = filtered_df.to_markdown()
        md_string = md_string + "\n" + f"### {t}" + "\n" + table_string + "\n"
    create_md_file_from_string(md_string, f"docs/data_dictionary/{dataset}.md")


if __name__ == "__main__":
    extract_information_schema_to_markdown('gcp-project', 'dataset')
