# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError, NoArgsCommand
from archivio.models import *
from baldessari_sketch import settings
import datetime
import json
from StringIO import StringIO
import re
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

def addMateriali(self):

    file = open(os.path.join(FILE_PATH, 'disegni-final.json'), 'r')
    docContent = StringIO(file.read())
    docDict = json.load(docContent)   #this dict will be updated with the content of docsDict
    file.close()
    
    # date variables
    
    for doc in docDict:
        print doc['segnatura']
        try:
            p = Drawing.objects.get(segnatura = doc['segnatura'])
            p.attivita = doc['Attivita']
            p.save()
            print ("doc esistente: " + doc['segnatura'])
    
        except Exception,e:     # doc does not exist
            print e
        
    

class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        addMateriali(self)