class MutualFriendCrawling:
    def __init__(self):
        self.queue = set()
        self.map = {}

    def crawl(self):
        while len(self.queue):
            for key, value in self.map:
                pass
