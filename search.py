from graph.graph import RelationGraph
import sys

def usage():
    print("Usage: python search.py <model> <start> <goal> [corpus='Corpus']")

def main():
    if len(sys.argv) < 3:
        usage()
        exit(1)

    model_options = ['u','b','t','a','lu','ld']
    model = sys.argv[1]
    if model not in model_options:
        print("Please input a valid model.\nu-unigram\nb-bigram\nt-trigram\na-Article to Article\nl-Topic Locality")
        return
    if len(sys.argv) > 4:
        corpus = sys.argv[4]
        if corpus not in ['Corpus', 'MiniCorpus']:
            print('Please input a valid corpus (Corpus or MiniCorpus).')
            return
    else:
        corpus = 'Corpus'
    graph = RelationGraph()
    model_file = 'RelationModels/'
    if model == 'u':
        model_file += corpus+'Unigram.txt'
        graph.load_graph(model_file)
    elif model == 'b':
        model_file += corpus+'Bigram.txt'
        graph.load_graph(model_file)
    elif model == 't':
        model_file += corpus+'Trigram.txt'
        graph.load_graph(model_file)
    elif model == 'a':
        model_file += corpus+'AtoA.txt'
        graph.load_graph(model_file)
    elif model == 'ld':
        model_file += corpus+'TopicLocalityDirected.txt'
        graph.load_graph(model_file)
    elif model == 'lu':
        model_file += corpus+'TopicLocalityUndirected.txt'
        graph.load_graph(model_file)

    if len(graph.vertices) == 0:
        #TODO check if corpus exists and construct it if needed instead of quitting
        print("This model needs to be constructed first: " + model_file + ".")

        return
    source = sys.argv[2]
    if graph.find_vertex(source) == None:
        print("Source not in model.")
        return
    target = sys.argv[3]
    if graph.find_vertex(target) == None:
        print("Target not in model.")
        return

    path = graph.search(source, target)
    for t in path:
        print(t.prop)




if __name__ == '__main__':
    main()
