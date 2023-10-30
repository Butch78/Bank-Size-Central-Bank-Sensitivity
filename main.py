print("Hello world")

import matplotlib.pyplot as plt

# Months of the year
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Average rainfall for each month (made-up data)
rainfall = [
    2.5, 3.1, 4.6, 3.8, 2.7, 2.1,
    1.8, 1.9, 2.4, 2.6, 2.2, 2.9
]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(months, rainfall, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Average Rainfall (inches)')
plt.title('Average Rainfall for Each Month of the Year')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
