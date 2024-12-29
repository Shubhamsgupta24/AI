def backtracking_search(search_space, domain):
    color = {key: None for key in search_space}
    answer = []
    recursive_backtracking(color, search_space, domain, answer)
    return bool(answer)

def uncolored(color):
    for key in color:
        if color[key] is None:
            return key
    return None

def recursive_backtracking(color, search_space, domain, answer):
    uncolored_node = uncolored(color)
    if uncolored_node is None:
        answer.append(color.copy())
        print(color)
        return
    for color_option in domain:
        check = all(color_option != color[neighbor] for neighbor in search_space[uncolored_node])
        if check:
            color[uncolored_node] = color_option
            recursive_backtracking(color, search_space, domain, answer)
            color[uncolored_node] = None

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

    domain = ["Red", "Green", "Blue"]

    result = backtracking_search(search_space, domain)
    if result:
        print("These are the possible available solutions")
    else:
        print("Assignment of colors is not possible")

