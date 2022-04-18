
def test_module(client: Client) -> str:
    try:
        client.'{your code here}'(max_results=1, start_time='1 day', alert_status=None, alert_type=None,
                             severity=None)
     except DemistoException as e:
        if 'Forbidden' in str(e):
            return 'Authorization Error: make sure API Key is correctly set'
        else:
            raise e
    return '{your code here}'