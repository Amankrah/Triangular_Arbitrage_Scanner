import pandas as pd
import os
import json
import time

json_file = 'pancakeswap_arbitrage2.json'
csv_file = 'pancakeswap_rates2.csv'

while True:
    # check the last modified time of the json file
    json_mod_time = os.path.getmtime(json_file)

    try:
        # read the JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)

        # convert json data to dataframe
        df = pd.json_normalize(data)

        # write the dataframe to csv file
        df.to_csv(csv_file, index=False)

        print(f'{csv_file} has been updated')
    except Exception as e:
        print(e)

    # wait for 60 seconds
    time.sleep(60)


