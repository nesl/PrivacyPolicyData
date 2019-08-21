# PrivacyPolicyData
Project involving basic algorithmically parseable privacy language with smart contracts


# Organization
Top level folder includes all files for running a basic script with key value store
 for accessing "private" data.  policies.py is a class of policies that can be enforced, and
 test.py tests the different policies available (expressed in plain English).  db_manager.py allows for database management along with extra functions specific to both
 granularity of the requested access (i.e. aggregate over a time range) and extent
 (i.e. only allow access between 9-10am)

 The "solidity" folder is a sandbox for testing smart contracts and how they
 can executed.

 # Running the Files

 Running the basic script for testing policies is easy. Just get Python 3.5+ and the sqlite3 package.
 To run the Solidity scripts, follow the install instructions at:
 https://medium.com/@mvmurthy/full-stack-hello-world-voting-ethereum-dapp-tutorial-part-1-40d2d0d807c2#.yqxqj0hff
 And then run:
 '''
 node test.js
 '''
