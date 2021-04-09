from ComputerVisionClient import ComputerVisionClient
import json

def main():
    with  open('ComputerVision/config.json') as jsonfile:
        config = json.load(jsonfile)
    subskey = config["api_key"]
    endpoint = config["endpoint"]
    client = ComputerVisionClient(subskey, endpoint)
    url = input("Enter an image url: ")
    tagResult = client.Service.tag_image(url)
    for tag in tagResult.tags:
        print(tag)

if __name__ == "__main__":
    main()

