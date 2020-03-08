# Feed Integrations

## How to Implement a Feed Integration

**Requirements**:  
- Demisto Server Version >= 5.5.0
- Having the field `feed: true` in the script part of their yaml.  
- Implementing `fetch-indicators` command.  
- The result should be returned using `demisto.createIndicators()` in batches of upto 2000 indicators (implemented via `batch()` as will be implemented in `CommonServerPython`.
- `demisto.createIndicators()` should receive a list of JSONs containing at least the following fields:
```
{
    "value": <value of the indicator>,
    "type": <type of the indicator>,
    "rawJSON": {
        "value": <value of the indicator>,
        "type": <type of the indicator>,
        <ANY OTHER RELEVANT FIELD FROM THE FEED>
    }
}
```
--- 
Feed integrations have OOTB fields (set via server when creating a new BYOI fetch-indicators integration), that should be included in all feed integrations, and shouldn't be edited:
- `feedInstanceReliability` - Reliability score.
- `expiration` - Used to expose all the other expiration fields.
- `expirationPolicy` - Sets the expiration policy.
- `feed` - Boolean param for toggling Fetch indicators.
