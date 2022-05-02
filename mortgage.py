house_price = 700_000
down_pay_percent = 0.20
mortgage_years = 30
mortgage_rate = 0.055

initial_payment = house_price * down_pay_percent
loan_amount = house_price - initial_payment
monthly_mortgage_rate = mortgage_rate / 12
mortgage_months = mortgage_years * 12

inflation_rate = 0.03
total_housing_price_decrease_inflation_adjusted = 0.20
depreciation_rate = 0.03636

# amortization with simple interest
monthly_payment = loan_amount * monthly_mortgage_rate / (1 - (1 + monthly_mortgage_rate) ** -mortgage_months)

house_price_at_end = house_price * (1 + inflation_rate - depreciation_rate) ** mortgage_years * (1 - total_housing_price_decrease_inflation_adjusted)
total_payment = initial_payment + monthly_payment * 12 * mortgage_years
total_house_gain = house_price_at_end - total_payment

print("House price at end:", house_price_at_end)
print("Total house payment:", total_payment)
print("Total house value:", total_house_gain)

monthly_rent = 3_000
annual_rent = monthly_rent * 12
rent_rise_rate = inflation_rate
total_rent_cost = annual_rent * ((rent_rise_rate * (rent_rise_rate + 1) ** mortgage_years) + (rent_rise_rate + 1) ** mortgage_years - 1) / rent_rise_rate
total_rent_gain = -total_rent_cost

print("Total rent value:", total_rent_gain)
print("House value over renting:", total_house_gain - total_rent_gain)
breakpoint()
