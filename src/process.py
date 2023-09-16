from src.mapping import country_name_to_code

def parse_location(location):
        # print(location)
        split = location.split(',')
        # remove empty strings
        split = [s.strip() for s in split if s.strip()]
        if len(split) == 0:
            return None
        
        city, state, country = [None, None, None]
        if len(split) == 3:
            city, state, country = split
        elif len(split) == 2:
            state, country = split
        elif len(split) == 1:
            country, = split

        if country is not None:
            country = country_name_to_code.get(country, None)

        return {'city': city, 'state': state, 'country': country}

def process_company(company):

    # Process location into a more structured format
    locations = company['all_locations']
    locations = [l.strip() for l in locations.split(';')]

    if 'Remote' in locations:
        locations.remove('Remote')
        company['remote'] = True
    else:
        company['remote'] = False

    # sometimes remote is not listed in all_locations, but in regions. 
    if 'Remote' in company['regions']:
        company['remote'] = True

    locations = list(set(locations))
    locations = [parse_location(l) for l in locations]  
    locations = [l for l in locations if l is not None]

    # TODO: add more props and improve processing of existing props
    return {
        'id': company['slug'],
        'name': company['name'],
        'logo_url': company['small_logo_thumb_url'] if not '/company/thumb/missing.png' in company['small_logo_thumb_url'] else None,
        'website': company['website'],
        'long_description': company['long_description'],
        'one_liner': company['one_liner'],
        'team_size': company['team_size'],
        'locations': locations,
        'industry': company['industry'],
        'remote': company['remote'],
        'subindustry': company['subindustry'].split('->')[-1].strip(),
        'tags': company['tags'],
        'batch': company['batch'],
        'batch_year': company['batch_year'],
        "batch_type": company['batch_type'],
        'status': company['status'],
        'regions': company['regions'],
    }