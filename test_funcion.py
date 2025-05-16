from diagnosticos import enfermedad1
def test_enfermedad():
  assert test_enfermedad(110,79,90,37) == 'NO ENFERMO'
  assert test_enfermedad(110,79,90,38) == 'ENFERMEDAD LEVE'
#  assert test_enfermedad(110,79,101,37) == 'ENFERMEDAD AGUDAAAAAA'
  assert test_enfermedad(121,79,90,37) == 'ENFERMEDAD CRÓNICA'
  
