from gdsctools.datasets import Data
from gdsctools import datasets

def test_data():

    d = Data()
    d.description= 'toto'
    d.authors = 'toto'
    d.filename = 'here'
    print(d)

    # here we just try to access to the data, we do not use them
    datasets.ic50_test
    datasets.genomic_features
    datasets.drug_test
    datasets.cancer_cell_lines 
