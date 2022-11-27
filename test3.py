import re

validate_phone_number_pattern = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
re.match(validate_phone_number_pattern, "+1 (615) 243-5172")