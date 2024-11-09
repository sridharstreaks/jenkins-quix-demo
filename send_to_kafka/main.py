from quixstreams import Application  # import the Quix Streams modules for interacting with Kafka:
# (see https://quix.io/docs/quix-streams/v2-0-latest/api-reference/quixstreams.html for more details)

# import additional modules as needed
import os
import json
import requests
import time
import logging

# for local dev, load env vars from a .env file
from dotenv import load_dotenv
load_dotenv()

app = Application(consumer_group="data_source", auto_create_topics=True,loglevel="DEBUG")  # create an Application

# define the topic using the "output" environment variable
topic_name = os.environ["output"]
topic = app.topic(topic_name)


def get_weather():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 51.5,
            "longitude": -0.11,
            "current": "temperature_2m",
        },
    )

    return response.json()


def main():
    """
    Read data from the hardcoded dataset and publish it to Kafka
    """

    # create a pre-configured Producer object.
    with app.get_producer() as producer:
        while True:
            weather = get_weather()
            logging.debug("Got weather: %s", weather)
            # publish the data to the topic
            producer.produce(
                topic=topic.name,
                key="London",
                value=json.dumps(weather),
            )

            # for more help using QuixStreams see docs:
            # https://quix.io/docs/quix-streams/introduction.html

            logging.info("Produced. Sleeping...")
            time.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()