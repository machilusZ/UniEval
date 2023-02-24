import sys
import csv
from utils import convert_to_json
from metric.evaluator import get_evaluator

def read_data(filename, chunksize=10):
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)
        chunk = []
        id_list = []
        out_list = []
        src_list = []
        for i, row in enumerate(reader):
            id_list.append(row[0])
            out_list.append(row[1])
            src_list.append(row[2])
            if (i+1) % chunksize == 0:
                ref_list = ['' for _ in range(chunksize)]
                yield convert_to_json(output_list=out_list,
                                      src_list=src_list,
                                      ref_list=ref_list,
                                      id_list=id_list)
                id_list = []
                out_list = []
                src_list = []
        if id_list:
            yield convert_to_json(output_list=out_list,
                                  src_list=src_list,
                                  ref_list=ref_list,
                                  id_list=id_list)

task = 'summarization'
evaluator = get_evaluator(task)

input_path = sys.argv[1]
output_path = sys.argv[2]

header = ["id", "coherence", "consistency", "fluency", "relevance", "overall"]
with open(output_path, "w") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)

for chunk in read_data(input_path, chunksize=10):
    results = evaluator.evaluate(chunk,print_result=False)
    with open(output_path, "a") as f:
        writer = csv.writer(f, delimiter="\t")
        for result in results:
            writer.writerow([result[key] for key in header])
