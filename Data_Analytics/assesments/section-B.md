# Section B Practical Task

1. Develop a Python-based ETL script using SQLAlchemy to automate the
creation of the analytics_db schema and enforce composite primary keys on
the ratings table.

```
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import PrimaryKeyConstraint
import pandas as pd

# MySQL Connection

engine = create_engine(
    "mysql+pymysql://root:password@localhost/analytics_db"
)

metadata = MetaData()

restaurants = Table(
    'restaurants',
    metadata,
    Column('restaurant_id', Integer, primary_key=True),
    Column('restaurant_name', String(255), nullable=False),
    Column('location_id', Integer),
    Column('cuisines', String(255))
)

ratings = Table(
    'ratings',
    metadata,
    Column('restaurant_id', Integer,
           ForeignKey('restaurants.restaurant_id')),
    Column('rating_date', String(20)),
    Column('rating', Float),
    PrimaryKeyConstraint('restaurant_id', 'rating_date')
)

metadata.create_all(engine)

print("Database Created Successfully")

```

2. Implement SQL ALTER statements to establish Referential Integrity through
Foreign Key constraints between restaurants and locations with ON DELETE
CASCADE actions.

```
ALTER TABLE restaurants
ADD CONSTRAINT fk_location
FOREIGN KEY(location_id)
REFERENCES locations(location_id)
ON DELETE CASCADE;
```


3. Write a Python validation script using Pandas to clean the Zomato dataset,
handling "NEW" or "-" values in the rating column before relational ingestion.

```
import pandas as pd

df = pd.read_csv("zomato.csv")

# Replace NEW and -

df['rate'] = df['rate'].replace("NEW", None)
df['rate'] = df['rate'].replace("-", None)

# Remove /5

df['rate'] = df['rate'].str.replace("/5", "", regex=False)

# Convert into float

df['rate'] = pd.to_numeric(df['rate'], errors="coerce")

# Fill missing values

df['rate'].fillna(df['rate'].mean(), inplace=True)

print(df.head())
```


4. Construct an optimized SQL indexing strategy on the location_id and cuisines
columns to accelerate multi-table JOIN operations for analytical queries.

```
CREATE INDEX idx_location
ON restaurants(location_id);

CREATE INDEX idx_cuisines
ON restaurants(cuisines);
```
