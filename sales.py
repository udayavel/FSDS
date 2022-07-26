import mysql.connector as conn
import pandas as pd
import pymongo
import json
import logging

# logging configuration
logging.basicConfig(filename='sales.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

try:

    # mysql configuration
    mydb = conn.connect(host='localhost', user='root', passwd='root', db='ineuron')
    cursor = mydb.cursor()
    logging.info('mysql was configured')

    # mongodb configuration
    client = pymongo.MongoClient(
        "mongodb+srv://Udayavel:root@cluster0.gqsn3hi.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    logging.info('mongodb was configured')

    # 1. Create a  table attribute dataset and dress dataset
    # creating attribute dataset table
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS attribute (Dress_ID INT,Style VARCHAR(30),Price VARCHAR(30),Rating FLOAT,Size VARCHAR(30),Season VARCHAR(30),NeckLine VARCHAR(30),SleeveLength VARCHAR(30),waiseline VARCHAR(30),Material VARCHAR(30),FabricType VARCHAR(30),Decoration VARCHAR(30),PatternType VARCHAR(30),Recommendation INT)')
    logging.info('attribute table created in my sql db')
    # creating dress sales dataset table
    cursor.execute(
        'create table if not exists sales(Dress_ID int,`29/8/2013` int,`31/8/2013` int,`09/02/2013` int,`09/04/2013` int,`09/06/2013` int,`09/08/2013` int,`09/10/2013` int,`09/12/2013` int,`14/9/2013` int,`16/9/2013` int,`18/9/2013` int,`20/9/2013` int,`22/9/2013` int,`24/9/2013` int,`26/9/2013` int,`28/9/2013` int,`30/9/2013` int,`10/02/2013` int,`10/04/2013` int,`10/06/2013` int,`10/08/2010` int,`10/10/2013` int,`10/12/2013` int)')
    logging.info('sales table created in my sql db')
    # 2. Do a bulk load for these two table for respective dataset
    # bulk upload attribue dataset
    cursor.execute(
        "LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Attribute DataSet.csv' INTO TABLE attribute FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 ROWS")
    logging.info('attribute dataset bulk upload performed')
    # bulk upload dress dataset
    cursor.execute(
        "LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Dress Sales.csv' INTO TABLE sales FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 ROWS")
    logging.info('sales dataset bulk upload performed')
    mydb.commit()

    # 3. read these dataset in pandas as a dataframe

    # extracting column names for attribute dataset
    cursor.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "attribute"')
    attribute_columns = cursor.fetchall()
    logging.info('storing attributes column names in variable')

    # extracting column name for sales dataset
    cursor.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "sales"')
    dress_columns = cursor.fetchall()
    logging.info('storing sales column names in variable')

    cursor.execute('select * from attribute')
    # creating attribute dataframe from the SQL
    attribute_df = pd.DataFrame(data=cursor.fetchall(), columns=[column[0] for column in attribute_columns])
    logging.info('attribute dataframe was created using pandas')
    logging.info(attribute_df)

    cursor.execute('select * from sales')
    # creating sales dataframe from the SQL
    sales_df = pd.DataFrame(data=cursor.fetchall(), columns=[column[0] for column in dress_columns])
    logging.info('sales dataframe was created using pandas')
    logging.info(sales_df)

    # 4. Convert attribute dataset in json format
    attribute_json = json.loads(attribute_df.to_json(orient="records"))
    logging.info('attribute dataframe was converted into json')

    # 5. Store this dataset into mongodb
    database = client['ineuron']
    collection = database['attribute']

    # inserting attribute dataset json to mongo db
    collection.insert_many(attribute_json)
    logging.info('attribute dataset successfully inserted into mongodb')

    # 6. in sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID
    cursor.execute('select * from attribute left join sales on attribute.Dress_ID=sales.Dress_ID')
    logging.info('performing leftjoin between attribute and sales datasets')
    for i in cursor.fetchall():
        logging.info(i)

    # 7. Write a sql query to find out how many unique dress that we have based on dress id
    cursor.execute('select count(distinct Dress_ID) from attribute')
    logging.info(f'Unique dress count from dataset - {cursor.fetchall()[0][0]}')

    # 8. Try to find out how mnay dress is having recommendation 0
    cursor.execute('select count(*) from attribute where recommendation=0')
    logging.info(f'{cursor.fetchall()[0][0]} dresses having recommendation 0')

    # 9. Try to find out total dress sell for individual dress id

    # framing column names for sum
    list_col = [f'`{column[0]}`' for column in dress_columns]
    list_col.remove('`Dress_ID`')
    query_col = '+'.join(list_col)
    logging.info('column names for query was framed')

    cursor.execute(f'select Dress_ID,sum({query_col}) from sales group by Dress_ID;')

    logging.info('dress grouping Sum')
    for i, j in cursor.fetchall():
        logging.info(f'{i} : {j}')

    # 10. Try to find out a third highest most selling dress id
    cursor.execute(
        f'select Dress_ID,sum({query_col}) as sales from sales group by Dress_ID ORDER BY sales DESC LIMIT 2, 1;')
    for i, j in cursor.fetchall():
        logging.info(f'Third largest most selling Dress_ID {i} with sum {j}')


except Exception as e:
    logging.error(e)

