from girder.models.item import Item

from .meta import TCGAModel


class Pathology(TCGAModel, Item):

    TCGAType = 'pathology'

    def importDocument(self, doc, **kwargs):
        name = doc['name']
        tcga = self.parsePathology(name)
        self.setTCGA(doc, **tcga)

        return super(Pathology, self).importDocument(doc, **kwargs)
