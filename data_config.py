# data_config.py

SUBJECT_PLAYER = {
    "name": "Magnus Carlsen",
    "elo": 2840
}

TOURNAMENT_QUOTAS = {
    "Pool_A": 3,
    "Pool_B": 3,
    "Pool_C": 4,
    "Pool_D": 3
}

POOLS = {
    "Pool_A": [  # Super Elite (2754+) - Total: 6 players (Excluding Nakamura)
        {"name": "Fabiano Caruana", "elo": 2793},
        {"name": "Nodirbek Abdusattorov", "elo": 2780},
        {"name": "Vincent Keymer", "elo": 2762},
        {"name": "Alireza Firouzja", "elo": 2759},
        {"name": "Wesley So", "elo": 2754},
        {"name": "Wei Yi", "elo": 2754}
    ],
    
    "Pool_B": [  # Elite (2736 - 2753) - Total: 6 players
        {"name": "Anish Giri", "elo": 2753},
        {"name": "Arjun Erigaisi", "elo": 2751},
        {"name": "Javokhir Sindarov", "elo": 2745},
        {"name": "Praggnanandhaa R", "elo": 2741},
        {"name": "Jan-Krzysztof Duda", "elo": 2739},
        {"name": "Jorden Van Foreest", "elo": 2736}
    ],
    
    "Pool_C": [  # Upper Mid (2715 - 2734) - Total: 11 players
        {"name": "Gukesh D", "elo": 2732},
        {"name": "Ian Nepomniachtchi", "elo": 2729},
        {"name": "Richard Rapport", "elo": 2729},
        {"name": "Hans Moke Niemann", "elo": 2728},
        {"name": "Levon Aronian", "elo": 2724},
        {"name": "Nihal Sarin", "elo": 2723},
        {"name": "Parham Maghsoodloo", "elo": 2720},
        {"name": "Awonder Liang", "elo": 2718},
        {"name": "Maxime Vachier-Lagrave", "elo": 2717},
        {"name": "Yu Yangyi", "elo": 2717},
        {"name": "Shakhriyar Mamedyarov", "elo": 2715}
    ],
    
    "Pool_D": [  # Wildcards / Prodigies (< 2715) - Total: 10 players
        {"name": "Santosh Gujrathi Vidit", "elo": 2708},
        {"name": "Vladimir Fedoseev", "elo": 2703},
        {"name": "Matthias Bluebaum", "elo": 2695},
        {"name": "Yagiz Kaan Erdogmus", "elo": 2687},
        {"name": "Alexey Sarana", "elo": 2658},
        {"name": "Pranav V", "elo": 2657},
        {"name": "Alexander Donchenko", "elo": 2642},
        {"name": "Frederik Svane", "elo": 2640},
        {"name": "Ediz Gurel", "elo": 2635},
        {"name": "Thai Dai Van Nguyen", "elo": 2633}
    ]
}