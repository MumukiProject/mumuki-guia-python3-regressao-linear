class Test(unittest.TestCase):

  def test_prever_resposta_20(self):
    self.assertAlmostEqual(prever_resposta(20), 85.05642088787117, 5)
    
  def test_prever_resposta_30(self):
    self.assertAlmostEqual(prever_resposta(30), 190.17295167042818, 5)
    
  def test_prever_resposta_15(self):
    self.assertAlmostEqual(prever_resposta(15), 32.49815549659269, 5)    