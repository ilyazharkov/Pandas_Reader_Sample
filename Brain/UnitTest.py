import unittest
import Brain.NNModules as nnm


class MyTestCase(unittest.TestCase):
    def main_test(self):
        nn_image = nnm.ImageNetwork()
        if nnm.INNNetwork.providedBy(nn_image):
            nn_image.GetData()
            nn_image.Teach()
            nn_image.Test()



if __name__ == '__main__':
    unittest.main()
