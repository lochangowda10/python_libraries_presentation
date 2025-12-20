
## FILE 4: 04_beautifulsoup_demo.py

"""
PYTHON LIBRARIES SELF-LEARNING ACTIVITY
Demo 4: BeautifulSoup - Web Scraping Library
Author: [Your Name]
Date: December 18, 2025
"""

try:
    from bs4 import BeautifulSoup
    import requests
    LIBRARIES_AVAILABLE = True
except ImportError:
    LIBRARIES_AVAILABLE = False
    print("⚠️  BeautifulSoup or Requests not installed.")
    print("Run: pip install beautifulsoup4 requests")

print("=" * 60)
print("BEAUTIFULSOUP DEMO - Web Scraping")
print("=" * 60)

if LIBRARIES_AVAILABLE:
    # Example 1: Parse Simple HTML
    print("\n1. PARSING HTML STRING:")
    print("-" * 40)
    
    html_content = """
    <html>
        <head><title>Python Libraries</title></head>
        <body>
            <h1>Popular Python Libraries</h1>
            <div class="library">
                <h2>NumPy</h2>
                <p>For numerical computing</p>
            </div>
            <div class="library">
                <h2>Pandas</h2>
                <p>For data analysis</p>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_content, 'html.parser')
    print(f"Page Title: {soup.title.string}")
    print(f"Main Heading: {soup.h1.string}")
    
    print("\nLibrary Names:")
    library_names = soup.find_all('h2')
    for i, name in enumerate(library_names, 1):
        print(f"  {i}. {name.string}")
    
    # Example 2: Job Listings
    print("\n2. JOB LISTINGS EXAMPLE:")
    print("-" * 40)
    
    job_html = """
    <html>
        <body>
            <div class="job">
                <h3>Python Developer</h3>
                <span class="company">Tech Corp</span>
                <span class="salary">₹8-12 LPA</span>
            </div>
            <div class="job">
                <h3>Data Scientist</h3>
                <span class="company">Data Inc</span>
                <span class="salary">₹10-15 LPA</span>
            </div>
        </body>
    </html>
    """
    
    job_soup = BeautifulSoup(job_html, 'html.parser')
    jobs = job_soup.find_all('div', class_='job')
    
    for i, job in enumerate(jobs, 1):
        title = job.find('h3').string
        company = job.find('span', class_='company').string
        salary = job.find('span', class_='salary').string
        print(f"\nJob {i}: {title}")
        print(f"  Company: {company}")
        print(f"  Salary: {salary}")
    
    print("\n" + "=" * 60)
    print("BeautifulSoup Demo Complete!")
    print("=" * 60)
else:
    print("\nPlease install: pip install beautifulsoup4 requests")