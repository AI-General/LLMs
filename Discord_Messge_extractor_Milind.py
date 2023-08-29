# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B2dO_k2I3TVcJKa3OQvQhETXNsT1ulLR
"""

import requests
import json
import csv

def retrieve_messages(channelid):
    num = 0
    limit = 10

    headers = {
        'authorization': 'Your_Token' #Enter  you own token
    }

    last_message_id = None
    messages = []  # Initialize an empty list to store message content and IDs

    while True:
        query_parameters = f'limit={limit}'
        if last_message_id is not None:
            query_parameters += f'&before={last_message_id}'

        r = requests.get(
            f'https://discord.com/api/v9/channels/{channelid}/messages?{query_parameters}', headers=headers
        )
        jsonn = json.loads(r.text)
        if len(jsonn) == 0:
            break

        for value in jsonn:
            message_content = value['content']
            message_id = value['id']
            messages.append([message_id, message_content])
            last_message_id = message_id
            num += 1
            print(f'Retrieving message {num} - ID: {message_id}')

    print('Number of messages collected:', num)
    return messages

def save_to_csv(messages, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['ID', 'Message'])
        csv_writer.writerows(messages)
    print(f'Saved {len(messages)} messages to {filename}')

channel_id = '702878028841091093'  # Replace with your desired channel ID
print('Fetching messages...')
saved_messages = retrieve_messages(channel_id)
print('Fetching messages completed!')
print('Saving to CSV...')
save_to_csv(saved_messages, 'messages.csv')
print('Saving to CSV completed!')

