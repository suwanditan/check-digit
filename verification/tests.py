"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "799 273 9871",
            "answer": ["3", 67],
            "explanation": ["1789372997", [2, 7, 7, 9, 6, 7, 4, 9, 9, 7]]
        },
        {
            "input": "139-MT",
            "answer": ["8", 52],
            "explanation": ["TM931", [9, 29, 9, 3, 2]]
        },
        {
            "input": "123",
            "answer": ["0", 10],
            "explanation": ["321", [6, 2, 2]]
        },
        {
            "input": "999_999",
            "answer": ["6", 54],
            "explanation": ["999999", [9, 9, 9, 9, 9, 9]]
        },
        {
            "input": "+61 820 9231 55",
            "answer": ["3", 37],
            "explanation": ["55132902816", [1, 5, 2, 3, 4, 9, 0, 2, 7, 1, 3]]
        },
        {
            "input": "VQ/WEWF/NY/8U",
            "answer": ["9", 201],
            "explanation": ["U8YNFWEWQV", [11, 8, 10, 30, 8, 39, 6, 39, 12, 38]]
        },
        {
            "input": "YOUR_CHECKSUM",
            "answer": ["3", 247],
            "explanation": ["MUSKCEHCRUOY", [13, 37, 7, 27, 11, 21, 12, 19, 14, 37, 8, 41]]
        },
        {
            "input": "4002 1265 7021 069",
            "answer": ["3", 47],
            "explanation": ["960120756212004", [9, 6, 0, 1, 4, 0, 5, 5, 3, 2, 2, 2, 0, 0, 8]]
        },
        {
            "input": "324 217 69",
            "answer": ["4", 36],
            "explanation": ["96712423", [9, 6, 5, 1, 4, 4, 4, 3]]
        }

    ],
    "Extra": [
        {
            "input": "ROB-L3MPLSE",
            "answer": ["9", 171],
            "explanation": ["ESLPM3LBOR", [6, 35, 11, 32, 13, 3, 11, 18, 8, 34]]
        },
        {
            "input": "EK_8XO5_V9T8",
            "answer": ["2", 168],
            "explanation": ["8T9V5OX8KE", [7, 36, 9, 38, 1, 31, 8, 8, 9, 21]]
        },
        {
            "input": "00000000EK8XO5V9T8",
            "answer": ["2", 168],
            "explanation": ["8T9V5OX8KE00000000", [7, 36, 9, 38, 1, 31, 8, 8, 9, 21, 0, 0, 0, 0, 0, 0, 0, 0]]
        },
        {
            "input": "Y9 IDV 90 NVK",
            "answer": ["1", 179],
            "explanation": ["KVN09VDI9Y", [9, 38, 6, 0, 9, 38, 4, 25, 9, 41]]
        },
        {
            "input": "OBYY/3/LXR/79",
            "answer": ["5", 175],
            "explanation": ["97RXL3YYBO", [9, 7, 14, 40, 11, 3, 10, 41, 9, 31]]
        },
        {
            "input": "6/KWK/DFD/79-A",
            "answer": ["8", 132],
            "explanation": ["A97DFDKWK6", [7, 9, 5, 20, 8, 20, 9, 39, 9, 6]]
        },
        {
            "input": "HXNPKG_Y4_EX",
            "answer": ["3", 187],
            "explanation": ["XE4YGKPNXH", [8, 21, 8, 41, 10, 27, 10, 30, 8, 24]]
        },
        {
            "input": "225-010-08",
            "answer": ["1", 19],
            "explanation": ["80010522", [7, 0, 0, 1, 0, 5, 4, 2]]
        },
        {
            "input": "45T/PECU/WKJ/",
            "answer": ["1", 169],
            "explanation": ["JKWUCEPT54", [7, 27, 15, 37, 11, 21, 10, 36, 1, 4]]
        }
    ]
}
