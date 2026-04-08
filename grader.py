def grade(response, expected):
    response = response.lower()
    if expected in response:
        return 1.0
    return 0.0