
# Claude's answer text
def get_text(data):
    claude_answer = data['content'][0]['text']
    return claude_answer

# True if the stop reason is end_turn, otherwise False

def is_complete(data):
    if data['stop_reason'] == "end_turn":
        complete = True
    else:
        complete = False

    return complete

# input tokens plus output tokens, as one number

def total_tokens(data):
    total = data['usage']['input_tokens'] + data['usage']['output_tokens']
    return total