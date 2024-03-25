import sys, re

# Get the JSX string from the command-line arguments
jsx = sys.argv[1]

# Compile a regular expression pattern to match '<' and '>' characters
regex = re.compile(r'<(?!>=)|(?<!=)>')

# Use the sub method to replace the matched characters with their corresponding HTML entities
result = re.sub(
    regex,
    lambda m: "&lt;" if m.group() == "<" else "&gt;",
    jsx
)

# Print the result to the standard output
print(result)
