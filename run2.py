import json
import time
import func_triarb2
import QueryBlock2

if __name__ == "__main__":

    while True:

        pairs = QueryBlock2.retrieve_pancakeswap_information()["data"]["pairs"]
        structured_pairs = func_triarb2.structure_trading_pairs(pairs, limit=500)

        # Get surface rates
        surface_rates_list = []
        for t_pair in structured_pairs:
            surface_rate = func_triarb2.calc_triangular_arb_surface_rate(t_pair, min_rate = 10)
            if len(surface_rate) > 0:
                surface_rates_list.append(surface_rate)

        # Save to JSON file
        if len(surface_rates_list) > 0:
            with open("pancakeswap_arbitrage2.json", "w") as fp:
                json.dump(surface_rates_list, fp)
                print("File saved.")

        time.sleep(60)