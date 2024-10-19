"""
word_cloud.py

This script generates a word cloud image from text input provided via command line arguments.
It uses the `WordCloud` class from the `wordcloud` library to create the word cloud and 
`matplotlib` to display the generated image.

Usage:
    python word_cloud.py <text>

Arguments:
    <text>  The text input from which to generate the word cloud. This can be multiple words 
            or sentences, and should be provided as command line arguments.

Example:
    python word_cloud.py "This is an example text for generating a word cloud."

Dependencies:
    - sys: For accessing command line arguments.
    - matplotlib.pyplot: For displaying the word cloud image.
    - wordcloud.WordCloud: For generating the word cloud image.

The script performs the following steps:
1. Collects text input from command line arguments.
2. Prints the collected text to the console for verification.
3. Generates a word cloud image from the input text.
4. Creates a matplotlib figure to display the word cloud.
5. Displays the word cloud image with smooth interpolation.
6. Removes axis labels for a cleaner look.
7. Shows the plot.
"""
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Collect text input from command line arguments
# sys.argv[1:] gets all command line arguments except the script name
text = '\n'.join(sys.argv[1:])

# Print the collected text to the console for verification
print(text)

# Generate a word cloud image from the input text
# width and height set the dimensions of the word cloud
# background_color sets the background color of the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# Create a matplotlib figure to display the word cloud
plt.figure(figsize=(10, 5))

# Display the word cloud image
# interpolation="bilinear" makes the display smoother
plt.imshow(wordcloud, interpolation="bilinear")

# Remove axis labels for a cleaner look
plt.axis("off")

# Show the plot
plt.show()