friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local = {"Rolf"}

local_friends = abroad.difference(friends)

all_friends = local.union(abroad)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

difference = art.difference(science)
print(difference)
both = art.intersection(science)
print(both)