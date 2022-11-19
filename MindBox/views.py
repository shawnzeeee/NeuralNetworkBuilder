import json
from django.http import JsonResponse 
from django.views.decorators.csrf import ensure_csrf_cookie
import numpy
import math
@ensure_csrf_cookie


def train(request):
        def sigmoid(num):
                return 1 / (1 + math.exp(-num))
#get initial training data
        rawData = request.GET.get('trainingData')
        rows = rawData.split('\n')
#create input array to put inside input matrix
        inputArr = []
        for i in range(len(rows)):
                newRow = rows[i].split(',')
                #del newRow[len(newRow)-1]
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
                #inputCol = numpy.array([[i] for i in numpy.zeros(outputLength+1)])
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
        layers[len(layers)-1]['activation'] = numpy.array([numpy.zeros(int(layers[len(layers)-1]['nodesLength']))])

        for i in range(int(rowLength)):
                layers[0]['activation'] = inputMatrix[i]
                for j in range(len(layers)-1):
                        inputActivation = numpy.add(numpy.matmul(layers[j]['activation'],layers[j]['weightMatrix']), layers[j]['bias'])
                        layers[j+1]['activation'] = numpy.array([sigmoid(i) for i in inputActivation[0]])
        #print(layers)


        return JsonResponse({"status": 'Success'}) 