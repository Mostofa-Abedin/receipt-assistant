
# Imports
from parse import get_text, is_complete, total_tokens

# A Fake dataset
fake_data = {
    "content": [{"text": "Test receipt answer"}],
    "stop_reason": "max_tokens",
    "usage": {
        "input_tokens": 10,
        "output_tokens": 20
    }
}

# checks get_text returns the text you put in the fake

def test_get_text():
    assert get_text(fake_data) == "Test receipt answer"

# checks is_complete returns False for your fake

def test_is_complete_false_when_cut_off():
    assert is_complete(fake_data) == False

# checks the sum is right for the numbers you chose

def test_total_tokens():
    assert total_tokens(fake_data) == 30