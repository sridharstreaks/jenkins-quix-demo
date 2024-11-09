```mermaid
%%{ init: { 'flowchart': { 'curve': 'monotoneX' } } }%%
graph LR;
send_to_kafka[fa:fa-rocket send_to_kafka &#8205] --> weather_data_demo{{ fa:fa-arrow-right-arrow-left weather_data_demo &#8205}}:::topic;
weather_data_demo{{ fa:fa-arrow-right-arrow-left weather_data_demo &#8205}}:::topic --> read_from_kafka[fa:fa-rocket read_from_kafka &#8205];
read_from_kafka[fa:fa-rocket read_from_kafka &#8205] --> weather_data_demo{{ fa:fa-arrow-right-arrow-left weather_data_demo &#8205}}:::topic;


classDef default font-size:110%;
classDef topic font-size:80%;
classDef topic fill:#3E89B3;
classDef topic stroke:#3E89B3;
classDef topic color:white;
```