import csv
import json

headers_csv = ['Company_name', 'Website', 'DescriptionEN', 'DescriptionCN', 'CountryName', 'IndustryIndex',
               'BoothNumber', 'Email', 'Youtube', 'Linkedin']

with open('detailed_info_company.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers_csv)

with open('data.json') as f:
    data = json.load(f)
counter = 0
for item in data["company"]:
    counter += 1
    Company_name = item['CompanyNEn']
    Website = item['Website']
    DescriptionEN = item['CompanyDescriptionEN']
    DescriptionCN = item['CompanyDescriptionCN']
    CountryName = item['countryname']
    IndustryIndex = item['Industryindex']
    BoothNumber = item['BoothNo']
    Email = item['Email']
    Youtube = item['YouTube']
    Linkedin = item['LinkedIn']

    with open('detailed_info_company.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([Company_name, Website, DescriptionEN, DescriptionCN, CountryName, IndustryIndex,
                         BoothNumber, Email, Youtube, Linkedin])
    print(Company_name, f'{counter} of {len(data["company"])} DOWLOADED')
