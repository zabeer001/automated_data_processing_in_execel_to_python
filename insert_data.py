from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up Selenium WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()

# List of keywords to search for
keywords = ["campus", "night", "Baby"]

# Prepare lists to store the longest options
longest_options = []
shortest_options = keywords  # Shortest will just be the keywords themselves

# Loop through the keywords and search on Google
for keyword in keywords:
    # Construct the search URL (you can modify this as needed)
    search_url = f'https://www.google.com/search?q={keyword}'
    
    # Open the search results page
    driver.get(search_url)
    
    # Wait for the page to load completely
    time.sleep(2)  # This is a basic wait, you can use WebDriverWait for more dynamic waits

    # Find all the search result titles or snippets (you can adjust this selector based on the page)
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')

    # Initialize variables to keep track of longest text
    longest_text = ""

    # Iterate through the search results
    for result in results:
        result_text = result.text
        
        # Check if this text is the longest
        if len(result_text) > len(longest_text):
            longest_text = result_text
    
    # Append the longest result for this keyword
    longest_options.append(longest_text)

# Close the browser
driver.quit()

# Prepare the data in a structured format (as a pandas DataFrame)
data = {
    'keyword': keywords,
    'longest option': longest_options,
    'shortest option': shortest_options  # Shortest option is now just the keyword
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('google_search_data.xlsx', index=False)

# Alternatively, save to a CSV file if needed
# df.to_csv('google_search_data.csv', index=False)

# Print the DataFrame
print(df)
