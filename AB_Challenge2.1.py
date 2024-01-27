# AB Challenge 2.1
# Create a list of legal and illegal variable names. Describe why each is either legal or illegal. 
# Next, create a list of "Good" and "bad" lefal variable names. Describe why each is either a good or bad choice for a variable name.

# Legal Variables

name            # Variable is all letters 
phone_number    # Variable is letters and one Underscore
pn              
variable_1      
var_45          # Letters, Underscores and numbers are all allowed in variable names
_variable       # This one is technically legal, but shouldn't be used. Variables that start with an underscore have a special meaning in python
Username        # This one is technically legal, but shouldn't be capitalized. Traditionally everything in python code is lowercase.

# Illegal Variables

1234            # Variables cannot start with a number
12_var          # Same
variable-1      # Variable names can only contain letters, numbers or underscores. Hyphens are not allowed
$income         # Dollar signs and other special characters are also not allowed in variable names
print           # print is a function in python and cannot be used as a variable
input           # input is also a function

# "Good" variables| These variables are short but descriptive and easy to read, so you have a good understanding of what each variable is being used for. 

client_name
patient_name
invoice_total
phone_number
note
username
account_number
account_balance

# "Bad" variables

pn              # Variable name is way too short and non-descript
variable_1      # This is a little longer, but again not descriptive and would make things confusing down the line as more and more variables are created
personal_checking_account_balance   # This variable isn't bad, and technically meets all of the criteria for a good variable name. However having a variable with such a long name makes it harder to read amongst code, and could cause issues down the line.
invtot          # This just looks like a series of letters smashed together. I know it means Invoice Total, but I created it. Anybody else reading my code may not get that and know what its purpose really is.
var_1234        # This is just a shorthand version of variable_1, and is ultimately bad for the same reasons.
