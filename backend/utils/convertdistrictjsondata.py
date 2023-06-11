import json
from typing import Dict


# Read District with it's municipalities from json db
def readDB() -> Dict:
    with open('../data/db/district_with_municipalities.json') as file:
        districts = json.load(file)

    return districts


# Create/Write new fixture data to insert into Django model


def createFixture():
    districts = readDB()
    district_fixture_list = []
    municipality_fixture_list = []
    district_counter = 1
    municipality_counter = 1
    for district, municipalities_dict in districts.items():
        district_data = {
            "model": "api.District",
            "pk": district_counter,
            "fields": {
                "name": district,
            },
        }
        for municipality_type, municipalities_list in municipalities_dict.items():
            for municipality in municipalities_list:
                type_temp = ""
                if municipality_type == "Ma.Na.Pa.":
                    type_temp = "MAHAHAGAR"
                elif municipality_type == "Upa.Ma.":
                    type_temp = "UPAMAHANAGAR"
                elif municipality_type == "Na.Pa.":
                    type_temp = "NAGARPALIKA"
                elif municipality_type == "Ga.Pa.":
                    type_temp = "GHAUPALIKA"
                municipality_data = {
                    "model": "api.Municipality",
                    "pk": municipality_counter,
                    "fields": {
                        "name": municipality,
                        "type": type_temp,
                        "district": district_counter,
                    },
                }
                municipality_counter += 1
                municipality_fixture_list.append(municipality_data)
        district_fixture_list.append(district_data)
        district_counter += 1
    # print(district_fixture)
    district_fixture_json = json.dumps(district_fixture_list, indent=4)
    municipality_fixture_json = json.dumps(municipality_fixture_list, indent=4)

    with open('../fixtures/district.json', 'w') as file:
        file.write(district_fixture_json)

    with open('../fixtures/municipality.json', 'w') as file:
        file.write(municipality_fixture_json)


createFixture()
