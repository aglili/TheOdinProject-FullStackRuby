friends = ["john","kwame","amarae","kwesi"]

invitation_list = []

# for friend in friends do
#   if friend != "john"
#   invitation_list.push(friend)
#   end
# end

# print invitation_list


print friends.select{|friend| friend != "john"}