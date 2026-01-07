"""
Carbon Calculator (Oak vs Pine)

This is a learning-focused Python calculator that replicates the basic idea
of a Python tool used during an earlier environmental field study.
"""

def carbon_index(height_m: float, canopy_diameter_m: float) -> float:
    # Simple comparison score (not a scientific sequestration model)
    return height_m * (canopy_diameter_m ** 2)


def read_positive_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number (example: 12.5).")


def get_tree_inputs(label: str) -> tuple[float, float]:
    print(f"\nEnter measurements for {label}:")
    height = read_positive_float("  Height (meters): ")
    canopy = read_positive_float("  Canopy diameter (meters): ")
    return height, canopy


def main():
    print("=== Carbon Calculator (Oak vs Pine) ===")
    print("Compares a simple carbon index using height and canopy diameter.\n")

    oak_h, oak_c = get_tree_inputs("Oak")
    pine_h, pine_c = get_tree_inputs("Pine")

    oak_score = carbon_index(oak_h, oak_c)
    pine_score = carbon_index(pine_h, pine_c)

    print("\n--- Results ---")
    print(f"Oak carbon index : {oak_score:.2f}")
    print(f"Pine carbon index: {pine_score:.2f}")

    if oak_score > pine_score:
        print("\nBased on this index, Oak > Pine.")
    elif pine_score > oak_score:
        print("\nBased on this index, Pine > Oak.")
    else:
        print("\nBased on this index, Oak and Pine are equal.")

    print("\nNote: simplified tool for comparison (learning-focused).")


if __name__ == "__main__":
    main()
