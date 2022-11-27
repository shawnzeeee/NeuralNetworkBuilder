import json
from django.http import JsonResponse 
from django.views.decorators.csrf import ensure_csrf_cookie
import numpy
import math
@ensure_csrf_cookie


def train(request):
        def sigmoid(num):
                return 1 / (1 + math.exp(-num))
        def diffSigmoid(num):
                return sigmoid(num) * (1 - sigmoid(num)) 
        
#get initial training data
        rawData = request.GET.get('trainingData')
        rows = rawData.split('\n')
#create input array to put inside input matrix
        inputArr = []
        for i in range(len(rows)):
                newRow = rows[i].split(',')
                if '?' not in newRow and '' not in newRow:
                        newRow = [float(i) for i in newRow]
                        inputArr.append(newRow)
        del inputArr[len(inputArr)-1]
        inputMatrix = numpy.array(inputArr, dtype = float)
#get dimensions of matrix
        colLength = str(inputMatrix.shape).replace('(','').replace(')','').split(',')[1]
        rowLength = str(inputMatrix.shape).replace('(','').replace(')','').split(',')[0]
#scaling input values to between 0,1
        for i in range(int(colLength)-1):
                scale = numpy.max(inputMatrix[:,i])
                inputMatrix[:,i] = numpy.divide(inputMatrix[:,i],int(scale))
#creating the input layer
        layers = [{'type': 'Input Layer', 'nodesLength': int(colLength)-1}]
#adding hidden layers
        layers += json.loads(request.GET.get('layers'))
#creating output layer
        outputVector = numpy.array([int(i) for i in inputMatrix[:,int(colLength)-1]])
        outputLength = numpy.max(outputVector) +1
        outputArr = []
        for i in range(len(outputVector)):
                index = outputVector[i]
                inputRow = numpy.zeros(outputLength)
                inputRow[index] = 1
                outputArr.append(inputRow)
        layers.append({'type': 'Output Layer', 'nodesLength': outputLength})
        outputMatrix = numpy.array(outputArr)
        inputMatrix = numpy.delete(inputMatrix,int(colLength)-1, 1)
        for i in range(len(layers)-1):
                if i == len(layers)-2:
                        layers[i]['weightMatrix'] = numpy.random.uniform(-2,2,(int(layers[i]['nodesLength']), outputLength))
                else:
                        layers[i]['weightMatrix'] = numpy.random.uniform(-2,2,(int(layers[i]['nodesLength']),int(layers[i+1]['nodesLength'])))
                layers[i]['activation'] = numpy.array([numpy.zeros(int(layers[i]['nodesLength']))])
                layers[i]['bias'] = numpy.random.uniform(-2,2,(1,int(layers[i+1]['nodesLength'])))
                layers[i]['weightGradientAverage'] = numpy.zeros(layers[i]['weightMatrix'].shape)
                layers[i]['biasGradientAverage'] = numpy.zeros(layers[i]['bias'].shape)
        layers[len(layers)-1]['activation'] = numpy.array([numpy.zeros(int(layers[len(layers)-1]['nodesLength']))])
   

        for i in range(int(rowLength)):
                layers[0]['activation'] = numpy.array([inputMatrix[i]])
                for j in range(len(layers)-1):
                        sigmoidActivation = numpy.array([sigmoid(node) for node in layers[j]['activation'][0]])
                        inputActivation = numpy.add(numpy.matmul(sigmoidActivation,layers[j]['weightMatrix']), layers[j]['bias'])
                        layers[j+1]['activation'] = numpy.array(inputActivation)
                #backprobagation
                sigmoidActivation = numpy.array([sigmoid(node) for node in layers[len(layers)-1]['activation'][0]])
                costFunction = numpy.array([numpy.power(numpy.subtract(sigmoidActivation, outputMatrix[i]),2)])
                delta = numpy.multiply(costFunction, numpy.array([diffSigmoid(i) for i in outputMatrix[i]]))
                k = len(layers)-2

                while k >= 0:
                        weightGradientInput = []
                        for i in delta[0]:
                                weightGradientInput.append(numpy.multiply(layers[k]['activation'][0],i))
                        weightGradientInput = numpy.transpose(numpy.array(weightGradientInput))
                        layers[k]['weightGradientAverage'] = numpy.add(layers[k]['weightGradientAverage'],weightGradientInput)
                        #print(numpy.transpose(layers[k]['weightMatrix']).shape,delta.shape)
                        delta = numpy.multiply(numpy.matmul(delta, numpy.transpose(layers[k]['weightMatrix'])), [diffSigmoid(node) for node in layers[k]['activation'][0]])
                        k -= 1
        
                        
        return JsonResponse({"status": 'Success'}) 