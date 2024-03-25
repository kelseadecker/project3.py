import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Population': [8398748, 3990456, 2705994, 2325502, 1680992]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['City'], df['Population'], color='skyblue')
plt.title('Population of Major US Cities')
plt.xlabel('City')
plt.ylabel('Population')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
