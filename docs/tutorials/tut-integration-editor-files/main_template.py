
def main() -> None:

    api_key = demisto.params().get('apikey')
    base_url = urljoin(demisto.params()['url'], '/api/v1')
    verify_certificate = not demisto.params().get('insecure', False)
    proxy = demisto.params().get('proxy', False)

    demisto.debug(f'Command being called is {demisto.command()}')
    try:
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        client = Client(
            base_url=base_url,
            verify=verify_certificate,
            headers=headers,
            proxy=proxy)

        if demisto.command() == 'test-module':
            result = '{your code here}'(client)
            return_results(result)

        elif demisto.command() == '{your code here}':
            return_results(search_alerts_command(client, demisto.args()))

    except Exception as e:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute {demisto.command()} command.\nError:\n{str(e)}')

