# the formatted variables
formatter = "%r %r %r %r"
# The output i want, defined as different variables.
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "Bit it didn't sing.",
    "So I said goodnight."
)
