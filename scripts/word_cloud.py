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