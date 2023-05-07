---
id: relationships
title: Relationships
---

### Relationships

Integrations that have the *create relationships* parameter creates relationships as part of the reputation commands.

```yaml
- defaultvalue: 'true'
  additionalinfo: Create relationships between indicators as part of enrichment.
  display: Create relationships
  name: create_relationships
  required: false
  type: 8
```

#### Steps how to create relationships:
1. Create an *EntityRelationship* object with the relationships data. If more than one relationship exists, create a list and append all of the *EntityRelationship* objects to it.

```python
EntityRelationship(
   name='contains',
   entity_a='1.1.1.1',
   entity_a_type='IP',
   entity_b='2.2.2.2',
   entity_b_type='IP',
   source_reliability='B - Usually reliable',
   brand='My Integration ID')
```
   - When setting the name of the relationship, make sure to choose a value that appear in the the predefined list of [relationships](https://xsoar.pan.dev/docs/reference/api/common-server-python#relationships.)

   - For more information about creating a relationship entity, visit the [EntityRelationship](https://xsoar.pan.dev/docs/reference/api/common-server-python#entityrelationship).
   
2. Use the Common object when creating the indicator and in the relationships key set the list of *EntityRelationship* objects.
3. Use CommandResults, set the relationships key to the list of *EntityRelationship* objects.

## Integrations for reference

[AutoFocus](https://github.com/demisto/content/tree/master/Packs/AutoFocus/Integrations/AutofocusV2) 

[AlienVault OTX](https://github.com/demisto/content/tree/master/Packs/AlienVault_OTX) 

[MISP](https://github.com/demisto/content/tree/master/Packs/MISP/Integrations/MISP_V2)

[DeHashed](https://github.com/demisto/content/tree/master/Packs/DeHashed/Integrations/DeHashed)
