def tordel(lst, n=None, indent=None):
    if n is None:
        n = 10
    if indent is None:
        indent = ''
    tordelt_sorok = []
    for i in range(0, len(lst), n):
        row = lst[i:i+n]
        tordelt_sorok.append(f"{indent}{', '.join(map(str, row))}")
    return "\n".join(tordelt_sorok)

