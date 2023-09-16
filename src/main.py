import json
import pandas as pd
import os
import argparse
from process import process_company
from download import download_ycombinator_companies

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract and process company data')
    
    parser.add_argument('--start_year', type=int, required=True, help='Start year for data extraction')
    parser.add_argument('--end_year', type=int, required=True, help='End year for data extraction', default=2030)
    
    args = parser.parse_args()

    if args.end_year < args.start_year:
        parser.error('End year should be greater than or equal to start year.')

    algolia_config = {
        "url": "https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries",
        "app_id": "45BWZJ1SGC",
        "api_key": "Zjk5ZmFjMzg2NmQxNTA0NGM5OGNiNWY4MzQ0NDUyNTg0MDZjMzdmMWY1NTU2YzZkZGVmYjg1ZGZjMGJlYjhkN3Jlc3RyaWN0SW5kaWNlcz1ZQ0NvbXBhbnlfcHJvZHVjdGlvbiZ0YWdGaWx0ZXJzPSU1QiUyMnljZGNfcHVibGljJTIyJTVEJmFuYWx5dGljc1RhZ3M9JTVCJTIyeWNkYyUyMiU1RA%3D%3D",
        "index_name": "YCCompany_production" 
    }

    companies = download_ycombinator_companies(args.start_year, args.end_year, algolia_config)
    companies = [process_company(company) for company in companies]
    
    with open(os.path.join('data', 'companies.json'), 'w') as f:
        json.dump(companies, f, indent=4)
