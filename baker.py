#!/usr/bin/python

'''Gathering acutal housing expenses from person and save results
   in variables to be called later'''

print('We are going to go over some of your monthly expenses, please answer in all lowercase')



mortgage_rent = input('Do you have a mortgage or rent?')

if mortgage_rent == 'mortgage':

    mortgage_1 = input('How much is your mortgage?')

    mortgage_2 = input('Do you have a second mortage payment; if so, how much is your payment?')

    rent = '0'
else:

    rent = input('How much is your rent?')

    mortgage_1 = '0'

    mortgage_2 = '0'
        

electric = input('How much is your electric bill?')

gas = input('How much is your home gas bill?')



phone = input('Are your phone, internet and cable all together?')

if phone == 'yes':

    phone_cable_internet = input('How much is your phone/internet/cable bill?')

    home_phone = '0'

    cell_phone = '0'

    cable = '0'

    internet = '0'
    
else:
    
    home_phone = input('How much is your home phone bill?')

    cell_phone = input('How much is your cell phone bill?')

    cable = input('How much is your cable bill?')

    internet = input('How much is your internet bill?')

    phone_cable_internet = '0'

water_sewer = input('How much is your water and sewer bill?')

trash = input('How much is your trash bill?')

home_insurance = input('How much is your home or renters insurance bill?')

property_taxes = input('How much is are your property taxes?')



total_actual_housing = int(mortgage_1) + int(mortgage_2) + int(rent) + int(electric) + int(gas) + int(phone_cable_internet) + int(home_phone) + int(cell_phone) + int(cable) + int(internet) + int(water_sewer) + int(trash) + int(home_insurance) + int(property_taxes)


print('Total actual housing expenses' + ' ' + total_actual_housing)