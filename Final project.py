def get_set_input(set_name):
    while True:
        user_input = input(f"Enter the elements of set {set_name} separated by spaces: ")
        try:
            
            return set(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Please enter integers only.")

def main():
    print("Welcome to the Set Operations Program!")
    
    set_A = get_set_input('A')
    set_B = get_set_input('B')
    
    union = set_A.union(set_B)
    intersection = set_A.intersection(set_B)
    difference_A_B = set_A.difference(set_B)
    difference_B_A = set_B.difference(set_A)
    is_subset_A_B = set_A.issubset(set_B)
    is_subset_B_A = set_B.issubset(set_A)

    print("\nResults of Set Operations:")
    print(f"Set A: {set_A}")
    print(f"Set B: {set_B}")
    print(f"Union (A ∪ B): {union}")
    print(f"Intersection (A ∩ B): {intersection}")
    print(f"Difference (A − B): {difference_A_B}")
    print(f"Difference (B − A): {difference_B_A}")
    print(f"Is A a subset of B (A ⊆ B)? {'Yes' if is_subset_A_B else 'No'}")
    print(f"Is B a subset of A (B ⊆ A)? {'Yes' if is_subset_B_A else 'No'}")

if __name__ == "__main__":
    main()