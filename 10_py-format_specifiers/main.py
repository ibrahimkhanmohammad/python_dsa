# Take salary input from user and convert it to float
salary = float(input("What is your salary? "))

# Basic print (raw value)
print(f"He earns {salary} dollars")

# Check the data type (for learning/debugging)
print(type(salary))

# Format salary with commas and 2 decimal places
print(f"He earns ${salary:,.2f}")

# Percentage formatting (NOTE: this works correctly only if value is like 0.25 for 25%)
print(f"His earning in percentage is {salary:.2%}")

# Take city input
city = input("What is your city? ")

# Different alignments with width = 10
print(f"{city:^10} place")   # center align
print(f"{city:>10} place")   # right align
print(f"{city:<10} place")   # left align
print(f"{city:_<10} place")  # left align with '_' fill

# Sign formatting
num = 42
print(f"{num:+}")    # always show sign (+)
print(f"{-num:+}")   # negative number with sign

# Zero padding (make number 5 digits)
num_s = 42
print(f"{num_s:05}")  # output: 00042

# Table header
print(f"|{'ID':<6}|{'Name':<10}|")
print("-" * 20)

# Table rows with:
# - zero-padded ID
# - left-aligned name
print(f"|{1:05}|{'Ali':<10}|")
print(f"|{23:05}|{'Sara':<10}|")
print(f"|{456:05}|{'John':<10}|")