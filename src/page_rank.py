import snap


def page_rank():
    graph = load_graph()

    page_rank_h = snap.TIntFltH()
    snap.GetPageRank(graph, page_rank_h)
    with open('output.txt', 'w') as output_file:
        for item in page_rank_h:
            print item, page_rank_h[item]

            output_file.write(str(page_rank_h.GetKey(item)))
            output_file.write(' ')
            output_file.write(str(page_rank_h[item]))
            output_file.write('\n')


def load_graph():
    graphfilename = "input.txt"

    schema = snap.Schema()
    context = snap.TTableContext()
    schema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
    schema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
    sample_table = snap.TTable.LoadSS(
        schema, graphfilename, context, " ", snap.TBool(False))

    graph = snap.ToGraph(snap.PNGraph, sample_table,
                         "srcID", "dstID", snap.aaFirst)

    return graph


def main():
    page_rank()


if __name__ == '__main__':
    main()
