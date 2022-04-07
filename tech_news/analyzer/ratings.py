from tech_news.database import get_collection


def top_5_news():
    result = []
    for news in get_collection().aggregate(
        [
            {
                "$group": {
                    "_id": {"title": "$title", "url": "$url"},
                    "popularity": {
                        "$sum": {
                            "$sum": [
                                "$shares_count",
                                "$comments_count",
                            ]
                        }
                    },
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "title": "$_id.title",
                    "url": "$_id.url",
                },
            },
            {
                "$sort": {
                    "popularity": -1,
                    "title": 1,
                },
            },
            {
                "$limit": 5,
            },
        ]
    ):
        if news["title"] is not None or news["url"] is not None:
            result.append((news["title"], news["url"]))
    return result


def top_5_categories():
    result = []
    for category in get_collection().aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$project": {"_id": 0, "category": "$_id"}},
            {"$sort": {"count": -1, "category": 1}},
            {"$limit": 5},
        ]
    ):
        result.append(category["category"])
    return result
