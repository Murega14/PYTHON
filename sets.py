# a set is a collection which is unordered and unindexed
# sets do not accept duplicate values

brands = {"nike", "adidas", "puma"}
os = {"ios", "android"}
#to add
brands.add("reebok")
#to remove
brands.remove("puma")
#to join the two sets
both = brands.union(os)


for x in both:
    print(x)

utensils = {"fork", "spoon", "knife", "cup"}
dishes = {"bowl", "plate", "cup", "knife"}
#to compare between the two sets
#for example to see whats not common in both sets
print(utensils.difference(dishes))
#to check what they have in common
print(utensils.intersection(dishes))