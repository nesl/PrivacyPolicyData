import os
import random
import db_manager as dm
import policies as pc

def remove_db(dbpath):
    if os.path.exists(dbpath):
        os.remove(dbpath)
        print("Removed DB")

# Just insert some example data into the table
def insert_example_data(connection, table_name):

    locations = ["UCLA", "HOME", "WORK", "MOVIES"]
    activities = ["Running", "Walking", "Sitting", "Dancing"]

    for i in range(0, 50):
        # Pick a random location and activity
        location = locations[random.randint(0,len(locations)-1)]
        activity = activities[random.randint(0,len(activities)-1)]

        values = ["Bob", i, location, activity]
        dm.insert_into_table(connection, table_name, values)

    print("Finished example inserts into database")



DBPATH = "health.db"
# Clear the database
remove_db(DBPATH)

# Test the DB manager to create a database
connection = dm.connect_db(DBPATH)

# Example columns:
col_names = ["patient_name", "time", "location", "activity"]
col_types = ["text", "real", "text", "text"]

dm.create_table(connection, "health", col_names, col_types)
insert_example_data(connection, "health")

dm.show_table(connection, "health")

# Now that the database has been created, we have to define the policies
# Your terms of use are defined by the functions that you are allowed to use
#  That way, you can control the downstream access as well by only giving access
#  to the functions that you can operate with

# data = dm.get_data(connection, "health")

print()

example1 = pc.policy2(connection)
print("\nEXAMPLE 1 QUERY: \n")
print(example1.query())

example2 = pc.policy1(connection)
print("\nEXAMPLE 2 QUERY: \n")
print(example2.query())



# result = dm.get_max_count_of_column(data, 3)
# print(result)
# print()
# result = dm.filter_data_location(data, "location", "UCLA")
# print(result)
# print()
# result = dm.filter_data_time(data, "time", [10, 50])
# print(result)
# print()
dm.close_db(connection)
