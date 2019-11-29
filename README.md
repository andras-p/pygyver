#  py-analytics

Contains Data Enginner, Data Scientist and 3rd party integration tools capabilities

## Installation
py-test-utility can be installed via pip

```python 
pip install ??find the name??
```


## BigQuery ##

To access BigQuery you will need following environment variables:

- `BIGQUERY_PROJECT` - name of the project in BigQuery. Default project cannot be changed in the code.
- `BIGQUERY_ACCESS_TOKEN_PATH` - path to the json token file.

BigQuery functions wrap `bigrquery` functions to provide higher level API removing boilerplate instructions of the lower level API.

## [tdd_utility - module](../blob/master/data_prep/README.md)

### class load_csv(csv,schema) 
Contains methods to extract the equivalent json from csv with nested and repeated records structures


#### Args

- csv
    - path and file name of the csv
    - mandatory
    - nested fields shall be separated by a dot "."  (i.e. item.id, item.quantity)

|order | item.id | item.quantity | delivery.address | delivey.postcode |
|---|---|---|---|---|
| A0001 | item1 | 5 | address1 | e13bp |
| | item2 | 1 | | |
| | item3 | 3 | | |
| A0002 | item4 | 4  | address4 | e13bp |
| | item1 | 4 | | |
| | item3 | 2 | | |

- schema 
    - path and schema file name of the table schema
    - required if the CSV contain nested and repeated records
    - json format i.e. 
```json
[  
    {
      "mode": "NULLABLE", 
      "name": "order", 
      "type": "STRING"
    },  
    {
      "fields": [
        {
          "mode": "NULLABLE", 
          "name": "id", 
          "type": "STRING"
        },
        {
          "mode": "NULLABLE", 
          "name": "quantity", 
          "type": "STRING"
        }
      ], 
      "mode": "REPEATED", 
      "name": "item", 
      "type": "RECORD"
    }, 
    {
      "fields": [
        {
          "mode": "NULLABLE", 
          "name": "address", 
          "type": "STRING"
        }, 
        {
          "mode": "NULLABLE", 
          "name": "postcode", 
          "type": "STRING"
        }
      ], 
      "mode": "NULLABLE", 
      "name": "delivery", 
      "type": "RECORD"
    }
  ]
```

#### Methods
- to_json()
    - if successfuls return the json extracted from the csv

- to_new_line_delimiter_file(output_file_name)
    - return 0 if successfuls 
    - create new line delimiter "output_file_name" file


#### Usage

```python 
>>> from data_prep import tdd_utility as  tu
>>> mockdata_csv = tu.load_csv(
...     csv="path/to/filename/file.csv", 
...     schema="path/to/schema/schema.json") # initialise the object
>>> mockdata_json = mockdata_csv.to_json() # return the equivalent json
>>> mockdata_json = mockdata_csv.to_new_line_delimiter_file(output="path/output_file_name.json") # return output_file_name
```
