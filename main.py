# Entry for make.fun bounty "The Excuse That Almost Works".
# Writes one line (max 140 chars, max 20 words) to /output/entry.txt.
#
# Judge criteria (from competition.yaml, most important first):
#   1. On-topic: an excuse a gamer sends a boss to skip work on GTA 6 launch week.
#   2. Almost believable: a real, specific, boring workplace detail, not a wild story.
#   3. Funny on its own terms: the laugh comes from the excuse's own logic/detail.
#   4. Reads like a hurried text: one line, plain words, no setup, no signature.
#   5. Fresh angle: not a dead grandmother, a flat tyre, or a sudden fever.
#   (A long excuse sounds rehearsed, and a rehearsed one is already a confession.)
#
# Four candidate lines of my own, scored 1-5 against the criteria above:
#
#   A. "Building's getting the water shut off Thursday for pipe work, landlord said no one can be home."
#      1:5  2:5  3:2  4:3  5:4  -> believable and boring, but flat; nobody laughs.
#   B. "My laptop picked today to run the big Windows update, says 3 hours, can't stop it."
#      1:5  2:5  3:4  4:4  5:5  -> a forced update is the one excuse every manager
#      has personally lived through; the humor is in the helplessness itself.
#   C. "Car's in the shop till Friday, they found the brake thing needs a part from another city."
#      1:5  2:3  3:2  4:3  5:1  -> too close to the flat-tyre cliche the brief warns against.
#   D. "Dentist moved my root canal to Thursday morning, whole side of my face will be numb."
#      1:5  2:4  3:3  4:3  5:3  -> specific and grim, but a boss just says "work from home then".
#
# Winner: B. It wins on criteria 2 and 5 outright -- a stuck forced update is
# boring, specific, and undeniable, and it is the rare excuse a manager cannot
# argue with because arguing does not unstick the laptop.

import os

LINE = "My laptop picked today to run the big Windows update, says 3 hours, can't stop it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
