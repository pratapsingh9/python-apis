import requests
from bs4 import BeautifulSoup

def get_repo_details(repo_url):
    response = requests.get(repo_url)
    if response.status_code != 200:
        return {"error": f"Failed to retrieve data: {response.status_code}"}

    soup = BeautifulSoup(response.content, 'html.parser')

    # Get repository name
    repo_name = soup.find('strong', {'itemprop': 'name'}).text.strip()

    # Get repository description (if available)
    description_tag = soup.find('p', {'itemprop': 'description'})
    repo_description = description_tag.text.strip() if description_tag else "No description available"

    # Get the file and folder structure
    file_list = []
    files = soup.find_all('a', {'class': 'js-navigation-open Link--primary'})
    for file in files:
        file_name = file.text.strip()
        file_path = repo_url + "/tree/main/" + file_name
        file_list.append({"name": file_name, "path": file_path})

    # Get other details (stars, forks, etc.)
    stars = soup.find('a', {'href': repo_url.split('github.com/')[-1] + '/stargazers'})
    forks = soup.find('a', {'href': repo_url.split('github.com/')[-1] + '/network/members'})
    repo_stars = stars.text.strip() if stars else "N/A"
    repo_forks = forks.text.strip() if forks else "N/A"

    return {
        "repository_name": repo_name,
        "description": repo_description,
        "structure": file_list,
        "stars": repo_stars,
        "forks": repo_forks
    }
