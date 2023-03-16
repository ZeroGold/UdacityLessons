### my code

####


# Activation (sigmoid) function
def sigmoid(x):
    ### THE ERROR WAS HERE
    ### IT SHOULD BE (1 + NP.EXP(-X) BECAUSE 1/1 WILL COMPILE FIRST DUE TO PEMDAS
    return 1/1+np.exp(-x)




# Output (prediction) formula
def output_formula(features, weights, bias):
    #USE NP.DOT FOR THIS OPERATION BECAUSE IT DOESN'T WORK ANY OTHER WAY
    # LOOK INTO NP.DOT FOR THE REASON WHY.
    return sigmoid(np.dot(features, weights) + bias)
    
# Error (log-loss) formula
def error_formula(y, output):
    return -y*np.log(output)-(1-y)*np.log(1-output)
    
# Gradient descent step
def update_weights(x, y, weights, bias, learnrate):
    y_hat = output_formula(x,weights,bias)
    weights = weights + learnrate*(y-y_hat)*x
    bias = bias + learnrate*(y-y_hat)
    return weights, bias






### Their code

# Activation (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def output_formula(features, weights, bias):
    return sigmoid(np.dot(features, weights) + bias)

def error_formula(y, output):
    return - y*np.log(output) - (1 - y) * np.log(1-output)

def update_weights(x, y, weights, bias, learnrate):
    output = output_formula(x, weights, bias)
    d_error = -(y - output)
    weights -= learnrate * d_error * x
    bias -= learnrate * d_error
    return weights, bias
