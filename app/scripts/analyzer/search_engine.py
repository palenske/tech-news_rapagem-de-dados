from datetime import datetime
from scripts.db.database import search_news


class SearchEngine:
    def __init__(self):
        self.search = search_news

    def search_by_title(self, title):
        self.title = title
        self.result = self.search(
            {"title": {"$regex": self.title, "$options": "i"}}
        )
        return [(new["title"], new["url"]) for new in self.result]

    def search_by_date(self, date):
        self.date = date
        try:
            bool(datetime.strptime(date, "%Y-%m-%d"))
            self.result = self.search({"timestamp": {"$regex": date}})
        except ValueError:
            raise ValueError("Data inválida")
        else:
            return [(new["title"], new["url"]) for new in self.result]

    def search_by_source(self, source):
        self.source = source
        self.result = self.search(
            {"sources": {"$regex": source, "$options": "i"}}
        )
        return [(new["title"], new["url"]) for new in self.result]

    def search_by_category(self, category):
        self.category = category
        self.result = self.search(
            {"categories": {"$regex": category, "$options": "i"}}
        )
        return [(new["title"], new["url"]) for new in self.result]
