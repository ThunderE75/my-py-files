# If you run a 10-kilometer race in 43 minutes 30 seconds, 
# Calculate your average time per mile and your average speed in miles per hour using Python
# Calculator. (Hint: there are 1.61 kilometers in a mile).


km = 10.0
mi = (km * (1.0 / 1.61))

sec = ((43.0*60)+30.0)
hrs = (43.5/60.0)

print ('Avg time per Mile: ', sec/ mi, 'sec/mile')
print ('Avg Speed per Mile: ', mi/ hrs, 'mile/hr')
