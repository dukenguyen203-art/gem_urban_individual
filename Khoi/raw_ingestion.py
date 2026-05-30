import pandas as pd
from sqlalchemy import create_engine

# Create a database engine
engine = create_engine(
    "postgresql://developer.gnimypbqaaeqfgisfuei:Gem%402026@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require"
)

# Read the agency.txt file into a DataFrame
df_agency = pd.read_csv(r"Folder Directory\agency.txt")

df_agency.to_sql(
    "gtfs_metro_train_agency",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the calendar.txt file into a DataFrame
df_calendar = pd.read_csv(r"Folder Directory\calendar.txt")

df_calendar.to_sql(
    "gtfs_metro_train_calendar",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the calendar_dates.txt file into a DataFrame
df_calendar_dates = pd.read_csv(r"Folder Directory\calendar_dates.txt")

df_calendar_dates.to_sql(
    "gtfs_metro_train_calendar_dates",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the levels.txt file into a DataFrame
df_levels = pd.read_csv(r"Folder Directory\levels.txt")

df_levels.to_sql(
    "gtfs_metro_train_levels",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

#Read the pathways.txt file into a DataFrame
df_pathways = pd.read_csv(r"Folder Directory\pathways.txt")
df_pathways.to_sql(
    "gtfs_metro_train_pathways",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the routes.txt file into a DataFrame
df_routes = pd.read_csv(r"Folder Directory\routes.txt")

df_routes.to_sql(
    "gtfs_metro_train_routes",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the shapes.txt file into a DataFrame
df_shapes = pd.read_csv(r"Folder Directory\shapes.txt")
df_shapes.to_sql(
    "gtfs_metro_train_shapes",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the stop_times.txt file into a DataFrame
df_stop_times = pd.read_csv(r"Folder Directory\stop_times.txt")
df_stop_times.to_sql(
    "gtfs_metro_train_stop_times",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the stops.txt file into a DataFrame
df_stops = pd.read_csv(r"Folder Directory\stops.txt")
df_stops.to_sql(
    "gtfs_metro_train_stops",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the transfers.txt file into a DataFrame
df_transfers = pd.read_csv(r"Folder Directory\transfers.txt")
df_transfers.to_sql(
    "gtfs_metro_train_transfers",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)

# Read the trips.txt file into a DataFrame
df_trips = pd.read_csv(r"Folder Directory\trips.txt")
df_trips.to_sql(
    "gtfs_metro_train_trips",
    engine,
    schema="bronze_urban",
    if_exists="replace",
    index=False
)
