import TwitterAPI
import yaml
import conf

if __name__ == "__main__":
    conf.check_conf()

    # Get tweets from 'vnnlp' community.
    with open("config.yaml", "r") as read_stream, \
            open("output.yaml", "a") as write_stream:
        max_id = None
        crawl_status = {}

        try:
            lock_stream = open("lock.yaml", "r")

            crawl_status = yaml.load(lock_stream)
            max_id = crawl_status["statuses/user_timeline"]["max_id"]
        except Exception as error:
            print(error)

        config = yaml.load(read_stream)
        api = TwitterAPI.TwitterAPI(**config)
        data = {
            'screen_name': 'vnnlp',
            'count': 1
        }

        max_id = '975965681354129408'

        if max_id:
            data["max_id"] = max_id

        r = TwitterAPI.TwitterPager(
            api, "statuses/user_timeline", data)

        new_max_id = None

        for item in r.get_iterator():
            yaml.dump([item], write_stream)
            if "id_str" in item:
                new_max_id = item["id_str"]
        
        if new_max_id:
            with open("lock.yaml", "w") as lock_stream:
                if not crawl_status:
                    crawl_status = {}

                crawl_status["status/user_timeline"] = {
                    "max_id": new_max_id
                }
                yaml.dump(crawl_status, lock_stream)
