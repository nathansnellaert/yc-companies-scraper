# Mapping from ycombinator country names to country codes
country_name_to_code = {
    "Taiwan": "TW",
    "Antarctica": "AQ",
    "Fiji": "FJ",
    "New Caledonia": "NC",
    "Papua New Guinea": "PG",
    "Solomon Islands": "SB",
    "Vanuatu": "VU",
    "American Samoa": "AS",
    "Cook Islands": "CK",
    "French Polynesia": "PF",
    "Niue": "NU",
    "Pitcairn Islands": "PN",
    "Samoa": "WS",
    "Tokelau": "TK",
    "Tonga": "TO",
    "Tuvalu": "TV",
    "Wallis and Futuna": "WF",
    "Guam": "GU",
    "Kiribati": "KI",
    "Marshall Islands": "MH",
    "Federated States of Micronesia": "FM",
    "Nauru": "NR",
    "Northern Mariana Islands": "MP",
    "Palau": "PW",
    "United States Minor Outlying Islands": "UM",
    "Kazakhstan": "KZ",
    "Kyrgyzstan": "KG",
    "Tajikistan": "TJ",
    "Turkmenistan": "TM",
    "Uzbekistan": "UZ",
    "China": "CN",
    "Hong Kong": "HK",
    "Macao": "MO",
    "North Korea": "KP",
    "Japan": "JP",
    "Mongolia": "MN",
    "South Korea": "KR",
    "Armenia": "AM",
    "Azerbaijan": "AZ",
    "Bahrain": "BH",
    "Cyprus": "CY",
    "Georgia": "GE",
    "Iraq": "IQ",
    "Israel": "IL",
    "Jordan": "JO",
    "Kuwait": "KW",
    "Lebanon": "LB",
    "Oman": "OM",
    "Qatar": "QA",
    "Saudi Arabia": "SA",
    "Palestine": "PS",
    "Syria": "SY",
    "Turkey": "TR",
    "United Arab Emirates": "AE",
    "Yemen": "YE",
    "Afghanistan": "AF",
    "Bangladesh": "BD",
    "Bhutan": "BT",
    "India": "IN",
    "Iran": "IR",
    "Maldives": "MV",
    "Nepal": "NP",
    "Pakistan": "PK",
    "Sri Lanka": "LK",
    "Belarus": "BY",
    "Bulgaria": "BG",
    "Czechia": "CZ",
    "Hungary": "HU",
    "Poland": "PL",
    "Moldova": "MD",
    "Romania": "RO",
    "Russia": "RU",
    "Slovakia": "SK",
    "Ukraine": "UA",
    "Austria": "AT",
    "Belgium": "BE",
    "France": "FR",
    "Germany": "DE",
    "Liechtenstein": "LI",
    "Luxembourg": "LU",
    "Monaco": "MC",
    "Netherlands": "NL",
    "Switzerland": "CH",
    "Algeria": "DZ",
    "Egypt": "EG",
    "Libya": "LY",
    "Morocco": "MA",
    "Sudan": "SD",
    "Tunisia": "TN",
    "Western Sahara": "EH",
    "Denmark": "DK",
    "Estonia": "EE",
    "Faroe Islands": "FO",
    "Finland": "FI",
    "Iceland": "IS",
    "Ireland": "IE",
    "Isle of Man": "IM",
    "Latvia": "LV",
    "Lithuania": "LT",
    "Norway": "NO",
    "Svalbard and Jan Mayen": "SJ",
    "Sweden": "SE",
    "United Kingdom": "GB",
    "Aland Islands": "AX",
    "Albania": "AL",
    "Andorra": "AD",
    "Bosnia and Herzegovina": "BA",
    "Croatia": "HR",
    "Gibraltar": "GI",
    "Greece": "GR",
    "Vatican City": "VA",
    "Italy": "IT",
    "Malta": "MT",
    "Montenegro": "ME",
    "Portugal": "PT",
    "San Marino": "SM",
    "Serbia": "RS",
    "Slovenia": "SI",
    "Spain": "ES",
    "North Macedonia": "MK",
    "Bermuda": "BM",
    "Canada": "CA",
    "Greenland": "GL",
    "Saint Pierre and Miquelon": "PM",
    "United States": "US",
    "Brunei": "BN",
    "Cambodia": "KH",
    "Indonesia": "ID",
    "Laos": "LA",
    "Malaysia": "MY",
    "Myanmar": "MM",
    "Philippines": "PH",
    "Singapore": "SG",
    "Thailand": "TH",
    "Timor-Leste": "TL",
    "Vietnam": "VN",
    "Australia": "AU",
    "Christmas Island": "CX",
    "Cocos (Keeling) Islands": "CC",
    "Heard Island and McDonald Islands": "HM",
    "New Zealand": "NZ",
    "Norfolk Island": "NF",
    "Anguilla": "AI",
    "Antigua and Barbuda": "AG",
    "Aruba": "AW",
    "Bahamas": "BS",
    "Barbados": "BB",
    "Caribbean Netherlands": "BQ",
    "British Virgin Islands": "VG",
    "Cayman Islands": "KY",
    "Cuba": "CU",
    "Cura\u00e7ao": "CW",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Grenada": "GD",
    "Guadeloupe": "GP",
    "Haiti": "HT",
    "Jamaica": "JM",
    "Martinique": "MQ",
    "Montserrat": "MS",
    "Puerto Rico": "PR",
    "Saint Barth\u00e9lemy": "BL",
    "Saint Kitts and Nevis": "KN",
    "Saint Lucia": "LC",
    "Saint Martin": "MF",
    "Saint Vincent and the Grenadines": "VC",
    "Sint Maarten": "SX",
    "Trinidad and Tobago": "TT",
    "Turks and Caicos Islands": "TC",
    "U.S. Virgin Islands": "VI",
    "Angola": "AO",
    "Cameroon": "CM",
    "Central African Republic": "CF",
    "Chad": "TD",
    "Congo": "CG",
    "DR Congo": "CD",
    "Equatorial Guinea": "GQ",
    "Gabon": "GA",
    "Sao Tome and Principe": "ST",
    "Argentina": "AR",
    "Bolivia": "BO",
    "Bouvet Island": "BV",
    "Brazil": "BR",
    "Chile": "CL",
    "Colombia": "CO",
    "Ecuador": "EC",
    "Falkland Islands": "FK",
    "French Guiana": "GF",
    "Guyana": "GY",
    "Paraguay": "PY",
    "Peru": "PE",
    "South Georgia and the South Sandwich Islands": "GS",
    "Suriname": "SR",
    "Uruguay": "UY",
    "Venezuela": "VE",
    "British Indian Ocean Territory": "IO",
    "Burundi": "BI",
    "Comoros": "KM",
    "Djibouti": "DJ",
    "Eritrea": "ER",
    "Ethiopia": "ET",
    "French Southern Territories": "TF",
    "Kenya": "KE",
    "Madagascar": "MG",
    "Malawi": "MW",
    "Mauritius": "MU",
    "Mayotte": "YT",
    "Mozambique": "MZ",
    "Rwanda": "RW",
    "Reunion": "RE",
    "Seychelles": "SC",
    "Somalia": "SO",
    "South Sudan": "SS",
    "Uganda": "UG",
    "Tanzania": "TZ",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
    "Benin": "BJ",
    "Burkina Faso": "BF",
    "Cabo Verde": "CV",
    "Ivory Coast": "CI",
    "Gambia": "GM",
    "Ghana": "GH",
    "Guinea": "GN",
    "Guinea-Bissau": "GW",
    "Liberia": "LR",
    "Mali": "ML",
    "Mauritania": "MR",
    "Niger": "NE",
    "Nigeria": "NG",
    "Saint Helena": "SH",
    "Senegal": "SN",
    "Sierra Leone": "SL",
    "Togo": "TG",
    "Belize": "BZ",
    "Costa Rica": "CR",
    "El Salvador": "SV",
    "Guatemala": "GT",
    "Honduras": "HN",
    "Mexico": "MX",
    "Nicaragua": "NI",
    "Panama": "PA",
    "Guernsey": "GG",
    "Jersey": "JE",
    "Botswana": "BW",
    "Eswatini": "SZ",
    "Lesotho": "LS",
    "Namibia": "NA",
    "South Africa": "ZA",
    # edge cases
    'USA': 'US',
    'Democratic Republic of the Congo': 'CD',
    'TW': 'TW',
}