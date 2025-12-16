class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(',')]

raw = "water , milk, tea leaves ,ginger "
cleaned_ingredients = ChaiUtils.clean_ingredients(raw)
print(cleaned_ingredients)