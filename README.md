# r5_evernote

This toolset can be used as an application, that provides subpar management means to your Evernote account.

Each script implements it's own basic function as follows:
- `list_notebooks.py` - outputs all existing Evernote notebooks into terminal.
- `add_note2journal.py` - creates new empty note titled with specific date. 
- `dump_inbox.py` - outputs contents of your notes from specific notebook into terminal.

## Installation guidelines

Means of access to remote Evernote account are implemented through python [Evernote SDK](https://pypi.org/project/evernote/). It was intended for use with *Python 2.X*, so it is recommended to follow that requirement.

Make sure you have python2 installed on your system:

```
> python2 -V
```

It is also advised to use [virtual environment](https://docs.python-guide.org/dev/virtualenvs/) for project isolation.

Once set up, install all prerequisites using `pip` (you might need to upgrade your `pip` for that)

```
> pip install -r requirements.txt
```

### Setting up your project environment

This script expects `.env` file in root of your project to load environment variables.

Core variables that has to be defined are listed below:

`EVERNOTE_PERSONAL_TOKEN` - is a string, representing your Evernote API access token. Proper personal token acquisition is done using *OAuth* and is not covered in scope of this project. 

If you posses means to get one, it will work just fine. However, for our purposes we will use a developer token for Evernote Sandbox. Follow [Evernote Cloud API Tutorial](https://dev.evernote.com/doc/articles/dev_tokens.php) in order to acquire it.

`EVERNOTE_IS_SANDBOX` - is a boolean flag, that indicates which endpoint must be used by our python client. Set to `True` if you've followed our guidelines and got a sandbox developer token. For production access this flag has to be set to `False`.

In order to use `dump_inbox.py` and `add_note2journal.py` - you must specify a `GUID`'s of your notebooks and notes.

You can get `GUID` values of your notebooks and notes using Evernote web client, just by opening them and deducing the URL address in your browser. Looking through URL fragment part (after `#`) you'll see list of `key=value` pairs separated by `&` symbol.

Look for key `b` - use value it is paired with as this notebook's `GUID`. You can deduce `GUID` of a note in a similar fashion, by looking for a value paired with `n` key, when the note is open in your web client.

`INBOX_NOTEBOOK_GUID` - is a string that is suppossed to represent your default notebook, which stores all notes coming over inbox e-mail.

`JOURNAL_NOTEBOOK_GUID` - is a string that represents your *journal* notebook, which will store notes created by our `add_note2journal.py` script. You might as well use your default notebook for that purpose, or create a separate one. That is up to you.

`JOURNAL_TEMPLATE_NOTE_GUID` - is a string that represents a *template* note, that we will use to create journal entries. This *template* note must be created manually.

The easiest way to do that is through Evernote web client. Create a new note in the notebook, that you have specified / will specify as your `JOURNAL_NOTEBOOK_GUID`. When you are prompted to set title of newly created note, input following value:

```Python
{date} {dow} # this is our journal template
```
Save it and leave it at that. Every time when you're going to use `add_note2journal.py` - it will create a copy of this note, substituting variables in curly braces with actual values, and part after `#` will be ommited. Make sure you note the `GUID` (no pun intended) of the newly created *template* note and save it in `JOURNAL_TEMPLATE_NOTE_GUID`.

At the end of environment configuration your `.env` file will look similar to that:

```
EVERNOTE_IS_SANDBOX = True
EVERNOTE_PERSONAL_TOKEN = 'painfully-long-string=that-is-your-access-token'

JOURNAL_NOTEBOOK_GUID = 'your-journal-notebook-guid'
JOURNAL_TEMPLATE_NOTE_GUID = 'your-journal-template-guid'
INBOX_NOTEBOOK_GUID = 'your-inbox-notebook-guid'
```

## Basic usage

Now the time has come, when all is set and done. You may use the scripts provided by this toolset:

```
> python2 list_notebooks.py
```

Outputs all your Evernote notebooks into terminal as `GUID - name` pairs.

```
> python2 add_note2journal.py
```

Creates a journal entry note by copying and substituting the template note. This one can take one optional parameter that can be:

- date in the following format: `%Y-%m-%d`
- time delta in days from current date represented by integer value.
- ommited. Default value is current date.

Substitution will replace `{date}` with the date provided as parameter, and `{dow}` will be set as day of the week this date falls upon. You can refer to usage example below:

```
> python2 add_note2journal.py 2023-10-11
Title Context is:
{
    "date": "2023-10-11", 
    "dow": "среда"
}
Note created: 2023-10-11 среда
Done

> python2 add_note2journal.py +3
Title Context is:
{
    "date": "2022-05-02", 
    "dow": "понедельник"
}
Note created: 2022-05-02 понедельник
Done
```

Last but not least:

```
> python2 dump_inbox.py
```

Will output text contents of notes in your inbox notebook. This can take one optional integer parameter, that specifies how many notes to print. Default is 10.

# Project goals

This project was refactored for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.