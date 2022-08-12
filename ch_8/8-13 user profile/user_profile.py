from building_profile import build_profile

user_profile = build_profile('carl', 'hermanson', middle='fredrik', field='QA', age = '22')

change = list(user_profile.items())

f_name = change[-3]
m_name = change[-2]
l_name = change[-1]

change.insert(0, f_name)
change.insert(1, m_name)
change.insert(2, l_name)

user_profile = dict(change)

print("person:")
for section, info in user_profile.items():
    print(f"- {section}: {info}")