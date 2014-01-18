stalkernet
==========

A simple program to query the MTU Stalkernet

Basic Usage
-----------

## Import Stalkernet:

    from stalkernet import stalkernet

## Query Stalkernet (the hard way)

    net = stalkernet()
    arr = net.buildArrayFromDict({"fname": ["and", "alice"]})
    data = net.doRunQuery(arr)

## Query Stalkernet (the easy way)

    net = stalkernet()
    data = net.doRunQuery({"fname": ["and", "bob"]})

Stuff to Know
-------------

The initial dictionary is formatted as such:

    {"category": ["operator", "query"]}

The categories can be:

+   fname
+   lname
+   fullname
+   username
+   email

The operators can be:

+   and
+   or
+   notand
+   notor
