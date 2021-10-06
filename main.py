# Python list mutation, adding elements
history = ["when"]

# adds item to the end of a list
history.append("how")
# ["when", "how"]

# combine lists
history.extend( ["what", "why"] ) # works with tuples too
# or
history = history + ["what", "why"]
# ["when", "how", "what", "why"]

# insert at target position
history.insert(3, "where")
# ["when", "how, "what", "where", "why"]
#