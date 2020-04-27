# numbers = [12, 4, 1, 3, 7, 5, 9]
# numbers.sort()
# print(numbers)
# from operator import itemgetter


# # names = ['Danny', 'Aaron', 'Zack', 'Jennifer', 'Jason', 'Mike', 'David']
# # sorted_names = sorted(names, reverse=True)
# # print(sorted_names)

# def daily_activity(order, day, activity):
#     return {'order': order, 'day': day, 'activity': activity}

# def activity_sorting(activity):
#     return activity['activity']

# mon_activity = daily_activity(0, 'Mon', 'Baseball')
# tue_activity = daily_activity(1, 'Tue', 'Swim')
# wed_activity = daily_activity(2, 'Wed', 'Soccer')
# thu_activity0 = daily_activity(3, 'Thu', 'Basketball')
# thu_activity1 = daily_activity(4, 'Thu', 'Dance')
# thu_activity2 = daily_activity(5, 'Thu', 'Football')
# activities = [mon_activity, tue_activity, wed_activity, thu_activity0, thu_activity1, thu_activity2]

# # sorted_activities = sorted(activities, key=lambda x: x['order'], reverse=True)
# #sorted_activities = sorted(activities, key=itemgetter('day', 'activity'), reverse=True)
# sorted_activities = sorted(activities, key=activity_sorting, reverse=True)
# print(sorted_activities)


# sales_dict = {'Spring': 1000, 'Summer': 950, 'Fall': 1030, 'Winter': 1200}
# sales_list0 = sorted(sales_dict.items(), key=lambda x: x[0])

# sales_list1 = list(sales_dict.items())
# sales_list1.sort(key=lambda x: x[1], reverse=True)
# print(sales_list1)

results1 = {'John': 95, 'Danny': 80, 'Zack': 98}
results2 = {'Danny': 84, 'Zack': 95, 'John': 88}

for name, score in sorted(results2.items()):
    print(f'{name} | Spring: {results1[name]} | Fall: {score}')

