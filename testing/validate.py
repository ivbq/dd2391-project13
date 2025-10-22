import collections
import json
import os


def main():
    configs_per_hash = collections.defaultdict(list)

    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.json")
    with open(abs_path, "r") as output:
        for line in output:
            fingerprint = json.loads(line)
            h = fingerprint.get("hash")

            if h is not None:
                configs_per_hash[h].append(fingerprint)

    collisions = {
        h: configs for h, configs in configs_per_hash.items() if len(configs) > 1
    }

    if len(collisions.items()) > 0:
        print(f"Collisions found: {collisions}")
    else:
        print("No collisions found!")

    # Analyze hash distribution
    hashes = configs_per_hash.keys()

    # Count hashes by first 2 characters to show distribution
    prefix_counts = collections.Counter(h[:2] for h in hashes if len(h) >= 2)

    used_buckets = len(prefix_counts)
    print(
        f"{len(hashes)} unique hashes spread across {used_buckets}/256 possible prefixes"
    )
    print(f"Average: {len(hashes) / used_buckets:.1f}")

    if len(hashes) > 1000:
        print("Low probability of collisions.")
    else:
        print("Non-negligible possibility of collisions.")


if __name__ == "__main__":
    main()
