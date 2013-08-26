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
            "explanation": "First Test"
        },
        {
            "input": "139-MT",
            "answer": ["8", 52],
            "explanation": "Second Test"
        },
        {
            "input": "123",
            "answer": ["0", 10],
            "explanation": "Test for zero"
        },
        {
            "input": "999_999",
            "answer": ["6", 54],
            "explanation": "Third Test"
        },
        {
            "input": "+61 820 9231 55",
            "answer": ["3", 37],
            "explanation": "Fourth Test"
        },
        {
            "input": "VQ/WEWF/NY/8U",
            "answer": ["9", 201],
            "explanation": "Fifth Test"
        },
        {
            "input": "YOUR_CHECKSUM",
            "answer": ["3", 247],
            "explanation": "Sixth Test"
        },
        {
            "input": "4002 1265 7021 069",
            "answer": ["3", 47],
            "explanation": "Seventh Test"
        },
        {
            "input": "324 217 69",
            "answer": ["4", 36],
            "explanation": "Eight Test"
        }

    ],
    "Extra": [
        {
            "input": "ROB-L3MPLSE",
            "answer": ["9", 171],
            "explanation": "Test 1"
        },
        {
            "input": "EK_8XO5_V9T8",
            "answer": ["2", 169],
            "explanation": "Test 2"
        },
        {
            "input": "00000000EK8XO5V9T8",
            "answer": ["2", 169],
            "explanation": "zero padding no effect"
        },
        {
            "input": "Y9 IDV 90 NVK",
            "answer": ["1", 179],
            "explanation": "Test 3"
        },
        {
            "input": "OBYY/3/LXR/79",
            "answer": ["5", 175],
            "explanation": "Test 4"
        },
        {
            "input": "6/KWK/DFD/79-A",
            "answer": ["8", 132],
            "explanation": "Test 5"
        },
        {
            "input": "HXNPKG_Y4_EX",
            "answer": ["3", 187],
            "explanation": "Test 6"
        },
        {
            "input": "225-010-08",
            "answer": ["1", 19],
            "explanation": "Test 7"
        },
        {
            "input": "45T/PECU/WKJ/",
            "answer": ["1", 169],
            "explanation": "Test 8"
        }
    ]
}
