
import sqlite3
from collections import Counter


# First we need some code for creating the tables, creating columns,
#   creating rows, etc.

# Return the connection for this database
def connect_db(dbname = "ex.db"):
    return sqlite3.connect(dbname)

# Show the rows of the table
def show_table(connection, table_name):

    #  Get the cursor for this connection
    c = connection.cursor()

    for row in c.execute('SELECT * FROM ' + table_name):
        print(row)

# Create the table with the column names and types specified
def create_table(connection, table_name, col_names, col_types):

    #  Get the cursor for this connection
    c = connection.cursor()

    table_args = "("
    for index, name in enumerate(col_names):
        table_args += " " + name + " " + col_types[index] + ","
    table_args = table_args[:-1] + ")"

    # # Create table
    c.execute("CREATE TABLE " + table_name + " " + table_args)

    # Save (commit) the changes
    connection.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    #connection.close()


# Insert a row of data into the table
def insert_into_table(connection, table_name, values):
    #  Get the cursor for this connection
    c = connection.cursor()

    # Insert a row of data
    table_args = "("
    for index, val in enumerate(values):
        if isinstance(val, int):
            table_args += str(val) + ","
        elif isinstance(val, str):
            table_args += '\'' + val + '\'' + ","

    table_args = table_args[:-1] + ")"
    print("INSERT INTO " + table_name + " VALUES " + table_args)
    c.execute("INSERT INTO " + table_name + " VALUES " + table_args)

    # Save (commit) the changes
    connection.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    #conn.close()

# Close the connection to the database
def close_db(connection):
    connection.close()
# We also need code for querying the tables.
#  On top of that, we need code that can perform operations on the tables


# Get all data of a table
def get_data(connection, table_name):
    c = connection.cursor()

    command = "SELECT * "
    command += "FROM \'" + table_name + "\'"
    results = []
    for result in c.execute(command):
        results.append(result)
    return results

# Filter the data according to the location
def filter_data_location(datalist, col_name, location):

    results = []
    # For each element in the datalist,
    #  determine if it is allowed in the results or not
    for row in datalist:

        if row[2] == location:
            results.append(row)

    return results

# Filter the data by time - from one minimum time to a max time
def filter_data_time(datalist, col_name, timelist):

    results = []
    # For each element in the datalist,
    #  determine if it is allowed in the results or not
    for row in datalist:

        if row[1] >= timelist[0] and row[1] <= timelist[1]:
            results.append(row)

    return results

# Get the max number of occurences for a column
def get_max_count_of_column(datalist, col_index):

    results = [x[col_index] for x in datalist]
    # print(results)
    # results = [(g[0], len(list(g[1]))) for g in itertools.groupby(results)]
    # print(results)
    # return results
    results = Counter( results )
    index = list(results.values()).index(max(results.values()))

    results = [(list(results.keys())[index], list(results.values())[index])]

    return results

# # Filters data according to a column
# def filter_data_location(connection, table_name, col_name, location):
#
#     c = connection.cursor()
#
#     command = "SELECT * "
#     command += "FROM \'" + table_name + "\'"
#     command += " WHERE \"" + col_name + "\" = \"" + location + "\""
#     #print(command)
#     results = []
#     for result in c.execute(command):
#         results.append(result)
#     return results
#
# # Filters data according to a column
# def filter_data_time(connection, table_name, col_name, timelist):
#
#     c = connection.cursor()
#
#     command = "SELECT * "
#     command += "FROM \'" + table_name + "\'"
#     command += " WHERE \"" + col_name + "\" >= "  + str(timelist[0]) + \
#     " AND \"" + col_name + "\" <= "  + str(timelist[1])
#
#     results = []
#     for result in c.execute(command):
#         results.append(result)
#     return results
#
# # Get the maximum occuring column value for a column
# def get_max_count_of_column(connection, table_name, col_name):
#     #  Get the cursor for this connection
#     c = connection.cursor()
#
#     command = "SELECT \'" + col_name + "\', COUNT(\'" + col_name + "\') AS \'cnt\' "
#     command += "FROM \'" + table_name + "\'" + " GROUP BY \'" + col_name + "\'"
#     command += " ORDER BY \'cnt\' DESC LIMIT 1"
#     #print(command)
#     results = []
#     for result in c.execute(command):
#         results.append(result)
#     return results

#  Lastly, we need code that can decide whether the user can actually
#  run those operations
