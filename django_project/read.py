from google.cloud import storage
import pandas as pd

col_names = [
    'ZIP',
    'Asthma',
    'Cardiovascular Disease'
]

def func():
    disadvantage_data = pd.read_csv('gs://disadvantage_data/sb535dacsces32018update.csv', usecols=col_names)
    disadvantage_data = disadvantage_data.set_index('ZIP')
    disadvantage_data = disadvantage_data.sort_index()
    disadvantage_data = disadvantage_data.groupby(level=0)
    disadvantage_data = disadvantage_data.agg({'Asthma':'mean', 'Cardiovascular Disease':'mean'})

    def calc_score(zip, age):
        asthma = 0
        card = 0
        if zip in disadvantage_data.index.values:
            asthma = disadvantage_data.at[zip, 'Asthma']
            card = disadvantage_data.at[zip, 'Cardiovascular Disease']
        return asthma + card + age

    input = pd.read_csv('gs://waitlist_input/input.csv')

    scores = []

    for i in range(len(input)):
        scores += [calc_score(input.get('zip')[i], input.get('age')[i])]

    data = {'name': input.get('first_name') + ' ' + input.get('last_name'), 'zip': input.get('zip'), 'age': input.get('age'), 'score': scores}

    output = pd.DataFrame(data)
    output = output.set_index('name')
    output = output.sort_values('score', ascending=False)
    output = output.drop('score', axis=1)

    output.to_csv('newWaitlist.csv')

    client = storage.Client()
    bucket = client.get_bucket('waitlist_output')
    blob = bucket.blob('newWaitlist.csv')
    blob.upload_from_filename('newWaitlist.csv')