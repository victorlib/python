def describe_city(city, country='china'):
    print(city.title()+' is in '+country.title())


describe_city('上海')
describe_city(city='北京')
describe_city(country='美国', city='纽约')
