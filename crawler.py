import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import csv
import time

def get_all_website_links(start_url):
    # Extract domain info to ensure we stay on the same site
    parsed_uri = urlparse(start_url)
    domain_name = parsed_uri.netloc
    
    # 'visited' keeps track of URLs to prevent loops
    visited = set()
    
    # 'queue' holds URLs to visit (Breadth-First Search)
    queue = deque([start_url])
    
    # List to store links for the CSV
    found_links = []
    
    print(f"--- Starting crawl on: {start_url} ---")
    print("Press Ctrl+C to stop early and save results.\n")

    try:
        while queue:
            current_url = queue.popleft()
            
            if current_url in visited:
                continue
            
            print(f"Scanning: {current_url}")
            
            try:
                response = requests.get(current_url, timeout=5)
                
                # If the link is broken (404) or forbidden, skip
                if response.status_code != 200:
                    visited.add(current_url)
                    continue

                soup = BeautifulSoup(response.text, "html.parser")
                visited.add(current_url)
                
                # Add to our results list
                found_links.append(current_url)

                # Find all links on this page
                for a_tag in soup.find_all("a"):
                    href = a_tag.attrs.get("href")

                    if href == "" or href is None:
                        continue

                    # handle relative paths (e.g. "/contact" becomes "https://site.com/contact")
                    full_url = urljoin(current_url, href)
                    
                    # Clean the URL (remove #fragments)
                    parsed_href = urlparse(full_url)
                    full_url = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

                    # STRICT CHECK: Only follow links on the same domain
                    if domain_name in full_url:
                        if full_url not in visited and full_url not in queue:
                            queue.append(full_url)
            
            except Exception as e:
                print(f"  Error reading {current_url}: {e}")
                visited.add(current_url)

    except KeyboardInterrupt:
        print("\n[!] Stopping manually...")

    return found_links, domain_name

def save_to_csv(links, domain_name):
    # Create a safe filename based on the domain
    filename = f"{domain_name.replace('.', '_')}_links.csv"
    
    print(f"\nSaving {len(links)} links to {filename}...")
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Found Links"]) # Header
        for link in links:
            writer.writerow([link])
            
    print(f"Done! Check the file '{filename}' in your folder.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Ask user for input
    target_site = input("Enter the website URL (e.g., https://www.example.com): ").strip()
    
    if target_site:
        links, domain = get_all_website_links(target_site)
        save_to_csv(links, domain)
    else:
        print("Please provide a valid URL.")
