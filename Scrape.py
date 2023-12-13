import requests
import requests

url = "https://api.fightinsider.io/gql"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
}

payload = {
    "query": "query OddsEventMenuQrQuery {\n  promotions: allPromotions(isActive: true) {\n    ...OddsEventMenu_promotions\n  }\n  upcomingEvents: allEvents(upcoming: true, orderBy: \"date\", isCancelled: false) {\n    ...OddsEventMenu_events\n    edges {\n      node {\n        straightOfferCount\n        promotion {\n          id\n        }\n        id\n      }\n    }\n  }\n  sportsbooks: allSportsbooks(hasOdds: true) {\n    ...OddsEventMenu_sportsbooks\n  }\n  eventOfferTable(nextEvent: true, isCancelled: false) {\n    ...OddsEventMenu_eventOfferTable\n    id\n  }\n}\n\nfragment EventOfferTable_eventOfferTable on EventOfferTableNode {\n  name\n  pk\n  fightOffers {\n    edges {\n      node {\n        id\n        fighter1 {\n          firstName\n          lastName\n          slug\n          id\n        }\n        fighter2 {\n          firstName\n          lastName\n          slug\n          id\n        }\n        bestOdds1\n        bestOdds2\n        slug\n        propCount\n        isCancelled\n        straightOffers {\n          edges {\n            node {\n              sportsbook {\n                id\n                shortName\n                slug\n              }\n              outcome1 {\n                id\n                odds\n                ...OddsWithArrowButton_outcome\n              }\n              outcome2 {\n                id\n                odds\n                ...OddsWithArrowButton_outcome\n              }\n              id\n            }\n          }\n        }\n      }\n    }\n  }\n}\n\nfragment EventOfferTable_sportsbooks on SportsbookNodeConnection {\n  edges {\n    node {\n      id\n      shortName\n      slug\n    }\n  }\n}\n\nfragment OddsEventMenu_eventOfferTable on EventOfferTableNode {\n  pk\n  ...EventOfferTable_eventOfferTable\n}\n\nfragment OddsEventMenu_events on EventNodeConnection {\n  edges {\n    node {\n      pk\n      id\n      name\n      slug\n      date\n      straightOfferCount\n      promotion {\n        id\n      }\n    }\n  }\n}\n\nfragment OddsEventMenu_promotions on PromotionNodeConnection {\n  edges {\n    node {\n      id\n      shortName\n      logo\n    }\n  }\n}\n\nfragment OddsEventMenu_sportsbooks on SportsbookNodeConnection {\n  ...EventOfferTable_sportsbooks\n}\n\nfragment OddsWithArrowButton_outcome on OutcomeNode {\n  id\n  ...OddsWithArrow_outcome\n}\n\nfragment OddsWithArrow_outcome on OutcomeNode {\n  odds\n  oddsPrev\n}",
    "variables": {}
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")
