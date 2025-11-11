from bs4 import BeautifulSoup

class Parser:
    def parse_search_results(self, page_content):
        soup = BeautifulSoup(page_content, "html.parser")
        repositories = []

        for repo_item in soup.find_all("li", class_="repo-list-item"):
            title_tag = repo_item.find("a", class_="v-align-middle")
            description_tag = repo_item.find("p", class_="col-9 color-text-secondary my-1 pr-4")
            url_tag = title_tag["href"]

            title = title_tag.text.strip()
            description = description_tag.text.strip() if description_tag else "No description"
            repo_url = f"https://github.com{url_tag}"

            repositories.append({
                "title": title,
                "description": description,
                "url": repo_url
            })

        return repositories
