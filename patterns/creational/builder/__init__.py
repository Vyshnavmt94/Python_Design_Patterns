# Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach.
# In this design pattern, a builder class builds the final object in step-by-step procedure.


# Constructing Complex objects : The Builder Method allows you to construct the products step-by-step.
# Even, we can defer the execution of some steps without breaking th efinal product.
# To create an object tree, it is handy to call the steps recursively.
# It prevents the client code from fetching the incomplete data because it doesn’t allow the exposing of an unfinished object.

# Differ by Representations: The Builder pattern is applicable when construction of various representations of the product involves similar steps that differ only in the details.
# The base builder intterface is used to define all the construction steps while these steps are implemented by concrete builders.