from graph.graph import RelationGraph
import sys

def usage():
    print("Usage: python search.py <model> (<start>|all) <goal> [corpus='Corpus']")

def run_all(graph):
    topics = [v.prop for v in graph.iter_vertex()]
    for a in topics:
        for b in topics:
            if a == b:
                continue
            path, path_weight = graph.search(a, b)
            print("{} -> {}".format(a, b))
            for t in path:
                print(t.prop)
            print("Weight", path_weight)
            

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
    if source == 'all':
        run_all(graph)
    elif graph.find_vertex(source) is not None:
        target = sys.argv[3]
        print(target)
        if graph.find_vertex(target) == None:
            print("Target not in model.")
            return

        path, path_weight = graph.search(source, target)
        for t in path:
            print(t.prop)

        print("Weight", path_weight)
    else:
        print("Source not in model.")
        return




if __name__ == '__main__':
    main()
