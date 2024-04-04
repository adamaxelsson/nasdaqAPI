from collections import Counter

def remove_dups(d):
    temp = {val: key for key, val in d.items()}
    res = {val: key for key, val in temp.items()}
    return res

def get_companies_from_country(name_dict, country_dict):
    companies_per_country_dict = {}

    for company_id, country in country_dict.items():
        company_name = name_dict.get(company_id)
        if company_name:
            companies_per_country_dict.setdefault(country, []).append(company_name)

    for country, company_names in companies_per_country_dict.items():
        companies_per_country_dict[country] = [len(company_names), (company_names)]

    return companies_per_country_dict


"""
def get_companies_from_country(name_dict, country_dict):
    country_list = []
    companies_per_country_dict = {}

    for company in country_dict.items():
        if company[1] not in country_list:
            country_list.append(company[1])

    for country in country_list:
        company_id_list = []
        company_name_list = []

        for company in country_dict.items():
            if company[1] == country:
                company_id_list.append(company[0])
        for company in name_dict.items():
            if company[0] in company_id_list:
                company_name_list.append(company[1])

        companies_per_country_dict[country] = [len(company_name_list), company_name_list]
    return companies_per_country_dict
"""