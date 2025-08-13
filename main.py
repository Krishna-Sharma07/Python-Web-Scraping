from bs4 import BeautifulSoup
import requests
Neo = requests.get('https://www.kotaksecurities.com/stocks/').text
soup = BeautifulSoup(Neo, 'lxml')
all_stocks = soup.find_all('a', class_="StockList_stock-list-names__mGEM_ kotak-text-small", href=True)
urls = [stock.get("href") for stock in all_stocks]
def search_stock_Neo(Name):
    #Company name and current price
    lower_split = [word.lower() for word in Name.split()]
    search_name = ('-'.join(lower_split))+'-'
    for i in urls:
        if(search_name in i):
            url = 'https://www.kotaksecurities.com'+ i
            Stock = requests.get(url).text
            soup = BeautifulSoup(Stock, 'lxml')
            Stock_name_detail = soup.find('div', class_ = 'TitleGridAndImage_title-grid-and-image-sub-text__p3ZYo kotak-label-small' )
            Stock_price = soup.find('div', class_ = 'TitleGridAndImage_title-grid-and-image-price-text__GxQMT kotak-heading-2' ).text
            Stock_name= Stock_name_detail.text.split()[0]
            print(f'\nName: {Stock_name}\nCurrent Price: {Stock_price}')
            search_stock_Screener(Stock_name)

def search_stock_Screener(name):
    #company ratio
    url = 'https://www.screener.in/company/' + name + '/consolidated/'
    Stock = requests.get(url).text
    soup = BeautifulSoup(Stock, 'lxml')
    company_ratios = soup.find_all('span', class_="name")
    company_ratios_value = soup.find_all('span', class_='nowrap value')
    for i in range(0,9):
        ratio = company_ratios[i].text
        ratio_vaule_detail = company_ratios_value[i].text.replace(' ', '')
        ratio_vaule_list = ratio_vaule_detail.split()
        ratio_vaule = ''.join(ratio_vaule_list)
        if(i == 1 or i == 5):
            continue
        else:
            print(f'{ratio.strip()}: {ratio_vaule}')
            continue
    #Quarter results
    company_quarter_result = soup.find(id="quarters")
    heading_detail = company_quarter_result.find_all('thead', class_='')
    headings_all = [heading.text.replace('\n','') for heading in heading_detail]
    headings_string = headings_all[0].replace(' ','')
    headings = []
    for i in range(0, len(headings_string), 7):
        headings.append(headings_string[i:i+7])
    heads = headings[-5:]
    sales_interest_expenses_detail = company_quarter_result.find_all('tr')
    for i in sales_interest_expenses_detail:
        if 'Sales' or 'Revenue' in i.text:
            sales = i.text.split('\n')[-6:-1]
        elif 'Interest' in i.text:
            interest = i.text.split('\n')[-6:-1]
        elif 'Expenses' in i.text:
            expenses = i.text.split('\n')[-6:-1]
        
    operating_profit_detail = (company_quarter_result.find('tr', class_="stripe strong") or company_quarter_result.find('tr', class_ = "strong"))
    operating_profit_list = operating_profit_detail.text.split()[-5: ]
    print('                    ', end='')
    print(f'{heads[0]}    {heads[1]}    {heads[2]}    {heads[3]}    {heads[4]}')
    print(f'Sales        {sales[0]}        {sales[1]}        {sales[2]}        {sales[3]}        {sales[4]}')
    print(f'Interest       {interest[0]}        {interest[1]}        {interest[2]}        {interest[3]}        {interest[4]}')
    print(f'Expenses       {expenses[0]}        {expenses[1]}        {expenses[2]}        {expenses[3]}        {expenses[4]}')
    print(f'Operating profit        {operating_profit_list[0]}        {operating_profit_list[1]}        {operating_profit_list[2]}        {operating_profit_list[3]}        {operating_profit_list[4]}')

    #Shareholding patterns
    company_shareholding = soup.find(id='shareholding').find(id='quarterly-shp')
    holding_promoter_dii = company_shareholding.find_all('tr', class_='stripe')
    holding_fii_public = company_shareholding.find_all('tr', class_ = '')
    promoter_detail = [a.text.replace('\n','') for a in holding_promoter_dii if 'Promoter' in a.text]
    promoter_holding = promoter_detail[0].split('%')[-6:-1]
    fii_detail = [a.text.replace('\n','') for a in holding_fii_public if 'FII' in a.text]
    fii_holding = fii_detail[0].split('%')[-6:-1]
    dii_detail = [a.text.replace('\n','') for a in holding_promoter_dii if 'DII' in a.text]
    dii_holding = dii_detail[0].split('%')[-6:-1]
    public_detail = [a.text.replace('\n','') for a in holding_fii_public if 'Public' in a.text]
    public_holding = public_detail[0].split('%')[-6:-1]
    print(f'Promoter Holding      {promoter_holding[0]}      {promoter_holding[1]}      {promoter_holding[2]}      {promoter_holding[3]}      {promoter_holding[4]}')
    print(f'FII Holding           {fii_holding[0]}      {fii_holding[1]}      {fii_holding[2]}      {fii_holding[3]}      {fii_holding[4]}')
    print(f'DII Holding           {dii_holding[0]}      {dii_holding[1]}      {dii_holding[2]}      {dii_holding[3]}      {dii_holding[4]}')
    print(f'Public Holding        {public_holding[0]}      {public_holding[1]}      {public_holding[2]}      {public_holding[3]}      {public_holding[4]}')
        
    #Cycle
    company_cycle = soup.find(id='ratios')
    head_yearly = company_cycle.find('tr').text.replace('\n', '')
    debtor_payable_detail = company_cycle.find_all('tr', class_='stripe')
    for i in debtor_payable_detail:
        if "Debtor" in i.text:
            debtor_days_detail = i.text.split('\n')[-6:-1]
        elif "Payable" in i.text:
            payable_days = i.text.split('\n')[-6:-1]
                
    cash_cycle_detail = company_cycle.find('tr', class_='strong').text.split('\n')[-6:-1]
    heading = head_yearly.replace(' ', '')
    headings = []
    for i in range(0, len(heading), 7):
        headings.append(heading[i:i+7])
    heads = headings[-5:]
    print('                    ', end='')
    print(f'{heads[0]}    {heads[1]}    {heads[2]}    {heads[3]}    {heads[4]}')
    print(f'Debtor Days          {debtor_days_detail[0]}          {debtor_days_detail[1]}          {debtor_days_detail[2]}         {debtor_days_detail[3]}        {debtor_days_detail[4]}')
    print(f'Days Payable          {payable_days[0]}          {payable_days[1]}          {payable_days[2]}         {payable_days[3]}        {payable_days[4]}')
    print(f'Cash Convertion Cycle           {cash_cycle_detail[0]}           {cash_cycle_detail[1]}          {cash_cycle_detail[2]}          {cash_cycle_detail[3]}          {cash_cycle_detail[4]}')
        
    #Cash flow
    company_cash_flow = soup.find(id='cash-flow')
    cash_flow = company_cash_flow.find('tr', class_='stripe').text.split('\n')[-6:-1]
    print(f'Cash from Operational activity         {cash_flow[0]}          {cash_flow[1]}          {cash_flow[2]}         {cash_flow[3]}        {cash_flow[4]}')
        
        
    print('')

name = input("Enter Stock Name: ")
search_stock_Neo(name)