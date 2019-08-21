# If you note that most policies are a set of conditions,
#  You can also note that they can be worked in any order.
#  This means that you filter out data in any order to
#  arrive at the same set of allowed data (i.e. encapsulating functions
#   can be done in any order.) except for extra functions such as get max

import db_manager as dm

# class policy_pass:
#
#     def __init__(self, parent_policy_func, add_constraint):
#         self.pr = parent_policy_func
#         self.con = add_constraint
#         self.con_params =
#
#     def policy_results(self):
#         dataview = self.pr()
#         dataview = self.add_constraint(dataview)

#  Example policy 1
#   Can access all of Bob's data from UCLA
#   Only offer functions to one more party, with limitation of only accessing
#   Bob's UCLA data from values 11 to 17

class policy1:

    def __init__(self, connection):
        self.connection = connection

    def policy_results(self):
        dataview  = dm.get_data(self.connection, "health")
        return dataview

    def query(self):
        return self.policy_results()
    # def export_policy(self):
    #
    #     parent_pol = self.policy_results
    #     constraint = dm.filter_data_time
    #
    #     # Create a new ToU
    #     policy_pass = policy_pass(parent_pol)
    #     return

# Example policy 2
#  Can access Bob'x max occuring activity at any point when he's at the Movies
#  and the time is in between 10 to 50
#  Basically must filter down Movies data to time data to max occuring data to
#   additional conditionals
class policy2:

    def __init__(self, connection):
        self.connection = connection

    # Returns the max view of this user's policies - they can perform queries
    #  on whatever view is granted.
    def policy_results(self):
        data = dm.get_data(self.connection, "health")
        # Get data from user at the movies
        data = dm.filter_data_location(data, "location", "MOVIES")
        # Get data from the user between these times
        data = dm.filter_data_time(data, "time", [10, 50])
        # Get max occuring activity data from this view
        dataview = dm.get_max_count_of_column(data, 3)

        return dataview

    # Allowed to query from the data that results from any of their functional
    #  policies
    def query(self):
        return self.policy_results()


# Example policy 3
#  Can only access data for the next




# Policy evaluator
#  Use some code of the original function, as well as
