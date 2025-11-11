from .fetcher import Fetcher
from .parser import Parser
from .saver import Saver

class Scraper:
    def __init__(self, search_url, output_format="csv", user_agent=None):
        self.search_url = search_url
        self.output_format = output_format
        self.fetcher = Fetcher(user_agent)
        self.parser = Parser()
        self.saver = Saver()

    def run(self):
        print(f"Fetching data from {self.search_url}...")
        page_content = self.fetcher.fetch_page(self.search_url)
        if not page_content:
            print("Failed to retrieve content.")
            return
        
        print("Parsing the content...")
        repositories = self.parser.parse_search_results(page_content)
        print(f"Found {len(repositories)} repositories.")

        if self.output_format == "csv":
            print("Saving to CSV...")
            self.saver.save_to_csv(repositories)
        elif self.output_format == "json":
            print("Saving to JSON...")
            self.saver.save_to_json(repositories)
        else:
            print(f"Unsupported output format: {self.output_format}")
