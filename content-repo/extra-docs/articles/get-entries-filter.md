# getEntries Filter
When building a script, you can fetch entries from an incident. If you do not specify the incident id number, the script fetches from the current incident.  You have the option to create a filter to limit the search results. 

| Filter        | Description           | 
| ------------- |-------------|   
| pageSize     | The number of entries to return.      |   
| lastId | Return entries starting from the specified entry ID and backward.     |   
| firstID     | The number of entries to return.      |   
| lastId | Return entries starting from the specified entry ID and forward.     |   
| selectedEntryID     | Return entries before and after the specified entry ID.   |   
| categories |  Return entries with the specified categories (array). {commandAndResults, playbookTaskResult, playbookTaskStartAndDone, playbookErrors, justFound, deleted, incidentInfo, chats, evidence, notes, attachments}    |   
| tags     |  Return entries with the specified tags (array).     |   
| users |   Return entries with the specified users (array).   |   
| tagsAndOperator     |  Return entries that include all specified tags.   |   
| fromTime |  Return entries from this time and forward.    |   
| parentID     | Return entries from this time and backward.    |   

### Example: Grab all entries that have been marked as a note:

```
res = demisto.executeCommand("getEntries", {"filter": {"categories": ["notes"]}})
demisto.results(str(res))
```

Response
```
[{
        u 'Category': u 'Builtin',
        u 'ModuleName': u 'InnerServicesModule',
        u 'System': u '',
        u 'Note': True,
        u 'Version': 2,
        u 'ReadableContentsFormat': u '',
        u 'Type': 1,
        u 'Metadata': {
            u 'reputationSize': 0,
            u 'startDate': u '0001-01-01T00:00:00Z',
            u 'recurrent': False,
            u 'sortValues': None,
            u 'file': u '',
            u 'retryTime': u '0001-01-01T00:00:00Z',
            u 'previousAllReadWrite': False,
            u 'endingDate': u '0001-01-01T00:00:00Z',
            u 'id': u '96@42646',
            u 'contents': u '',
            u 'cronView': False,
            u 'category': u 'chat',
            u 'note': True,
            u 'isTodo': False,
            u 'format': u 'markdown',
            u 'system': u '',
            u 'mirrored': False,
            u 'hasRole': False,
            u 'pinned': False,
            u 'instance': u 'Builtin',
            u 'version': 2,
            u 'parentId': u '',
            u 'type': 1,
            u 'brand': u 'Builtin',
            u 'timezoneOffset': 0,
            u 'scheduled': False,
            u 'parentEntryTruncated': False,
            u 'previousRoles': None,
            u 'allRead': False,
            u 'allReadWrite': False,
            u 'incidentCreationTime': u '0001-01-01T00:00:00Z',
            u 'ShardID': 0,
            u 'reputations': None,
            u 'user': u 'admin',
            u 'taskId': u '',
            u 'parentContent': u '!getEntries filter="{\\"categories\\":[\\"notes\\"]}"',
            u 'fileMetadata': None,
            u 'tags': None,
            u 'tagsRaw': None,
            u 'errorSource': u '',
            u 'entryTask': None,
            u 'roles': None,
            u 'created': u '2021-03-08T18:47:47.786120529Z',
            u 'IndicatorTimeline': None,
            u 'modified': u '2021-03-08T18:47:51.032485206Z',
            u 'times': 0,
            u 'investigationId': u '42646',
            u 'dbotCreatedBy': u 'admin',
            u 'playbookId': u '',
            u 'contentsSize': 14,
            u 'previousAllRead': False,
            u 'fileID': u ''
        },
        u 'ContentsFormat': u 'markdown',
        u 'Tags': None,
        u 'Brand': u 'Builtin',
        u 'HumanReadable': None,
        u 'ID': u '96@42646',
        u 'FileID': u '',
        u 'IgnoreAutoExtract': False,
        u 'IndicatorTimeline': None,
        u 'Evidence': False,
        u 'EntryContext': None,
        u 'Contents': u 'This is a note',
        u 'File': u '',
        u 'EvidenceID': u '',
        u 'FileMetadata': None,
        u 'ImportantEntryContext': None
    }
]
```
