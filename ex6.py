def weighted_combined_score(numbers):
    total = 0
    n = len(numbers)

    for i, value in enumerate(numbers):
        if i == 0:
            weight = 1.5          
        elif i == n - 1:
            weight = 0.5          
        else:
            weight = 1.0          

        total += value * weight

    return total


def load_translation(filename):
    mapping = {}

    with open(filename) as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                accession = parts[0]
                swissprot = parts[1]
                mapping[swissprot] = accession

    return mapping


def load_banned_accessions(negative_file, translation_map):
    banned_accessions = set()

    with open(negative_file) as f:
        for line in f:
            swissprot_id = line.strip()

            if swissprot_id in translation_map:
                banned_accessions.add(translation_map[swissprot_id])

    return banned_accessions


def main():
    translation_map = load_translation("translation.txt")
    banned_accessions = load_banned_accessions(
        "negative_list.txt",
        translation_map
    )

    results = []

    with open("scores.txt") as f:
        for line in f:
            parts = line.strip().split("\t")

            accession = parts[0]

            # Skip banned genes
            if accession in banned_accessions:
                continue

            scores = [float(x) for x in parts[1:]]

            score = weighted_combined_score(scores)

            results.append((score, line.strip()))

    # Sort high → low
    results.sort(reverse=True, key=lambda x: x[0])

    top10 = results[:10]
    bottom10 = results[-10:]

    final = top10 + bottom10

    with open("scoresextreme.txt", "w") as out:
        for _, line in final:
            out.write(line + "\n")


if __name__ == "__main__":
    main()