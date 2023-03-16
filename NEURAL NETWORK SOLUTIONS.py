##NOT RUNNABLE IN CURRENT STATE

## Your solution

def activation(x):
    val = 1 /(1 + np.exp(-x))
    return val

hidden = 256
out = 10
    
images = images.reshape(64,784)

##or
i = images.view(images.shape[0],-1)


### IMPORTANT THING HERE, WHEN PERFORMING MATRIX MULTIPLICATION
### LAYERS OUT HAVE TO MATCH LAYERS IN
## 784 TO 784 THEN IF 784 EXITS AS 10, 10 TO 10

W1 = torch.randn(images.shape[1], hidden)
W2 = torch.randn(hidden,out)
B1 = torch.randn((1, hidden))
B2 = torch.randn((1, out))



### IMPORTANT THING TO NOTE

##ACTIVATE THE FIRST LAYER

## THEN ONLY PERFORM MATRIX MULTIPLICATION ON THE SECOND LAYER
h = activation(torch.mm(images,W1)+B1)
output = torch.mm(h,W2)+B2
print(output.size())



