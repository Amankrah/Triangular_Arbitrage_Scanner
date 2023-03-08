# https://docs.nodereal.io/reference/pancakeswap-graphql-api
import requests
import json

""" RETRIEVE GRAPH QL MID PRICES FOR PANCAKESWAP"""

def retrieve_pancakeswap_information():
    query = """
         {
              pairs(orderBy:trackedReserveBNB, orderDirection: desc, where:
              {token0_in:["0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
              "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
              "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
              "0x55d398326f99059fF775485246999027B3197955"
              "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"
              "0x8C851d1a123Ff703BD1f9dabe631b69902Df5f97"
              "0xD40bEDb44C081D2935eebA6eF5a3c8A31A1bBE13"
              "0x1F7e8fe01AEbA6fDAEA85161746f4D53DC9bdA4F"
              "0x6cf271270662be1C4fc1b7BB7D7D7Fc60Cc19125"
              "0x2859e4544C4bB03966803b044A93563Bd2D0DD4D"
              "0xD41FDb03Ba84762dD66a0af1a6C8540FF1ba5dfb"
              "0xa260E12d2B924cb899AE80BB58123ac3fEE1E2F0"
              "0xCa3F508B8e4Dd382eE878A314789373D80A5190A"
              "0xF68C9Df95a18B2A5a5fa1124d79EEEffBaD0B6Fa"
              "0xBf5140A22578168FD562DCcF235E5D43A02ce9B1"
              "0x3019BF2a2eF8040C242C9a4c5c4BD4C81678b2A1"
              "0x0Eb3a705fc54725037CC9e008bDede697f62F335"
              "0x9C65AB58d8d978DB963e63f2bfB7121627e3a739"
              "0x56b6fB708fC5732DEC1Afc8D8556423A2EDcCbD6"
              "0xFeea0bDd3D07eb6FE305938878C0caDBFa169042"
              "0xBc7d6B50616989655AfD682fb42743507003056D"
              "0x3EE2200Efb3400fAbB9AacF31297cBdD1d435D47"
              "0x6bfF4Fb161347ad7de4A625AE5aa3A1CA7077819"
              "0xAC51066d7bEC65Dc4589368da368b212745d63E8"
              "0xc5E6689C9c8B02be7C49912Ef19e79cF24977f03"
              "0xf307910A4c7bbc79691fD374889b36d8531B08e3"
              "0x52F24a5e03aee338Da5fd9Df68D2b6FAe1178827"
              "0xC762043E211571eB34f1ef377e5e8e76914962f9"
              "0x37dfACfaeDA801437Ff648A1559d73f4C40aAcb7"
              "0xCfFD4D3B517b77BE32C76DA768634dE6C738889B"
              "0x40C8225329Bd3e28A043B029E0D07a5344d2C27C"
              "0x031b41e504677879370e9DBcF937283A8691Fa7f"
              "0xaEC945e04baF28b135Fa7c640f624f8D90F1C3a6"
              "0xd17479997F34dd9156Deef8F95A52D81D265be9c"
              "0x039cB485212f996A9DBb85A9a75d898F94d38dA6"
              "0x8fF795a6F4D97E7887C79beA79aba5cc76444aDf"
              "0xe0F94Ac5462997D2BC57287Ac3a3aE4C31345D66"
              "0x9f589e3eabe42ebC94A44727b3f3531C0c877809"
              ]
              token1_in:["0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
              "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
              "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
              "0x55d398326f99059fF775485246999027B3197955"
              "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"
              "0x8C851d1a123Ff703BD1f9dabe631b69902Df5f97"
              "0xD40bEDb44C081D2935eebA6eF5a3c8A31A1bBE13"
              "0x1F7e8fe01AEbA6fDAEA85161746f4D53DC9bdA4F"
              "0x6cf271270662be1C4fc1b7BB7D7D7Fc60Cc19125"
              "0x2859e4544C4bB03966803b044A93563Bd2D0DD4D"
              "0xD41FDb03Ba84762dD66a0af1a6C8540FF1ba5dfb"
              "0xa260E12d2B924cb899AE80BB58123ac3fEE1E2F0"
              "0xCa3F508B8e4Dd382eE878A314789373D80A5190A"
              "0xF68C9Df95a18B2A5a5fa1124d79EEEffBaD0B6Fa"
              "0xBf5140A22578168FD562DCcF235E5D43A02ce9B1"
              "0x3019BF2a2eF8040C242C9a4c5c4BD4C81678b2A1"
              "0x0Eb3a705fc54725037CC9e008bDede697f62F335"
              "0x9C65AB58d8d978DB963e63f2bfB7121627e3a739"
              "0x56b6fB708fC5732DEC1Afc8D8556423A2EDcCbD6"
              "0xFeea0bDd3D07eb6FE305938878C0caDBFa169042"
              "0xBc7d6B50616989655AfD682fb42743507003056D"
              "0x3EE2200Efb3400fAbB9AacF31297cBdD1d435D47"
              "0x6bfF4Fb161347ad7de4A625AE5aa3A1CA7077819"
              "0xAC51066d7bEC65Dc4589368da368b212745d63E8"
              "0xc5E6689C9c8B02be7C49912Ef19e79cF24977f03"
              "0xf307910A4c7bbc79691fD374889b36d8531B08e3"
              "0x52F24a5e03aee338Da5fd9Df68D2b6FAe1178827"
              "0xC762043E211571eB34f1ef377e5e8e76914962f9"
              "0x37dfACfaeDA801437Ff648A1559d73f4C40aAcb7"
              "0xCfFD4D3B517b77BE32C76DA768634dE6C738889B"
              "0x40C8225329Bd3e28A043B029E0D07a5344d2C27C"
              "0x031b41e504677879370e9DBcF937283A8691Fa7f"
              "0xaEC945e04baF28b135Fa7c640f624f8D90F1C3a6"
              "0xd17479997F34dd9156Deef8F95A52D81D265be9c"
              "0x039cB485212f996A9DBb85A9a75d898F94d38dA6"
              "0x8fF795a6F4D97E7887C79beA79aba5cc76444aDf"
              "0xe0F94Ac5462997D2BC57287Ac3a3aE4C31345D66"
              "0x9f589e3eabe42ebC94A44727b3f3531C0c877809"
              ]

              }){
              id
              name
              reserve0
              reserve1
              token0 {id symbol  decimals}
              token1 {id symbol  decimals}
              }

        }
    """

    url = "https://open-platform.nodereal.io/4b8c54fec1c647d9b75a218749872ce7/pancakeswap/graphql"
    req = requests.post(url, json={'query': query})
    json_dict = json.loads(req.text)
    return json_dict