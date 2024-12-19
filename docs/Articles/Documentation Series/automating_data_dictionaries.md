---
title: Automating Data Dictionary creation and maintenance
description: Technical overview of how to add data dictionary creation/maintenance to your pipelines. This allows you to have up to date data dictionaries in your centralised documentation based on your production pipelines
authors: Harry Dunn
created: 2024-03-19
---

# Automating Data Dictionary creation and maintenance

Nobody wants to spend all their time writing documentation, so lets make some code to do it for you. I have written a script which takes tables from any bigquery dataset (that you have access to) and generates a data dictionary for each table in the dataset within a single md file. If you display this in a centralised site such as Mkdocs you can then split your data dictionaries by dataset and they are all easily searchable through the search bar on Mkdocs. This makes looking at data very powerful as its easy to search for certain key words over many different projects.

Please see my previous [article](../Documentation%20Series/central_docs_methodology.md) for more information on setting up a centralised documentation site.

## How it works

This is specifically for extracting data information out of bigquery and displaying it as a data dictionary within a central documentation site.

1. **You need to ensure your columns descriptions are labelled appropriately**. See here for information on how to do this within dataform: [Centralising & Automating Dataform Column Descriptions](../Dataform/dataform_column_descriptions.md).
2. You need to have access to the appropriate tables and access to the metadata tables: "INFORMATION_SCHEMA.COLUMN_FIELD_PATHS"
3. If your table schemas or descriptions change you will need to rerun this code and push to the repo.
4. Have pandas & google-cloud-bigquery installed to use the libraries

## The Code

```py linenums="1" hl_lines="31"
from google.cloud import bigquery
import pandas as pd

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
```

The key function is **extract_information_schema_to_markdown** which is highlighted above. This creates the data dictionary.
To Run the code you can set the datasets you want to extract in "if __name__ == "__main__":". Which can be run through your IDE or through ```python3 <path>```. Example is shown below.

```py
if __name__ == "__main__":
    extract_information_schema_to_markdown("gcp-project", "gcp_dataset")
    extract_information_schema_to_markdown("gcp-project", "gcp_dataset_RAW")
    extract_information_schema_to_markdown("gcp-project", "gcp_dataset_ACCESS")
```

Once you have run this code the files will exist in the docs folder in your repo. You will need to then add, commit and push them into your repo.

```
git add .
git commit -am"added data dictionaries for ..."
git push
```

🚀 Now you are all done. Automated data dictionaries in minutes. If you make any changes to the schemas or add new tables, just rerun this code to overwrite the data dictionaries with the new information. These data dictionaries can now be viewed within your software development platform (e.g Gitlab, Github) or Centralised site (e.g Mkdocs).

To improve upon this we can add more columns to the data dictionary with other tables available within the INFORMATION_SCHEMA. Next steps would also include adding this into the CI/CD process to ensure the schema is always updated when changes are made.

```sql
SELECT
  COLUMN_FIELD_PATHS.table_catalog,
  COLUMN_FIELD_PATHS.table_schema,
  COLUMN_FIELD_PATHS.table_name, 
  COLUMN_FIELD_PATHS.column_name, 
  COLUMN_FIELD_PATHS.data_type, 
  COLUMN_FIELD_PATHS.description, 
  COLUMN_FIELD_PATHS.collation_name, 
  COLUMN_FIELD_PATHS.rounding_mode,
  COL.is_nullable,
  COL.is_partitioning_column,
  COL.clustering_ordinal_position, 
  ordinal_position
FROM `gcp-project.gcp_dataset.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS` COLUMN_FIELD_PATHS
LEFT JOIN `gcp-project.gcp_dataset.INFORMATION_SCHEMA.COLUMNS` COL
  ON COLUMN_FIELD_PATHS.table_catalog = COL.table_catalog
  AND COLUMN_FIELD_PATHS.table_schema = COL.table_schema
  AND COLUMN_FIELD_PATHS.table_name = COL.table_name
  AND COLUMN_FIELD_PATHS.column_name = COL.column_name
ORDER BY table_name ASC, ordinal_position ASC
```

!!! rocket "This is only the beginning"

    This is only a starting point and more can be done to make this code simple and efficient. So I would like to hear your thoughts!! I would love to hear about any improvements you would make to this or additions so everyone can make writing data dictionaries easy and super fast. Most importantly I  want this information to be readable and accessable, so people can find data quickly and easily.