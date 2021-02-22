import json
import random

file_name = "jeopardy.json"
rows_to_load = 200
filter_keys = ['question', 'answer', 'value']
by_category = {}


def load_file():
    """ ingest the raw data, filter for the items we want, and organize it by category"""
    return json.loads(open(file=file_name, mode="r").read())


def get_me_rows_from_file(row_count=rows_to_load):
    """Get x number of first rows."""
    return file_contents[:row_count]


def get_questions(category):
    """Returns all questions from the dataset that match the given category"""
    return by_category.get(str.upper(category), [])


def get_question(category):
    """ Returns  random question (question text only) from the given category"""
    return random.choice(get_questions(category))


def categorize_questions():
    """Adds category with questions."""
    for item in get_me_rows_from_file():
        # Demo 2: n, c, q
        # import pdb; pdb.set_trace()
        category = item['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append({key: item[key] for key in filter_keys})


# Bonus: b (Adds break point on the run.)
# import pdb; pdb.set_trace()
file_contents = load_file()
categorize_questions()


# Demo 1: l (list), p (print), pp (pretty print)
# import pdb; pdb.set_trace()


def get_input_from_user():
    """Gets an input from the user."""
    for idx, category in enumerate(by_category.keys()):
        print("{0}. {1}".format(idx, category))
    return input("=> Select a category: ") or 'ARCHITECTS'


category = get_input_from_user()
# Demo 3: s, r
# import pdb; pdb.set_trace()
question = get_question(category)
print('Here is your question about "{0}": {1}'.format(category, question["question"]))
