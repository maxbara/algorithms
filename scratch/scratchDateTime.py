from datetime import datetime

# ISO 8601 from Azure appinsights
d = datetime.fromisoformat("2022-09-15T01:21:44.732Z".replace('Z', '+00:00'))
print(d)

# acquire now
d2 = datetime.now()
print(d2)

# strictly takes only 10 characters
d3 = datetime.fromisoformat("2022-09-15")
print(d3)


