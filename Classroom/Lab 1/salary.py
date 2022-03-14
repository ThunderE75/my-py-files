# Write a Python script that accepts name, basic salary and displays gross salary.
#. hra=12% of basic_sal
# da=10% of basic_sal
# Gross_sal=basic_sal +da + hra


name = input('Enter you name: ')
basic_sal = float(input('Enter you basic_sal: '))

da =  0.1 * basic_sal
hra = 0.12 * basic_sal
gross_sal = basic_sal + da + hra

print('Gross Salary: ',gross_sal)