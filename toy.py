from utils import convert_to_json
from metric.evaluator import get_evaluator

task = 'summarization'

# a list of source documents
src_list = ['Peter and Elizabeth took a taxi to attend the night party in the city. \
             While in the party, Elizabeth collapsed and was rushed to the hospital.']
# a list of human-annotated reference summaries
ref_list = ['Elizabeth was hospitalized after attending a party with Peter.']
# a list of model outputs to be evaluataed
output_list = ['Peter and Elizabeth attend party city. Elizabeth rushed hospital.']

# Prepare data for pre-trained evaluators
data = convert_to_json(output_list=output_list, 
                       src_list=src_list, ref_list=ref_list)
# Initialize evaluator for a specific task
evaluator = get_evaluator(task)
# Get multi-dimensional evaluation scores
eval_scores = evaluator.evaluate(data, print_result=True)
