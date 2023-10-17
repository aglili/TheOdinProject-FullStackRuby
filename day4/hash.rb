

new_hash = Hash.new


new_hash["a"] = "apple"
new_hash["b"] = "ball"


new_hash["b"] = "brazil"


new_hash2 = {
    "c" => "crab",
    "d" => "dog"
}


print new_hash.merge(new_hash2)


fruits = {
    :apple => "Apple",
    :strawberry => "Strawberry",
    :guava => "Guava"

}




print fruits.fetch(:apple)