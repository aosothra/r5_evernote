#!/usr/bin/env python 

import os
from distutils.util import strtobool

from dotenv import load_dotenv
from evernote.api.client import EvernoteClient

    
if __name__ == '__main__':
    load_dotenv()
    en_token = os.getenv('EVERNOTE_PERSONAL_TOKEN')
    en_is_sandbox = strtobool(os.getenv('EVERNOTE_IS_SANDBOX'))

    client = EvernoteClient(
        token=en_token,
        sandbox=en_is_sandbox
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print('%s - %s' % (notebook.guid, notebook.name))
