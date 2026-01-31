from collections import Counter

def analyze_log(file_path):
    levels = []

    with open(file_path, 'r') as file:
        for line in file:
            level = line.split()[0]
            levels.append(level)

    counts = Counter(levels)
    return counts

if __name__ == "__main__":
    results = analyze_log("sample_log.txt")

    print("Log Summary:")
    for level, count in results.items():
        print(f"{level}: {count}")
