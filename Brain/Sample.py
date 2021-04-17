import Brain.NNModules as nnm


nn_image = nnm.ImageNetwork()
if nnm.INNNetwork.providedBy(nn_image):
    nn_image.GetData()
    nn_image.Teach()
    nn_image.Test()