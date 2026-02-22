def combined_score(numbers):
    return sum(numbers)


def main():
    results = []

    with open("scores.txt") as f:
        for line in f:
            parts = line.strip().split("\t")
            accession = parts[0]
            scores = list(map(float, parts[1:]))

            score = combined_score(scores)
            results.append((score, line.strip()))

    # Sort by score descending
    results.sort(reverse=True, key=lambda x: x[0])

    top10 = results[:10]
    bottom10 = results[-10:]

    final = top10 + bottom10

    with open("scoresextreme.txt", "w") as out:
        for _, line in final:
            out.write(line + "\n")


if __name__ == "__main__":
    main()