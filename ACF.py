import matplotlib.pyplot as plt

Y_axis_time_series_data = [266,145.9,183.1,119.3,180.3,168.5,231.8,224.5,192.8,122.9,336.5,185.9,194.3,149.5,210.1,273.3,191.4,287,226,303.6,289.9,421.6,264.5,342.3,339.7,440.4,315.9,439.3,401.3,437.4,575.5,407.6,682,475.3,581.3,646.9]
X_axis_time = []
for i in range(1, len(Y_axis_time_series_data) + 1):
	X_axis_time.append(i)
	
plt.plot(X_axis_time, Y_axis_time_series_data)
plt.show()

def get_lagged_list(list, lag):
	if lag == 0:
		return list
	else:
		lagged_list = [0] + list
		lagged_list.pop()
		return get_lagged_list(lagged_list, lag - 1)	

def get_average(list):
	return sum(list)/len(list)	

def list_subtract(list, value):
	return [(element - value) for element in list]

def list_squared(list):
	return [(element ** 2) for element in list]

def get_auto_correlation(list1, list2, lag):
	numerator = sum(list1 [lag:len(list1)] )
	denominator = sum(list2)
	return numerator/denominator 

def get_correlogram(time_series_data, number_of_lags = 20):
	Y = time_series_data
	acf_y_axis = []
	Y_bar = get_average(Y)
	Y_minus_Y_bar = list_subtract(Y, Y_bar)
	Y_minus_Y_bar_squared = list_squared(Y_minus_Y_bar)
	for lag in range(1, number_of_lags + 1):
		Y_lagged_x = get_lagged_list(Y, lag)
		Y_lagged_x_minus_Y_bar = list_subtract(Y_lagged_x, Y_bar)
		Y_minus_Y_bar_multiplied_Y_lagged_x_minus_Y_bar = [a*b for a,b in zip(Y_minus_Y_bar, Y_lagged_x_minus_Y_bar)]
		auto_correlation_x = get_auto_correlation(Y_minus_Y_bar_multiplied_Y_lagged_x_minus_Y_bar, Y_minus_Y_bar_squared, lag)
		acf_y_axis.append(auto_correlation_x)
	return acf_y_axis

number_of_lags = 20
Y_axis_ACF = get_correlogram(Y_axis_time_series_data, number_of_lags)
X_axis_lag = []
for i in range(1, number_of_lags + 1):
	X_axis_lag.append(i)

plt.step(X_axis_lag, Y_axis_ACF)
plt.show()

