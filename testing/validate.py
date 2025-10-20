from collections import defaultdict
import json

def main():
    configs_per_hash = defaultdict(list)

    with open("output.json", "r") as output:
        for line in output:
            fingerprint = json.loads(line)
            h = fingerprint.get("hash")

            if h is not None:
                configs_per_hash[h].append(fingerprint)

    collisions = {}
    for h, configs in configs_per_hash.items():
        if len(configs) > 1:
            collisions[h] = configs

    if len(collisions.items()) > 0:
        print(f"Collisions found: {collisions}")
    else:
        print("No collisions found!")

if __name__ == "__main__":
    main()