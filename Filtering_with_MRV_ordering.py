def MRV(search_space, domain):
    color = {key: None for key in search_space}
    answer = []
    rec(search_space, domain, color, answer)
    return bool(answer)

def find_min(domain, color):
    curr = None
    min_var = float('inf')
    for key in domain:
        if color[key] is None and len(domain[key]) < min_var:
            min_var = len(domain[key])
            curr = key
    return curr

def rec(search_space, domain, color, answer):
    curr = find_min(domain, color)
    if curr is None:
        answer.append(color.copy())
        print(color)
        print()
        return

    curr_domain = list(domain[curr])
    for color_option in curr_domain:
        color[curr] = color_option
        for neighbor in search_space[curr]:
            if color[neighbor] is None and color_option in domain[neighbor]:
                domain[neighbor].remove(color_option)
        rec(search_space, domain, color, answer)
        for neighbor in search_space[curr]:
            if color[neighbor] is None and color_option not in domain[neighbor]:
                domain[neighbor].append(color_option)
        color[curr] = None

if __name__ == "__main__":
    search_space = {
        "Estonia": ["Latvia", "Russia"],
        "Russia": ["Estonia", "Latvia", "Belarus"],
        "Latvia": ["Estonia", "Russia", "Belarus", "Lithuania"],
        "Lithuania": ["Latvia", "Belarus", "Kaliningrad", "Poland"],
        "Belarus": ["Russia", "Latvia", "Lithuania", "Poland"],
        "Poland": ["Kaliningrad", "Lithuania", "Belarus"],
        "Kaliningrad": ["Lithuania", "Poland"]
    }

    domain = {
        "Estonia": ["Red", "Blue", "Green"],
        "Russia": ["Red", "Blue", "Green"],
        "Latvia": ["Red", "Blue", "Green"],
        "Lithuania": ["Red", "Blue", "Green"],
        "Belarus": ["Red", "Blue", "Green"],
        "Poland": ["Red", "Blue", "Green"],
        "Kaliningrad": ["Red", "Blue", "Green"]
    }

    result = MRV(search_space, domain)
    if result:
        print("These are the possible solutions")
    else:
        print("Assignment of colors is not possible")

