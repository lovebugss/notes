import boto3
import logging
import requests

logging.basicConfig(level=logging.DEBUG)


def main():
    protocol = "https://"
    host = "pricing.us-east-1.amazonaws.com"
    index_path = "/offers/v1.0/cn/index.json"
    resp = requests.get("https://" + host + index_path)
    result = resp.json()
    services = result['offers']
    for k, v in services.items():
        url = "https://{host}{uri}".format(host=host, uri=v['currentVersionUrl']).replace('json', 'csv')
        res = requests.get(url, stream=True)
        with open("cn/" + k + "-CN.csv", 'wb') as f:
            for chunk in res.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)


if __name__ == '__main__':
    '''
    北京：https://pricing.us-east-1.amazonaws.com/offers/v1.0/cn/AmazonDynamoDB/current/cn-north-1/index.json
    宁夏：https://pricing.us-east-1.amazonaws.com/offers/v1.0/cn/AmazonDynamoDB/current/cn-northwest-1/index.json
    '''
    main()
