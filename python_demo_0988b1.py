# Learning Objective: Craft an interactive data visualization that tells a compelling story using Python with Plotly.

# This tutorial will guide you through creating a simple, yet interactive, bar chart using the Plotly library.
# We'll focus on how to make your visualizations dynamic, allowing users to explore data points.
# This is a fundamental skill for telling stories with data, as interactivity can reveal hidden patterns and insights.

# We'll be using the 'plotly.express' module, which is designed for rapid and easy creation of common plot types.
# Plotly.express is built on top of Plotly.graph_objects, providing a higher-level interface.
# For this tutorial, we will focus on creating a bar chart, a versatile tool for comparing categories.

import plotly.express as px
import pandas as pd

# --- Data Preparation ---
# For this example, we'll create a simple dataset representing fictional sales figures for different products.
# In a real-world scenario, you would load your data from a CSV, Excel file, or database.
# We're using a Pandas DataFrame because it's the standard for data manipulation in Python and works seamlessly with Plotly.

data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home Goods', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Home Goods', 'Clothing'],
    'Sales': [150, 200, 180, 120, 250, 160, 210, 190, 130, 260],
    'Month': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Feb', 'Feb']
}
df = pd.DataFrame(data)

# --- Creating the Interactive Visualization ---
# The core of our interactive visualization will be created using Plotly Express.
# 'px.bar' is the function for generating bar charts.

# 'data_frame=df': This tells Plotly which DataFrame to use for the plot.
# 'x='Product'': This specifies the column to be used for the x-axis, representing our products.
# 'y='Sales'': This specifies the column to be used for the y-axis, representing the sales figures.
# 'color='Category'': This is a key feature for storytelling! It colors the bars based on the 'Category' column.
#                     This allows us to visually distinguish between different product categories.
# 'barmode='group'': This groups bars by 'Product' when multiple entries exist for the same product (e.g., different months).
#                   This helps in comparing sales across months for each product.
# 'title='Product Sales by Category and Month'': Sets a descriptive title for our visualization.
# 'labels={'Product': 'Product Name', 'Sales': 'Total Sales ($)'}': This allows us to customize the axis labels for clarity.
# 'hover_data=['Category', 'Month']': This is where the interactivity comes in! When you hover over a bar,
#                                     these additional data points will be displayed. This is crucial for
#                                     providing context and deeper insights without cluttering the initial view.

fig = px.bar(
    data_frame=df,
    x='Product',
    y='Sales',
    color='Category',
    barmode='group',
    title='Product Sales by Category and Month',
    labels={'Product': 'Product Name', 'Sales': 'Total Sales ($)'},
    hover_data=['Category', 'Month']
)

# --- Enhancing Interactivity (Optional but Recommended) ---
# While Plotly Express provides good default interactivity (like hover info),
# you can further customize it. For this tutorial, we'll stick to the defaults for simplicity,
# but know that you can, for example, add dropdowns or sliders for more complex interactions
# using Plotly.graph_objects or other libraries.

# --- Displaying the Visualization ---
# The 'fig.show()' method renders the interactive plot.
# If you are in a Jupyter Notebook or similar environment, the plot will appear directly in the output.
# If running as a standalone script, it will typically open in your default web browser.

# fig.show()

# --- Example Usage ---
# To run this code:
# 1. Make sure you have Plotly and Pandas installed:
#    pip install plotly pandas
# 2. Save this code as a Python file (e.g., interactive_sales.py).
# 3. Uncomment the 'fig.show()' line.
# 4. Run the file from your terminal: python interactive_sales.py

# When the plot appears, try the following:
# - Hover your mouse over individual bars to see the detailed information (Product, Sales, Category, Month).
# - Observe how the bars are colored by 'Category', making it easy to see the distribution of sales across categories.
# - Notice how bars for the same product are grouped together by month, allowing for month-over-month comparison.
# - Use the legend on the right to click on a category and filter the view, showing only bars of that category.

print("Interactive visualization created. Uncomment 'fig.show()' to display it.")
print("Example DataFrame:")
print(df)