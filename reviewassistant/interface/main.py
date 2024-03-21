from reviewassistant.params import *


def generate_criteria(product_txt: str) -> list[str]:
    pass

def generate_reviews(rated_criteria: dict[str, int], num_reviews: int=3) -> str:
    pass


if __name__ == '__main__':
    product = input("Which product would you like a review for?\n ")
    criteria = generate_criteria(product)

    print("\nRate the following from 1 to 5:")
    rated_criteria = {
        int(input(f"{criterium.title()}? "))
        for criterium in criteria
    }
    print(rated_criteria)

    reviews = generate_reviews(rated_criteria)
    print("\nHere are some potential reviews:")
    for i, review in enumerate(reviews):
        if i > 0:
            print("---\n")
        print(review + '\n')
