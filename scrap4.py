import requests
from bs4 import BeautifulSoup
import csv

# Set the URL of the page to scrape
url = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z'

# Send a request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
anchors = soup.find_all('a')

# Extract the links that lead to illness pages
illness_links = []
for link in anchors:
    href = link.get('href')
    if href and 'illnesses-and-conditions/a-to-z' in href:
        illness_links.append('https://www.nhsinform.scot' + href)

for links in illness_links:       
    print(links)

with open('health_topics_nhs2.csv', mode='w', newline='') as file:  
    writer = csv.writer(file)
    writer.writerow(['Disease','About', 'Symptom', 'Causes', 'Diagnosing', 'Treating', 'Prevention'])
    for illness_link in illness_links:
        # Send a request to the illness page
        response = requests.get(illness_link)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the list of health topics
        health_topics = soup.find('div', {'class': 'js-guide cf guide'})

        if health_topics:
            # Extract the health topics
            health_topic_items = health_topics.find_all(['h1','p', 'h2'])
            
            h=0
            disease = ''
            about = ''
            symptom = ''
            causes = ''
            diagnosing = ''
            treating = ''
            prevention = ''                
            for item in health_topic_items:
                if item.name == 'h1':
                    disease = disease + item.get_text().strip()
                elif item.name == 'h2':
                    h=h+1
                    # writer.writerow([''] * 6)
                    # writer.writerow([item.get_text(), '', '', '', '', ''])
                elif item.name == 'p':
                    text = item.get_text().strip()
                    if h == 1:
                        about = about+item.text
                        #writer.writerow([text, '', '', '', '', ''])
                    elif h == 2:
                        symptom = symptom+item.text
                        # writer.writerow(['', text, '', '', '', ''])
                    elif h == 3:
                        causes = causes+item.text
                        # writer.writerow(['', '', text, '', '', ''])
                    elif h == 4:
                        diagnosing = diagnosing+item.text
                        # writer.writerow(['', '', '', text, '', ''])
                    elif h == 5:
                        treating = treating+item.text
                        # writer.writerow(['', '', '', '', text, ''])
                    elif h == 6:
                        prevention = prevention+item.text
                        # writer.writerow(['', '', '', '', '', text])          
            writer.writerow([disease, about, symptom, causes, diagnosing, treating, prevention])
            print(disease)