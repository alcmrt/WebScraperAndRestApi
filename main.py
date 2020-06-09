"""
Run web_scrapper module to get data of the cars
"""

import web_scraper as ws

if __name__ == '__main__':

    # url for BMW cars
    URL = "https://www.cars.com/for-sale/searchresults.action/?mkId=20005&dealerType=localOnly&page=1&perPage=100&searchSource=GN_BREADCRUMB&sort=relevance&zc=90006"

    ##
    # get list of BMW cars from given url, and store to database
    ##
    car_list = ws.get_list_of_cars(URL)
    car_list_with_extracted_information = ws.extract_information_of_cars(car_list)
    ws.store_car_data(car_list_with_extracted_information)

    # url for Ford cars
    URL = "https://www.cars.com/for-sale/searchresults.action/?mkId=20015&dealerType=localOnly&page=1&perPage=100&searchSource=GN_BREADCRUMB&sort=relevance&zc=90006"

    ##
    # get list of Ford cars from given url, and store to database
    ##
    car_list = ws.get_list_of_cars(URL)
    car_list_with_extracted_information = ws.extract_information_of_cars(car_list)
    ws.store_car_data(car_list_with_extracted_information)