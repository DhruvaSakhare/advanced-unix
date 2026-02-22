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
    main()def combined_score(numbers):
    return sum(numbers)


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

            scores = list(map(float, parts[1:]))

            score = combined_score(scores)
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
    main()def combined_score(numbers):
    return sum(numbers)


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
            
            # Works for any number of scores
            scores = list(map(float, parts[1:]))

            score = combined_score(scores)
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
    main()def average_score(numbers):
    return sum(numbers) / len(numbers)


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

            scores = list(map(float, parts[1:]))

            # 🔹 CHANGED HERE
            score = average_score(scores)

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
    main()def weighted_combined_score(numbers):
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
    main()def sliding_weighted_score(numbers, B=1.5, E=0.5):
    """
    B = beginning weight
    E = ending weight
    """
    total = 0
    N = len(numbers)

    for i, value in enumerate(numbers):
        P = i + 1  # position (1-based index)

        if N == 1:
            weight = 1.0  # avoid division by zero
        else:
            weight = B - (B - E) * (P - 1) / (N - 1)

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

            score = sliding_weighted_score(scores)

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
    main()def sliding_weighted_score(numbers, B=1.5, E=0.5):
    """
    B = beginning weight
    E = ending weight
    """
    total = 0
    N = len(numbers)

    for i, value in enumerate(numbers):
        P = i + 1  # position (1-based index)

        if N == 1:
            weight = 1.0  # avoid division by zero
        else:
            weight = B - (B - E) * (P - 1) / (N - 1)

        total += value * weight

    return total

def combined_score(numbers):
    return sum(numbers)

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

            score = combined_score(scores)

            results.append((score, line.strip()))

    # Sort high → low
    results.sort(reverse=True, key=lambda x: x[0])

    top10 = results[:10]

    with open("scoresextreme.txt", "w") as out:
        for _, line in top10:
            out.write(line + "\n")


if __name__ == "__main__":
    main()import heapq


def sliding_weighted_score(numbers, B=1.5, E=0.5):
    """
    B = beginning weight
    E = ending weight
    """
    total = 0
    N = len(numbers)

    for i, value in enumerate(numbers):
        P = i + 1  # position (1-based index)

        if N == 1:
            weight = 1.0  # avoid division by zero
        else:
            weight = B - (B - E) * (P - 1) / (N - 1)

        total += value * weight

    return total

def combined_score(numbers):
    return sum(numbers)

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

    heap = []

    with open("scores.txt") as f:
        for line in f:
            parts = line.strip().split("\t")

            accession = parts[0]

            # Skip banned genes
            if accession in banned_accessions:
                continue

            scores = [float(x) for x in parts[1:]]
            score = combined_score(scores)

            if len(heap) < 10:
                heapq.heappush(heap, (score, line.strip()))
            else:
                heapq.heappushpop(heap, (score, line.strip()))

    # Sort final 10 high → low
    top10 = sorted(heap, reverse=True)

    with open("scoresextreme.txt", "w") as out:
        for _, line in top10:
            out.write(line + "\n")


if __name__ == "__main__":
    main()