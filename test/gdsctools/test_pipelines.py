from gdsctools.scripts import anova as pipelines
from gdsctools import  ic50_test

from nose.plugins.attrib import attr



class TestPipeline(object):

    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        klass.prog = "gdsctools"
        klass.filename = ic50_test.filename
        klass.params = {'prog': klass.prog, 'filename': klass.filename}

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_version(self):
        pipelines.main([self.prog, '--version'])

    def test_help(self):
        pipelines.main([self.prog, '--help'])
        pipelines.main([self.prog])

    def test_print_drug_names(self):
        pipelines.main([self.prog, '--input-ic50', self.filename,
            '--print-drug-names'])
    def test_print_tissue_names(self):
        pipelines.main([self.prog, '--input-ic50', self.filename,
            '--print-tissue-names'])
    def test_print_feature_names(self):
        pipelines.main([self.prog, '--input-ic50', self.filename,
            '--print-feature-names'])

    def test_odaf(self):
        pipelines.main([self.prog, '--input-ic50', self.filename,
            '--drug', '1047', '--no-html'])

    def test_odof(self):
        pipelines.main([self.prog, '--input-ic50', self.filename,
            '--drug', '1047', '--no-html', '--feature', 'TP53_mut'])
        pipelines.main([self.prog, '--input-ic50', self.filename,
            '--drug', '1047', '--feature', 'TP53_mut'])


    # slow takes about 30-60 seconds
    @attr('skip')
    def test_adaf(self):
        pipelines.main([self.prog, '--input-ic50', self.filename,
            '--no-html'])

    def test_license(self):
        pipelines.main([self.prog, '--license'])
    def test_summary(self):
        pipelines.main([self.prog, '--summary'])
    def test_summary(self):
        pipelines.main([self.prog, '--testing'])
