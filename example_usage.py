from client import ClientSideHydrationRuntimeErrorTriageClient

def main():
    client = ClientSideHydrationRuntimeErrorTriageClient()
    res = client.triage_hydration_error()
    print('Hydration Triage: ' + res['triage_id'] + ' (' + res['root_cause'] + ')')
    print('Fix Pattern: ' + res['recommended_fix_pattern'])
    print('Dossier URL: ' + res['triage_dossier_url'])

if __name__ == '__main__':
    main()
