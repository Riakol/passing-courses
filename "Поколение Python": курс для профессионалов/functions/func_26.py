from datetime import date

def date_formatter(country_code):
    def func(dt):
        date_formats = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y',
                        'ca': '%Y-%m-%d', 'br': '%d/%m/%Y',
                        'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y',}
        return date.strftime(dt, date_formats[country_code])
    return func
