AI-Driven Insurance Sales Suite
===============================

This repository contains a suite of four projects that together create an AI-driven solution for insurance sales. Our solution harnesses the power of artificial intelligence to provide personalized insurance recommendations, real-time price prediction, and enhanced customer interaction through a Rasa chatbot.

Components
----------

1.  bot_ui - The user interface for the chatbot, presenting an intuitive interface for customers to interact with the Rasa bot.

2.  price_prediction - An RandomForestRegressor model that predicts insurance pricing based on the customer data collected during the chat.

3.  rasa_bot - A Rasa chatbot that collects customer data, provides real-time insurance comparisons, and interfaces with the other components.

4.  recommendations - A system that uses the data collected by the Rasa chatbot to provide personalized insurance recommendations.

* * * * *

Installation
------------

Each project has its own dependencies and requires a separate virtual environment. Follow the installation instructions for each one in the respective order.

### bot_ui

To install: to be added

### price_prediction

To install:

```
cd price_prediction
python3 -m venv ./venv
source ./venv/bin/activate
python3.8 -m pip install -r requirements.txt
```

### rasa_bot

To install: (Provide instructions here)

### recommendations

To run:

```
cd recommendations
python3 -m venv ./venv
source ./venv/bin/activate
python3.8 -m pip install -r requirements.txt
```

* * * * *

Running the Projects
--------------------

### bot_ui

To start:

```
open index.html file in the browser
```

### price_prediction

To start:

```
cd price_prediction
source ./venv/bin/activate
python3.8 main.py
```

### rasa_bot

To start:

```
cd rasa_bot
source ./venv/bin/activate
rasa run actions
docker run -p 8000:8000 rasa/duckling
rasa run -m models --enable-api --cors "*" --debug
```

### recommendations

To start:

```
cd recommendations
source ./venv/bin/activate
python3.8 main.py
```

### database

To start

```
docker-compose -f docker-compose-db.yml up
```

* * * * *

Contributions and Future Enhancements
-------------------------------------

We are actively working on improving this project and adding new features. The upcoming enhancements will include sentiment analysis integration, speech recognition and synthesis, multilingual support, advanced machine learning models, and integration with additional sales channels.

We encourage contributions and suggestions. Please feel free to open issues or submit pull requests!

* * * * *

Resources used
-------------------------------------

* https://rasa.com/docs/rasa/
* https://extendsclass.com/csv-generator.html
* https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/02_lead_bot
* https://github.com/facebook/duckling
* https://github.com/JiteshGaikwad/Chatbot-Widget
* https://github.com/dotnet/machinelearning-samples