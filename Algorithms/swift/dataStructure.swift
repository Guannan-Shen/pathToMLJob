// test array
var perStuPetCount = [0, 1, 3, 1]
var numOfStu = perStuPetCount.count 

print(perStuPetCount[0])
print(numOfStu)

// total pet
var sum = 0
for i in perStuPetCount{
    sum = sum + i
}

print(sum)

var averPet = sum/numOfStu

print(averPet)

