import TwitterAPI
import yaml
import conf

def main():
    conf.check_conf()

    with open("config.yaml", "r") as config_file:
        crawl_config = yaml.load(config_file)

    if not crawl_config:
        return

    with open("lock.yaml", "r") as lock_file:
        crawl_status = yaml.load(lock_file)
    
    if not crawl_status:
        crawl_status = {}
    
    api = TwitterAPI.TwitterAPI( ** crawl_config)
    data = {
        "screen_name": "vnnlp"
    }

    if "max_id" in crawl_status:
        data["max_id"] = crawl_status["max_id"] - 1
    
    max_id = None
    try:
        with open("output.yaml", "a") as output_file:
            r = TwitterAPI.TwitterPager(api, "statuses/user_timeline", data)
            for item in r.get_iterator():
                yaml.dump([item], output_file, default_flow_style=False)

                if "id" in item:
                    max_id = item["id"]

    except KeyboardInterrupt:
        pass

    if max_id:
        crawl_status["max_id"] = max_id
    
    with open("lock.yaml", "w") as lock_file:
        yaml.dump(crawl_status, lock_file, default_flow_style=False)

    return

if __name__ == "__main__":
    main()
