# 7.1
years_list = [year for year in range(1979, 1985)]
print(years_list)

# 7.2
print(years_list[3])

# 7.3
print(years_list[-1])

# 7.4
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5
things1 = [title.title() for title in things]
print(things1)

# 7.6
things2 = [cheese.upper() for cheese in things if cheese.endswith("rella") ]
print(things2)

# 7.7
things3 = [thing for thing in things if not thing.startswith("sal")]
print(things3)
