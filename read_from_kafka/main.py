import os
from quixstreams import Application
import json

# for local dev, load env vars from a .env file
from dotenv import load_dotenv
load_dotenv()

def main():
    app = Application(consumer_group="data_source", auto_offset_reset="earliest",loglevel="DEBUG")

    input_topic = app.topic(os.environ["input"])
    output_topic = app.topic(os.environ["output"])

    with app.get_consumer() as consumer:
            consumer.subscribe([input_topic.name])

            while True:
                msg = consumer.poll(1)

                if msg is None:
                    print("Waiting...")
                elif msg.error() is not None:
                    raise Exception(msg.error())
                else:
                    key = msg.key().decode("utf8")
                    value = json.loads(msg.value())
                    offset = msg.offset()

                    print(f"{offset} {key} {value}")
                    consumer.store_offsets(msg)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass