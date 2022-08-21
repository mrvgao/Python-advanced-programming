import ray
import random 
from ray import serve


def complicated_neural_network_model(text):
    """
    Pytorch implemented neural network
    """
    return random.choice(['dog', 'cat'])

ray.init(address="auto", namespace="serve")
serve.start(detached=True)

@serve.deployment
def router(request):
    txt = request.query_params["txt"]
    return summarize(txt)

    
if __name__ == '__main__':
    #result = complicated_neural_network_model('some test')
    #print(result)
    ## devlopment environment
    router.deploy()

