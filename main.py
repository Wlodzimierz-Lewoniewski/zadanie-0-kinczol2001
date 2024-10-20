import string

def load_data():
    doc_count = int(input("Podaj liczbę dokumentów: "))
    docs = [input(f"Wprowadź dokument {i + 1}: ") for i in range(doc_count)]
    query_count = int(input("Podaj liczbę zapytań: "))
    query_list = [input(f"Wprowadź zapytanie {j + 1}: ").strip().lower() for j in range(query_count)]
    return docs, query_list

def count_word_occurrences(word, text):
    cleaned_text = ''.join(char.lower() if char not in string.punctuation else ' ' for char in text)
    word_list = cleaned_text.split()
    return word_list.count(word)

def find_query_matches(docs, queries):
    output = []
    for query in queries:
        cleaned_query = ''.join(char for char in query if char not in string.punctuation)
        doc_match_counts = [(idx, count_word_occurrences(cleaned_query, doc)) for idx, doc in enumerate(docs)]
        filtered_results = [entry for entry in doc_match_counts if entry[1] > 0]
        sorted_results = sorted(filtered_results, key=lambda item: (-item[1], item[0]))
        matched_indexes = [doc_index for doc_index, _ in sorted_results]
        output.append(matched_indexes)
    return output

def run_program():
    docs, queries = load_data()
    query_results = find_query_matches(docs, queries)
    print("\nWyniki dla wprowadzonych zapytań:")
    for res in query_results:
        print(res)

if __name__ == "__main__":
    run_program()

